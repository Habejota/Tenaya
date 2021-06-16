from socket import gethostname, gethostbyname
import os

print("Booting from Network. . .")
print("\n")
input("")

os.system("title Network Driver System: iPXE")
os.system("cls")
print("iPXE -- Open Source Network Boot Firmware -- http://ipxe.org")
print("Features: HTTP iSCSI DNS TFTP AoE FCoE TFTP COMBOOT ELF PXE PXEXT")

while True:
    try:
        cmd: str = input("iPXE> ").strip()
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
            os.chdir("..")
            os.system("boot.exe")
            break
        elif cmd == "ls":
            pasta = os.getcwd()
            for diretorio, subpastas, arquivos in os.walk(pasta):
                for arquivo in arquivos:
                    print(os.path.join(os.path.realpath(diretorio), arquivo))
        elif cmd == "reboot":
            os.system("boot.exe")
            break
        elif cmd == "exit":
            break
        elif cmd == "":
            continue
        elif cmd == "ifstat":
            print(""" net0: 52:54:00:12:34:56 using rtl8139 on PCI00:03.0 (Ethernet) [closed]\n[Link:up, TX:0 TXE:0 RX:0 RXE:0]""")
        elif cmd == "route":
            print("net0: 10.0.0.155/255.255.255.0 gw 10.0.0.1")
        
        
        
        
        else:
            print("Sorry! Cannot execute this command!")
    except KeyboardInterrupt:
        input("\n\nPress ENTER to turn off the computer. . .")
        break
    