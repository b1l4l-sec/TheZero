import socket
import sys
import threading
from datetime import datetime
import os
from logo import display_logo2
import time

LIGHT_CYAN_BOLD = "\033[1;36m"  # Bold light cyan
BOLD_RED = "\033[1;31m"  # Bold red
BOLD_ORANGE = "\033[1;33m"  # Bold yellow (close to orange)
BOLD_GREEN = "\033[1;32m"  # Bold green
BOLD_YELLOW = "\033[1;33m"  # Bold yellow
RESET = "\033[0m"  # Reset styling

# Function to scan a port
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))  # 0 means open
        if result == 0:
            print(f"{BOLD_ORANGE}Port {port} is open{RESET}")
        s.close()
    except socket.error as e:
        pass
    except Exception as e:
        print(f"{BOLD_RED}Unexpected error on port {port}: {e}{RESET}")


#Main function - argument validation and target definition
def scan_target(target):

    # Resolve the target hostname to an IP address
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"{BOLD_RED}Error: Unable to resolve hostname {target}{RESET}")
        return

    # Add a pretty banner
    print("-" * 50)
    print(f"{BOLD_YELLOW}Scanning target {target_ip}")
    print(f"Time started: {datetime.now()}{RESET}")
    print("-" * 50)

    try:
        # Use multithreading to scan ports concurrently
        threads = []
        for port in range(1,65536):
            thread = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print(f"\n{BOLD_RED}Scan interrupted{RESET}")
        return

    except socket.error as e:
        print(f"{BOLD_RED}Socket error: {e}{RESET}")
        return

    print(f"\n{BOLD_GREEN}Scan completed!{RESET}")
    

def scan():
    os.system("clear")
    display_logo2()

    while True :
          target = input(f"\n\n{LIGHT_CYAN_BOLD}Enter target IP or hostname (or 'back' to return):{RESET} ").strip()
          if target.lower() in ['exit', 'back', 'return'] :
              print(f"\n{BOLD_GREEN}Returning to main menu...{RESET}")
              time.sleep(1)
              return
          scan_target(target)
 
