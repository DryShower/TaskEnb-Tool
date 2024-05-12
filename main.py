import os
from platform import system
from colorama import Fore
from time import sleep
import asyncio

# Global variables
VERSION = '1.0.3'
LANGUAGE = 'English'

# Windows registry commands
ENABLE_TASK_MANAGER_CMD = 'REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f'
DISABLE_TASK_MANAGER_CMD = 'REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f'

# Function to clear the screen
def clear_screen():
    os.system('cls')

# Function to print empty lines for spacing
def print_empty_lines(lines=1):
    for _ in range(lines):
        print("")

# Function to check if the program is running on Windows
async def check_platform():
    plat = system()
    if plat != 'Windows':
        print(' This program is written for Windows.')
        print_empty_lines()
        input("  Press Enter to exit.")
        exit()

# Function to display the main menu
def display_menu():
    clear_screen()
    os.system("color e")
    logo = """

    
            ████████  █████  ███████ ██   ██  ███    ███  █████  ███    ██  █████   ██████  ███████ ██████         
               ██    ██   ██ ██      ██  ██   ████  ████ ██   ██ ████   ██ ██   ██ ██       ██      ██   ██        
               ██    ███████ ███████ █████    ██ ████ ██ ███████ ██ ██  ██ ███████ ██   ███ █████   ██████         
               ██    ██   ██      ██ ██  ██   ██  ██  ██ ██   ██ ██  ██ ██ ██   ██ ██    ██ ██      ██   ██        
               ██    ██   ██ ███████ ██   ██  ██      ██ ██   ██ ██   ████ ██   ██  ██████  ███████ ██   ██        

    """
    print(logo)
    print(f"{Fore.LIGHTBLACK_EX: >98}Language: {LANGUAGE}")
    print(f"{Fore.LIGHTBLACK_EX: >98}Version: {VERSION}")
    print_empty_lines()
    print(Fore.CYAN + '   [0]  Exit.')
    print(Fore.CYAN + '   [1] Enable Task Manager.')
    print(Fore.CYAN + '   [2] Disable Task Manager.')
    print_empty_lines()

# Function to handle user input
def handle_input():
    req = input(Fore.YELLOW + "  Command:  ")
    print_empty_lines()
    if req == '1':
        os.system(ENABLE_TASK_MANAGER_CMD)
        exit()
    elif req == '2':
        os.system(DISABLE_TASK_MANAGER_CMD)
        exit()
    elif req == '0':
        exit()
    else:
        clear_screen()
        print_empty_lines(2)
        print(" There are only two options.\n  Try again.")
        print_empty_lines()
        sleep(1.1)
        return

# Main function
def main():
    asyncio.run(check_platform())
    display_menu()
    handle_input()

if __name__ == "__main__":
    main()
