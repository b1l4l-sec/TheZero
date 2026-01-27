#!/usr/bin/env python3

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.banner import (
    print_banner, print_menu, print_success,
    print_error, print_info, print_warning, Colors
)
from config.settings import SERVER_PORT, CAPTURES_DIR
from core.dependency_checker import check_and_install_dependencies, check_dependencies_status
from core.server import run_server
from core.ngrok_manager import start_ngrok_tunnel

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def launch_local_server():
    clear_screen()
    print_banner()

    try:
        webbrowser.open(f'http://localhost:{SERVER_PORT}')
    except:
        pass

    run_server()

def launch_ngrok_tunnel():
    clear_screen()
    print_banner()
    start_ngrok_tunnel()

def open_captures_directory():
    clear_screen()
    print_banner()

    print()
    print(f"{Colors.CYAN}{'='*64}{Colors.RESET}")
    print(f"{Colors.BOLD}  CAPTURES DIRECTORY{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*64}{Colors.RESET}")
    print()

    if not os.path.exists(CAPTURES_DIR):
        os.makedirs(CAPTURES_DIR, exist_ok=True)
        print_info(f"Created captures directory: {CAPTURES_DIR}")

    try:
        if sys.platform == 'darwin':
            subprocess.run(['open', CAPTURES_DIR])
        elif sys.platform == 'linux':
            subprocess.run(['xdg-open', CAPTURES_DIR])
        elif sys.platform == 'win32':
            subprocess.run(['explorer', CAPTURES_DIR])

        print_success(f"Opened: {CAPTURES_DIR}")
    except Exception as e:
        print_error(f"Failed to open directory: {str(e)}")
        print_info(f"Manual path: {CAPTURES_DIR}")

    print()
    print_info("Press Enter to return to main menu...")
    input()

def check_dependencies():
    clear_screen()
    print_banner()
    check_dependencies_status()

def main_menu():
    while True:
        clear_screen()
        print_banner()
        print_menu()

        try:
            choice = input(f"{Colors.BOLD}Select option:{Colors.RESET} ").strip()

            if choice == '1':
                launch_local_server()
            elif choice == '2':
                launch_ngrok_tunnel()
            elif choice == '3':
                open_captures_directory()
            elif choice == '4':
                check_dependencies()
            elif choice == '0':
                clear_screen()
                print_banner()
                print()
                print_success("Thank you for using SpecterVision!")
                print_info("All session data has been saved to the captures directory")
                print()
                sys.exit(0)
            else:
                print_warning("Invalid option. Please select 0-4.")
                import time
                time.sleep(1)

        except KeyboardInterrupt:
            print()
            print()
            print_info("Shutting down...")
            print_success("Goodbye!")
            print()
            sys.exit(0)
        except Exception as e:
            print_error(f"An error occurred: {str(e)}")
            import time
            time.sleep(2)

def main():
    clear_screen()
    print_banner()

    print()
    print_info("Initializing SpecterVision...")
    print_info("Checking dependencies...")
    print()

    check_and_install_dependencies(silent=True)

    print_success("System ready!")
    print()
    print_info("Press Enter to continue...")
    input()

    main_menu()

if __name__ == '__main__':
    main()
