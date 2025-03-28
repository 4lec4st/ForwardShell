#!/usr/bin/env python3

import signal
import sys
from forwardshell import ForwardShell

def def_handler(signal, frame):
    print("\n[!] Exiting...")
    my_shell.remove_data()
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

if __name__ == "__main__":
    my_shell = ForwardShell()
    my_shell.run()