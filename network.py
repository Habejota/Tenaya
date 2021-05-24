from bios import *
from socket import gethostname, gethostbyname
import os

print("Booting from Network shell. . .")

while True:
    try:
        cmd: str = input("[~] ").strip()
        if cmd.startswith("pack"):
            cmd = cmd.replace("pack ", "")
            cmd = cmd.replace("pack", "")
            shell(fr"git clone https://github.com/{cmd}.git")
        elif cmd.startswith("install"):
            cmd = cmd.replace("install ", "")
            cmd = cmd.replace("install", "")
            shell(f"move {cmd}\*.* os")
        elif cmd == "ls":
            pasta = 'E:\TARDIS'
            for diretorio, subpastas, arquivos in os.walk(pasta):
                for arquivo in arquivos:
                    print(os.path.join(os.path.realpath(diretorio), arquivo))
        elif cmd == "reboot":
            shell("python boot.py")
            break
        elif cmd == "exit":
            input("Press ENTER to turn off the computer. . .")
            break
    except KeyboardInterrupt:
        input("Press ENTER to turn off the computer. . .")
        break
    