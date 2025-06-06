# Forward Shell

## Descripción
Este script establece una shell remota utilizando solicitudes HTTP y técnicas de codificación base64 para ejecutar comandos en el sistema objetivo. Puede enviar comandos y recibir respuestas desde un servidor remoto especificado.

## Requisitos
- Python 3.x
- Librería `requests` (instalar con pip):
```bash
pip install requests
```
- Acceso de red al servidor remoto especificado en el script.

## Instalación
1. Clona el repositorio o guarda los scripts en tu máquina.
2. Asegúrate de que ambos scripts tengan permisos de ejecución:
```bash
chmod +x main.py forwardshell.py
```

## Uso
Ejecuta el script principal con permisos adecuados:
```bash
python3 main.py
```

### Comandos Disponibles
- Comandos del sistema operativo (ej: ls, whoami, id, pwd, etc.).
- Comando especial: `enum suid` para enumerar archivos SUID en el sistema remoto.
- Comando especial: `help` para mostrar opciones disponibles.
- Comando especial: `exit` para salir del terminal pseudo-interactivo.

### Salida Esperada
- Ejecuta comandos y recibe la salida del sistema remoto.
- En modo pseudo-terminal (`script /dev/null -c bash`), muestra la respuesta de manera más interactiva.
- Al salir muestra:
```
[+] Exiting pseudo terminal...
```
- Si se presiona Ctrl+C durante la ejecución, se muestra:
```
[!] Exiting...
```


