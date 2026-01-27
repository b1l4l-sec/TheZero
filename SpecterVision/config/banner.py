class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

BANNER = r"""
 _______                     __              ___ ___ _     _
|   _   .-----.-----.----.--|  |.-----.----.|   |   |_|___|_| .-----.----.
|   1___|  _  |  -__|  __|  _  ||  -__|   _| \     /| |   | | |  _  |     |
|____   |   __|_____|____|_____||_____|__|    \___/ |_|_|_|_| |_____|__|__|
|_______|__|   [ v1.0.0-Beta | Biometric Security Research ]
"""

MENU = """
{cyan}╔══════════════════════════════════════════════════════════════╗
║                      MAIN CONTROL PANEL                      ║
╚══════════════════════════════════════════════════════════════╝{reset}

  {bold}[1]{reset} Launch Local Server (Port 5000)
  {bold}[2]{reset} Start ngrok Tunnel (Global Access)
  {bold}[3]{reset} Open Captures Directory
  {bold}[4]{reset} Check System Dependencies
  {bold}[0]{reset} Exit

{cyan}╚══════════════════════════════════════════════════════════════╝{reset}
"""

def print_banner():
    print(Colors.GREEN + BANNER + Colors.RESET)

def print_menu():
    print(MENU.format(
        cyan=Colors.CYAN,
        reset=Colors.RESET,
        bold=Colors.BOLD
    ))

def print_success(message):
    print(f"{Colors.GREEN}[✓]{Colors.RESET} {message}")

def print_error(message):
    print(f"{Colors.RED}[✗]{Colors.RESET} {message}")

def print_info(message):
    print(f"{Colors.CYAN}[i]{Colors.RESET} {message}")

def print_warning(message):
    print(f"{Colors.YELLOW}[!]{Colors.RESET} {message}")
