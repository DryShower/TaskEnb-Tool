import os
import asyncio
import requests
from platform import system
from colorama import Fore, init
import keyboard

# Initialize Colorama
init(autoreset=True)

# Global variables
VERSION = 'v1.2.7'
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
ENABLE_TASK_MANAGER_CMD = 'REG add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 0 /f'
DISABLE_TASK_MANAGER_CMD = 'REG add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f'

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
        print('This program is written for Windows.')
        print_empty_lines()
        input("Press Enter to exit.")
        exit()

def enable_taskmgr():
    os.system(ENABLE_TASK_MANAGER_CMD)
    print("Task Manager Enabled.")

def disable_taskmgr():
    os.system(DISABLE_TASK_MANAGER_CMD)
    print("Task Manager Disabled.")

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
    print(Fore.CYAN + '   [1]  Enable Task Manager.')
    print(Fore.CYAN + '   [2]  Disable Task Manager.')
    print_empty_lines()

# Function to handle key presses
def handle_key_presses():
    # Register hotkeys
    keyboard.add_hotkey('1', enable_taskmgr)
    keyboard.add_hotkey('2', disable_taskmgr)
      # Exit the program when '0' is pressed

    # Keep the program running and listening for key presses
    keyboard.wait('esc')  # Press 'esc' to exit the program

# Main function
def main():
    asyncio.run(check_platform())
    display_menu()
    handle_key_presses()

if __name__ == "__main__":
    main()
