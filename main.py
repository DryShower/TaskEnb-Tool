import os
from platform import system
import asyncio
from time import sleep
#Third Party
from colorama import Fore
import requests

# Global variables
VERSION = 'v1.0.4'
LANGUAGE = 'English'

# Function to check the latest version
async def try_to_check_version():
    try:
        response = requests.get("https://github.com/fairyfart/TaskEnb-Tool/releases/latest")
        latest_version = response.url.split("/").pop()
        return latest_version
    except requests.exceptions.ConnectionError:
        return None

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
    latest_version = asyncio.run(try_to_check_version())
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

    if latest_version:
        if latest_version != VERSION:
            print(f"{Fore.LIGHTBLACK_EX: >98}Latest: {Fore.RED}{latest_version}")
        else:
            print(f"{Fore.LIGHTBLACK_EX: >98}Latest: {latest_version}")
    else:
        print(f"{Fore.RED: >98}Latest: Unable to check.")
        print(f"{Fore.RED: >108} (No Wifi)")
        
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
