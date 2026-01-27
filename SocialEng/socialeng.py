#!/usr/bin/env python3

import os
import sys
import time

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))

from modules.email_harvester import harvest_emails
from modules.phone_validator import validate_phone
from modules.username_generator import generate_usernames
from modules.target_profiler import profile_target
from modules.social_enum import enumerate_social

BANNER = f"""{CYAN}
███████╗ ██████╗  ██████╗██╗ █████╗ ██╗     ███████╗███╗   ██╗ ██████╗
██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║     ██╔════╝████╗  ██║██╔════╝
███████╗██║   ██║██║     ██║███████║██║     █████╗  ██╔██╗ ██║██║  ███╗
╚════██║██║   ██║██║     ██║██╔══██║██║     ██╔══╝  ██║╚██╗██║██║   ██║
███████║╚██████╔╝╚██████╗██║██║  ██║███████╗███████╗██║ ╚████║╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝{RESET}
{YELLOW}═══════════════════════════════════════════════════════════════════{RESET}
{GREEN}          Social Engineering Framework - OSINT & Intelligence{RESET}
{MAGENTA}                  Developed by b1l4l-sec | v2.0{RESET}
{YELLOW}═══════════════════════════════════════════════════════════════════{RESET}
"""

def clear():
    os.system('clear')

def print_menu():
    print(f"""
{BOLD}{CYAN}┌───────────────────────────────────────────────────────────────┐
│                    SOCIAL ENGINEERING TOOLKIT                 │
└───────────────────────────────────────────────────────────────┘{RESET}

  {GREEN}[1]{RESET} {BOLD}Email Harvesting{RESET}
      └─ Extract emails from domains and websites

  {GREEN}[2]{RESET} {BOLD}Phone Number Validation{RESET}
      └─ Validate and format phone numbers

  {GREEN}[3]{RESET} {BOLD}Username Generation{RESET}
      └─ Generate potential usernames from names

  {GREEN}[4]{RESET} {BOLD}Target Profiling{RESET}
      └─ Aggregate intelligence and create profiles

  {GREEN}[5]{RESET} {BOLD}Social Media Enumeration{RESET}
      └─ Check username availability across platforms

  {RED}[0]{RESET} {BOLD}Back to Main Menu{RESET}

{YELLOW}═══════════════════════════════════════════════════════════════════{RESET}
{RED}{BOLD}WARNING:{RESET} {YELLOW}Authorized use only. Obtain proper permissions.{RESET}
""")

def main():
    while True:
        clear()
        print(BANNER)
        print_menu()

        try:
            choice = input(f"\n{BOLD}{CYAN}SocialEng{RESET} > ").strip()

            if choice == '1':
                harvest_emails()
            elif choice == '2':
                validate_phone()
            elif choice == '3':
                generate_usernames()
            elif choice == '4':
                profile_target()
            elif choice == '5':
                enumerate_social()
            elif choice == '0':
                print(f"\n{GREEN}Returning to main menu...{RESET}")
                time.sleep(1)
                return
            else:
                print(f"{RED}Invalid option. Please select 0-5.{RESET}")
                time.sleep(1)

        except KeyboardInterrupt:
            print(f"\n{YELLOW}Returning to main menu...{RESET}")
            time.sleep(1)
            return
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")
            time.sleep(2)

if __name__ == '__main__':
    main()
