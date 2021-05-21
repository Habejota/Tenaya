import random, time
import PySimpleGUI as sg
from os import *
from socket import gethostname, gethostbyname

version = "0.0.2"

def hostname():
    return gethostname()
def ifconfig():
    return gethostbyname(hostname())
def test_suit(host="192.168.1.1", body=sg, stream=80, suit=None):
    t_host = [hostname(), host]
    return t_host, body, stream, suit

class Main:
    def __init__(self):
        sg.theme("Reddit")
        layout = [
            [sg.Text("Script", size=(10,1)), sg.Input(key='script', size=(22,1))],
            [sg.Button('Execute', size=(30,2))],
            [sg.Checkbox('Sudo'), sg.Checkbox('Hosted'), sg.Checkbox('Command')],
            [sg.Text("Output:", size=(10,1))],
            [sg.Output(size=(32, 6))],
        ]
        self.windows =sg.Window("Tardis Executer", layout)
    def Iniciar(self):
        while True:
            eventos, valores = self.windows.read()
            if eventos == sg.WINDOW_CLOSED:
                break
            elif eventos == 'Execute':
                cmd = valores['script']
                if cmd == "exit":
                    print("Exiting of Tardis Executer. . ."), sleep(4)
                    break
                elif cmd.startswith("echo"):
                    cmd = cmd.replace("echo ", "")
                    cmd = cmd.replace("echo", "")
                    print(cmd)
                elif cmd == "hostname":
                    print(f"Hostname of Machine: {hostname()}")
                    continue
                elif cmd == "ifconfig":
                    print(f"{ifconfig()} ({hostname()})")
                    continue
                elif cmd.startswith("set"):
                    cmd = cmd.replace("set ", "")
                    cmd = cmd.replace("set", "")
                    shalala = cmd
                    print("Value was uploaded")
                elif cmd == "anchor":
                    try:
                        print(shalala)
                    except:
                        print("Dont have a loaded string")
                elif cmd == "unset":
                    del shalala
                    print('Deleted')
                elif cmd == "shell":
                    print("O Shell foi iniciado. . .")
                    print("Shell basic builder Tardis Shell")

                    system("python shell.py")
                elif cmd == "hidden":
                    print(test_suit())
                elif cmd == "":
                    print()
                    pass
                else:
                    print(f"Tardis cannot execute: {cmd}")

janela = Main()
janela.Iniciar()