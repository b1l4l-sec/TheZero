import os
import re
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

def extract_emails_from_text(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return list(set(emails))

def harvest_from_website(url):
    try:
        print(f"{CYAN}[*] Fetching content from {url}...{RESET}")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text_content = soup.get_text()

            emails = extract_emails_from_text(text_content)

            if emails:
                print(f"{GREEN}[+] Found {len(emails)} email(s):{RESET}")
                for email in sorted(emails):
                    print(f"    {YELLOW}├─{RESET} {email}")
                return emails
            else:
                print(f"{YELLOW}[!] No emails found on this page{RESET}")
                return []
        else:
            print(f"{RED}[-] Failed to fetch URL (Status: {response.status_code}){RESET}")
            return []

    except requests.exceptions.Timeout:
        print(f"{RED}[-] Request timed out{RESET}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"{RED}[-] Error: {e}{RESET}")
        return []

def save_results(emails, target):
    if not emails:
        return

    targets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'targets')
    os.makedirs(targets_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename_json = os.path.join(targets_dir, f'emails_{target}_{timestamp}.json')
    filename_txt = os.path.join(targets_dir, f'emails_{target}_{timestamp}.txt')

    data = {
        'target': target,
        'timestamp': datetime.now().isoformat(),
        'emails_found': len(emails),
        'emails': sorted(emails)
    }

    with open(filename_json, 'w') as f:
        json.dump(data, f, indent=4)

    with open(filename_txt, 'w') as f:
        f.write(f"Email Harvesting Results\n")
        f.write(f"Target: {target}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total: {len(emails)} emails\n")
        f.write("="*50 + "\n\n")
        for email in sorted(emails):
            f.write(f"{email}\n")

    print(f"\n{GREEN}[+] Results saved:{RESET}")
    print(f"    {CYAN}├─ JSON:{RESET} {filename_json}")
    print(f"    {CYAN}└─ TXT:{RESET}  {filename_txt}")

def harvest_emails():
    os.system('clear')
    print(f"""
{BOLD}{GREEN}EMAIL HARVESTER{RESET}
{CYAN}═══════════════════════════════════════════════════════════════════{RESET}

{YELLOW}Extract email addresses from websites and domains{RESET}
{RED}Note: Only use on authorized targets{RESET}

""")

    target_url = input(f"{BOLD}Enter target URL (e.g., https://example.com):{RESET} ").strip()

    if not target_url:
        print(f"{RED}[-] No URL provided{RESET}")
        input(f"\n{BOLD}Press Enter to continue...{RESET}")
        return

    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url

    print(f"\n{CYAN}{'='*67}{RESET}")
    emails = harvest_from_website(target_url)

    if emails:
        domain = target_url.replace('https://', '').replace('http://', '').split('/')[0]
        save_results(emails, domain.replace('.', '_'))

    print(f"{CYAN}{'='*67}{RESET}")
    input(f"\n{BOLD}Press Enter to continue...{RESET}")
