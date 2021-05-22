import time  # Importing Time module
import PySimpleGUI as sg  # Import module to construct gui
from os import *  # Import all of os Python module
from socket import gethostname, gethostbyname  # Socket host version

# Version of this program
version = "0.0.013x1"
locked = False

# Getting hostname
def hostname():
    return gethostname()
# Getting ip configuration
def ifconfig():
    return gethostbyname(hostname())
# Realize test suite in program
def test_suit(host="192.168.1.1", body=sg, stream=80, suit=None):
    t_host = [hostname(), host]
    return t_host, body, stream, suit

# Installer packages module
class Package:
    def __init__(self, package="", mirror="https://github.com/TenayaOS/"):  # Manager config
        self.package = package
        if package == "":
            print("Insert package name to download!")
        else:
            self.download()
            self.MoveToLOCAL()
    def download(self, mirror="https://github.com/TenayaOS/"):
        mirror_setup = mirror, self.package
        system(f"git clone {mirror_setup}")

    def MoveToLOCAL(self):
        system(f"move {self.package} local")
# Shell
class Main:
    # Create window module Layout Widgets
    def __init__(self):
        sg.theme("Reddit")  # Setting theme of window
        layout = [
            [sg.Text("Script", size=(10,1)), sg.Input(key='script', size=(22,1))],  # Script input widget
            [sg.Button('Execute', size=(30,2))],  # Execute button widget
            [sg.Checkbox('Sudo'), sg.Checkbox('Hosted'), sg.Checkbox('Command')],  # Checkbox permission widget
            [sg.Text("Output:", size=(10,1))],  # Text widget
            [sg.Output(size=(32, 6))],  # Output widget
        ]
        self.windows =sg.Window("Tardis Executer", layout)  # Mount window shell
    def Iniciar(self):  # Reader and executer module
        while True:
            try:
                eventos, valores = self.windows.read()
                # Ram memory iExecuter
                if eventos == sg.WINDOW_CLOSED:
                    del eventos, valores
                    break

                # Execute commands
                elif eventos == 'Execute':
                    cmd = valores['script']  # Get script typed
                    # Close shell window
                    if cmd == "exit":
                        print("Exiting of Tardis Executer. . ."), time.sleep(4)
                        break
                    # Relese version
                    elif cmd == "version":
                        print(version)
                        print("This is a pre-realease of this version and being updating continualy, this version s very big and was divided in ")
                        print("seven part that be disponibilized in everyday of next week!")
                        print("https://github.com/TenayaOS/Tenaya")
                        continue
                    # Print a menssage in console
                    elif cmd.startswith("echo"):
                        cmd = cmd.replace("echo ", "")
                        cmd = cmd.replace("echo", "")
                        cmd = cmd.replace("%goto%", "\n")
                        cmd = cmd.replace("%window", '"Tardis Executer')
                        cmd = cmd.replace("%mirror%", "https://github.com/TenayaOS/Tenaya")
                        cmd = cmd.replace("%appdata%", "https://github.com/TenayaOS/Tenaya/tree/main/bin")
                        print(cmd)
                    # Install pack
                    elif cmd.startswith("install"):
                        cmd.replace("install ", "")
                        cmd.replace("install", "")
                        Package(package=cmd)
                    # Print readed host
                    elif cmd == "hostname":
                        print(f"Hostname of this Machine: {hostname()}")
                        continue
                      # Print readed host configured
                    elif cmd == "ifconfig":
                        print(f"{ifconfig()} ({hostname()})")
                        continue
                    # Set local variable
                    elif cmd.startswith("set"):
                        cmd = cmd.replace("set ", "")
                        cmd = cmd.replace("set", "")
                        cmd = cmd.replace("%goto%", "\n")
                        cmd = cmd.replace("%window", '"Tardis Executer')
                        cmd = cmd.replace("%mirror%", "https://github.com/TenayaOS/Tenaya")
                        cmd = cmd.replace("%appdata%", "https://github.com/TenayaOS/Tenaya/tree/main/bin")
                        shalala = cmd
                        print("Value was uploaded")
                    # Print local variable seted
                    elif cmd == "anchor":
                        try:
                            print(shalala)
                        except:
                            print("Dont have a loaded string")
                    # Delete value loaded
                    elif cmd == "unset":
                        del shalala
                        print('Deleted')
                    # Realize test suit
                    elif cmd == "hidden":
                        print(test_suit())
                        continue
                    # If value is ""
                    elif cmd == "":
                        print()
                        pass
                    # If command is invalid
                    else:
                        print(f"Tardis cannot execute: {cmd}")
                elif locked == True:
                    print("The shell been locked\nThe shell cannot be execute because dont have a bash")
            except KeyboardInterrupt:
                if locked == False:
                    print("/bin/shell: Your shell was locked")
                    locked = True
                if locked == True:
                    print("/bin/shell: Your shell was unlocked")
                    locked = False
if __name__ == "__main__":
    janela = Main()
    janela.Iniciar() # Execute Program gui
