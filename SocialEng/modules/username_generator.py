import os
import json
from datetime import datetime

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

def generate_username_variations(first_name, last_name, birth_year=None):
    first = first_name.lower()
    last = last_name.lower()

    usernames = []

    usernames.append(first + last)
    usernames.append(last + first)
    usernames.append(first + "." + last)
    usernames.append(last + "." + first)
    usernames.append(first + "_" + last)
    usernames.append(last + "_" + first)
    usernames.append(first[0] + last)
    usernames.append(first + last[0])
    usernames.append(first[0] + "." + last)
    usernames.append(first + "." + last[0])

    if len(first) > 0:
        usernames.append(first)
    if len(last) > 0:
        usernames.append(last)

    if birth_year:
        year_str = str(birth_year)
        year_short = year_str[-2:]

        usernames.append(first + year_str)
        usernames.append(first + year_short)
        usernames.append(last + year_str)
        usernames.append(last + year_short)
        usernames.append(first + last + year_str)
        usernames.append(first + last + year_short)
        usernames.append(first + "." + last + year_str)
        usernames.append(first + "_" + last + year_str)
        usernames.append(first[0] + last + year_str)

    common_numbers = ['1', '123', '01', '99', '21', '007']
    for num in common_numbers:
        usernames.append(first + num)
        usernames.append(first + last + num)

    return list(set(usernames))

def save_usernames(usernames, name):
    targets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'targets')
    os.makedirs(targets_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename_json = os.path.join(targets_dir, f'usernames_{name}_{timestamp}.json')
    filename_txt = os.path.join(targets_dir, f'usernames_{name}_{timestamp}.txt')

    data = {
        'target': name,
        'timestamp': datetime.now().isoformat(),
        'total_usernames': len(usernames),
        'usernames': sorted(usernames)
    }

    with open(filename_json, 'w') as f:
        json.dump(data, f, indent=4)

    with open(filename_txt, 'w') as f:
        f.write(f"Username Generation Results\n")
        f.write(f"Target: {name}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total: {len(usernames)} variations\n")
        f.write("="*50 + "\n\n")
        for username in sorted(usernames):
            f.write(f"{username}\n")

    print(f"\n{GREEN}[+] Results saved:{RESET}")
    print(f"    {CYAN}├─ JSON:{RESET} {filename_json}")
    print(f"    {CYAN}└─ TXT:{RESET}  {filename_txt}")

def generate_usernames():
    os.system('clear')

    print(f"""
{BOLD}{GREEN}USERNAME GENERATOR{RESET}
{CYAN}═══════════════════════════════════════════════════════════════════{RESET}

{YELLOW}Generate potential username variations from personal information{RESET}
{RED}Use for authorized security testing only{RESET}

""")

    first_name = input(f"{BOLD}Enter first name:{RESET} ").strip()
    last_name = input(f"{BOLD}Enter last name:{RESET} ").strip()
    birth_year = input(f"{BOLD}Enter birth year (optional):{RESET} ").strip()

    if not first_name or not last_name:
        print(f"{RED}[-] First name and last name are required{RESET}")
        input(f"\n{BOLD}Press Enter to continue...{RESET}")
        return

    year = None
    if birth_year:
        try:
            year = int(birth_year)
        except ValueError:
            print(f"{YELLOW}[!] Invalid year, ignoring...{RESET}")

    print(f"\n{CYAN}{'='*67}{RESET}")
    print(f"{CYAN}[*] Generating username variations...{RESET}")

    usernames = generate_username_variations(first_name, last_name, year)

    print(f"\n{GREEN}[+] Generated {len(usernames)} username variations:{RESET}\n")

    for i, username in enumerate(sorted(usernames), 1):
        print(f"    {YELLOW}{i:3d}.{RESET} {username}")

    save_usernames(usernames, f"{first_name}_{last_name}")

    print(f"\n{CYAN}{'='*67}{RESET}")
    input(f"\n{BOLD}Press Enter to continue...{RESET}")
