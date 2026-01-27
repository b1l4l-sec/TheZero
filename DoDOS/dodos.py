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

BANNER = f"""{CYAN}
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║         ██████╗  ██████╗ ██████╗  ██████╗ ███████╗        ║
║         ██╔══██╗██╔═══██╗██╔══██╗██╔═══██╗██╔════╝        ║
║         ██║  ██║██║   ██║██║  ██║██║   ██║███████╗        ║
║         ██║  ██║██║   ██║██║  ██║██║   ██║╚════██║        ║
║         ██████╔╝╚██████╔╝██████╔╝╚██████╔╝███████║        ║
║         ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝        ║
║                                                            ║
║           DoS Stress Testing Framework for CTF            ║
║              Network Load & Resilience Testing            ║
║                  Educational Use Only                     ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝{RESET}
{MAGENTA}Developer: b1l4l-sec | GitHub: https://github.com/b1l4l-sec{RESET}
"""

LEGAL_WARNING = f"""{RED}{BOLD}
╔════════════════════════════════════════════════════════════╗
║                  ⚠️  LEGAL WARNING ⚠️                       ║
╚════════════════════════════════════════════════════════════╝{RESET}

{YELLOW}This tool is designed EXCLUSIVELY for:{RESET}
  {GREEN}✓{RESET} Authorized penetration testing with written consent
  {GREEN}✓{RESET} CTF competitions and security challenges
  {GREEN}✓{RESET} Educational research in controlled environments
  {GREEN}✓{RESET} Network resilience testing on owned infrastructure

{RED}{BOLD}STRICTLY PROHIBITED:{RESET}
  {RED}✗{RESET} Unauthorized DoS/DDoS attacks on any system
  {RED}✗{RESET} Disrupting services without explicit authorization
  {RED}✗{RESET} Testing against third-party networks
  {RED}✗{RESET} Any illegal or malicious activity

{RED}{BOLD}CONSEQUENCES OF MISUSE:{RESET}
  {YELLOW}• Criminal prosecution under computer crime laws{RESET}
  {YELLOW}• Civil liability and financial damages{RESET}
  {YELLOW}• Imprisonment and heavy fines{RESET}
  {YELLOW}• Permanent criminal record{RESET}

{CYAN}By using this tool, you acknowledge that you have obtained
proper written authorization and accept full legal responsibility.{RESET}

{BOLD}The developer assumes NO liability for misuse of this tool.{RESET}
"""

def clear():
    os.system('clear')

def show_legal_warning():
    clear()
    print(BANNER)
    print(LEGAL_WARNING)
    print(f"\n{BOLD}{YELLOW}Do you have WRITTEN AUTHORIZATION to perform stress testing? (yes/no){RESET}")
    response = input(f"{CYAN}> {RESET}").strip().lower()

    if response not in ['yes', 'y']:
        print(f"\n{RED}Authorization required. Exiting...{RESET}\n")
        time.sleep(2)
        sys.exit(0)

    print(f"\n{GREEN}Proceeding with authorized testing...{RESET}")
    time.sleep(1)

def print_menu():
    print(f"""
{BOLD}{CYAN}┌────────────────────────────────────────────────────────┐
│                    DODOS MAIN MENU                     │
└────────────────────────────────────────────────────────┘{RESET}

  {GREEN}[1]{RESET} {BOLD}TCP Flood Attack{RESET}
      └─ SYN flood with configurable parameters

  {GREEN}[2]{RESET} {BOLD}UDP Flood Attack{RESET}
      └─ UDP packet flooding

  {GREEN}[3]{RESET} {BOLD}HTTP Request Flood{RESET}
      └─ Application layer stress testing

  {GREEN}[4]{RESET} {BOLD}Configuration Settings{RESET}
      └─ Adjust threads, timeout, packet size

  {YELLOW}[5]{RESET} {BOLD}View Legal Warning{RESET}
      └─ Review authorization requirements

  {RED}[0]{RESET} {BOLD}Back to Main Menu{RESET}

{CYAN}═══════════════════════════════════════════════════════════{RESET}
""")

def launch_tcp_flood():
    from modules.dos_tester import TCPFlooder

    clear()
    print(BANNER)
    print(f"{BOLD}{CYAN}TCP FLOOD ATTACK CONFIGURATION{RESET}\n")

    target = input(f"{CYAN}Enter target IP address: {RESET}").strip()
    if not target:
        print(f"{RED}Error: Target IP required{RESET}")
        time.sleep(2)
        return

    port_input = input(f"{CYAN}Enter target port (default 80): {RESET}").strip()
    port = int(port_input) if port_input else 80

    threads_input = input(f"{CYAN}Enter number of threads (default 10): {RESET}").strip()
    threads = int(threads_input) if threads_input else 10

    duration_input = input(f"{CYAN}Enter duration in seconds (default 60): {RESET}").strip()
    duration = int(duration_input) if duration_input else 60

    print(f"\n{YELLOW}Configuration:{RESET}")
    print(f"  Target: {GREEN}{target}:{port}{RESET}")
    print(f"  Threads: {GREEN}{threads}{RESET}")
    print(f"  Duration: {GREEN}{duration} seconds{RESET}")

    confirm = input(f"\n{BOLD}{YELLOW}Start attack? (yes/no): {RESET}").strip().lower()
    if confirm not in ['yes', 'y']:
        print(f"{YELLOW}Attack cancelled{RESET}")
        time.sleep(1)
        return

    flooder = TCPFlooder(target, port, threads, duration)
    flooder.start()

    input(f"\n{CYAN}Press Enter to continue...{RESET}")

def launch_udp_flood():
    from modules.dos_tester import UDPFlooder

    clear()
    print(BANNER)
    print(f"{BOLD}{CYAN}UDP FLOOD ATTACK CONFIGURATION{RESET}\n")

    target = input(f"{CYAN}Enter target IP address: {RESET}").strip()
    if not target:
        print(f"{RED}Error: Target IP required{RESET}")
        time.sleep(2)
        return

    port_input = input(f"{CYAN}Enter target port (default 53): {RESET}").strip()
    port = int(port_input) if port_input else 53

    packet_size_input = input(f"{CYAN}Enter packet size in bytes (default 1024): {RESET}").strip()
    packet_size = int(packet_size_input) if packet_size_input else 1024

    threads_input = input(f"{CYAN}Enter number of threads (default 10): {RESET}").strip()
    threads = int(threads_input) if threads_input else 10

    duration_input = input(f"{CYAN}Enter duration in seconds (default 60): {RESET}").strip()
    duration = int(duration_input) if duration_input else 60

    print(f"\n{YELLOW}Configuration:{RESET}")
    print(f"  Target: {GREEN}{target}:{port}{RESET}")
    print(f"  Packet Size: {GREEN}{packet_size} bytes{RESET}")
    print(f"  Threads: {GREEN}{threads}{RESET}")
    print(f"  Duration: {GREEN}{duration} seconds{RESET}")

    confirm = input(f"\n{BOLD}{YELLOW}Start attack? (yes/no): {RESET}").strip().lower()
    if confirm not in ['yes', 'y']:
        print(f"{YELLOW}Attack cancelled{RESET}")
        time.sleep(1)
        return

    flooder = UDPFlooder(target, port, threads, duration, packet_size)
    flooder.start()

    input(f"\n{CYAN}Press Enter to continue...{RESET}")

def launch_http_flood():
    from modules.dos_tester import HTTPFlooder

    clear()
    print(BANNER)
    print(f"{BOLD}{CYAN}HTTP REQUEST FLOOD CONFIGURATION{RESET}\n")

    target = input(f"{CYAN}Enter target URL (e.g., http://target.com): {RESET}").strip()
    if not target:
        print(f"{RED}Error: Target URL required{RESET}")
        time.sleep(2)
        return

    if not target.startswith(('http://', 'https://')):
        target = 'http://' + target

    threads_input = input(f"{CYAN}Enter number of threads (default 20): {RESET}").strip()
    threads = int(threads_input) if threads_input else 20

    duration_input = input(f"{CYAN}Enter duration in seconds (default 60): {RESET}").strip()
    duration = int(duration_input) if duration_input else 60

    print(f"\n{YELLOW}Configuration:{RESET}")
    print(f"  Target: {GREEN}{target}{RESET}")
    print(f"  Threads: {GREEN}{threads}{RESET}")
    print(f"  Duration: {GREEN}{duration} seconds{RESET}")

    confirm = input(f"\n{BOLD}{YELLOW}Start attack? (yes/no): {RESET}").strip().lower()
    if confirm not in ['yes', 'y']:
        print(f"{YELLOW}Attack cancelled{RESET}")
        time.sleep(1)
        return

    flooder = HTTPFlooder(target, threads, duration)
    flooder.start()

    input(f"\n{CYAN}Press Enter to continue...{RESET}")

def show_config():
    clear()
    print(BANNER)
    print(f"""
{BOLD}{CYAN}CONFIGURATION GUIDELINES{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}

{BOLD}{YELLOW}Thread Configuration:{RESET}
  {GREEN}Low Impact:{RESET}     1-10 threads
  {YELLOW}Medium Impact:{RESET}  11-50 threads
  {RED}High Impact:{RESET}    51-200 threads

{BOLD}{YELLOW}Packet Size (UDP):{RESET}
  {GREEN}Small:{RESET}   64-512 bytes
  {YELLOW}Medium:{RESET}  513-2048 bytes
  {RED}Large:{RESET}   2049-65507 bytes

{BOLD}{YELLOW}Duration Recommendations:{RESET}
  {GREEN}Quick Test:{RESET}    10-30 seconds
  {YELLOW}Standard Test:{RESET} 31-120 seconds
  {RED}Stress Test:{RESET}   121+ seconds

{BOLD}{YELLOW}Timeout Settings:{RESET}
  Default socket timeout: 5 seconds
  HTTP request timeout: 10 seconds

{CYAN}═══════════════════════════════════════════════════════════{RESET}
{YELLOW}Note: Higher values consume more system resources{RESET}
""")
    input(f"\n{BOLD}Press Enter to continue...{RESET}")

def main():
    show_legal_warning()

    while True:
        clear()
        print(BANNER)
        print_menu()

        try:
            choice = input(f"{BOLD}{CYAN}DoDOS{RESET} > ").strip()

            if choice == '1':
                launch_tcp_flood()
            elif choice == '2':
                launch_udp_flood()
            elif choice == '3':
                launch_http_flood()
            elif choice == '4':
                show_config()
            elif choice == '5':
                clear()
                print(BANNER)
                print(LEGAL_WARNING)
                input(f"\n{BOLD}Press Enter to continue...{RESET}")
            elif choice == '0':
                clear()
                print(f"{YELLOW}Exiting DoDOS...{RESET}\n")
                break
            else:
                print(f"{RED}Invalid option. Please select 0-5.{RESET}")
                time.sleep(1)

        except KeyboardInterrupt:
            print(f"\n{YELLOW}Interrupted by user{RESET}\n")
            break
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")
            time.sleep(2)

if __name__ == '__main__':
    main()
