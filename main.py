from platform import system
import os; os.system("color e"); os.system("title Task-Enb"); os.system("echo off")
from colorama import Fore, Style
from time import sleep

Enabling_code = 'REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f'
Disable_code = 'REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f'


def clear():
    os.system('cls')

def space():
    print("")



clear()

platform = system()
if platform == 'Windows':
    pass
else:
    print('This code is written for Windows.')
    input("Press Enter to exit.")
    exit()



logo = """


             ████████  █████  ███████ ██   ██  ███    ███  █████  ███    ██  █████   ██████  ███████ ██████  
                ██    ██   ██ ██      ██  ██   ████  ████ ██   ██ ████   ██ ██   ██ ██       ██      ██   ██ 
                ██    ███████ ███████ █████    ██ ████ ██ ███████ ██ ██  ██ ███████ ██   ███ █████   ██████  
                ██    ██   ██      ██ ██  ██   ██  ██  ██ ██   ██ ██  ██ ██ ██   ██ ██    ██ ██      ██   ██ 
                ██    ██   ██ ███████ ██   ██  ██      ██ ██   ██ ██   ████ ██   ██  ██████  ███████ ██   ██ 
                                                                                                           


"""




print(logo)

space()
print(Fore.CYAN + '  [0]  Exit.')
print(Fore.CYAN + '  [1] Enable Task Manager.')
print(Fore.CYAN + '  [2] Disable Task Manager.')
space()

Style.RESET_ALL
req = input(Fore.YELLOW + " Command:  ")

def ask():
    while True:
        if req == '1':
            os.system(Enabling_code)
            exit()
        elif req == '2':
            os.system(Disable_code)
            exit()
        elif req == '0':
            exit()
        else:
            clear()
            space()
            space()
            print(" There are only two options.\n  Try again.")
            space()
            sleep(2.2)
            exit()
ask()
