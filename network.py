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
            os.system(fr"git clone https://github.com/{cmd}.git")
        elif cmd == "install --default":
            os.system(r"git clone https://github.com/Habejota/OSystem.git")
        elif cmd == "clear":
            os.system("cls")
        elif cmd == "update":
            os.chdir("os")
            os.system("git pull")
            
        elif cmd == "ls":
            pasta = os.getcwd()
            for diretorio, subpastas, arquivos in os.walk(pasta):
                for arquivo in arquivos:
                    print(os.path.join(os.path.realpath(diretorio), arquivo))
        elif cmd == "reboot":
            os.system("python boot.py")
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
    