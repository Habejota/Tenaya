from bios import *
from socket import gethostname, gethostbyname
import os

print("Booting from Network. . .")
print("\n")
print("Https socket server: Git Manager")
print("Welcome to Client Line Interface Git Merge!\n")

while True:
    try:
        cmd: str = input("[~] ").strip()
        if cmd.startswith("pkg"):
            cmd = cmd.replace("pkg ", "")
            cmd = cmd.replace("pkg", "")
            shell(fr"git clone https://github.com/{cmd}.git")
        elif cmd == "update":
            os.chdir("os")
            os.system("git pull")
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
        elif cmd == "":
            continue
        else:
            print("Sorry! Cannot execute this command!")
    except KeyboardInterrupt:
        input("Press ENTER to turn off the computer. . .")
        break
    