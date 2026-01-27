import os
import json
from datetime import datetime

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

def collect_profile_data():
    print(f"{CYAN}[*] Collecting target information...{RESET}\n")

    profile = {}

    profile['full_name'] = input(f"  {BOLD}Full Name:{RESET} ").strip()
    profile['email'] = input(f"  {BOLD}Email Address:{RESET} ").strip()
    profile['phone'] = input(f"  {BOLD}Phone Number:{RESET} ").strip()
    profile['company'] = input(f"  {BOLD}Company/Organization:{RESET} ").strip()
    profile['job_title'] = input(f"  {BOLD}Job Title:{RESET} ").strip()
    profile['location'] = input(f"  {BOLD}Location:{RESET} ").strip()

    print(f"\n{YELLOW}Social Media Profiles (press Enter to skip):{RESET}")
    profile['social_media'] = {}
    profile['social_media']['linkedin'] = input(f"  {BOLD}LinkedIn:{RESET} ").strip()
    profile['social_media']['twitter'] = input(f"  {BOLD}Twitter/X:{RESET} ").strip()
    profile['social_media']['facebook'] = input(f"  {BOLD}Facebook:{RESET} ").strip()
    profile['social_media']['instagram'] = input(f"  {BOLD}Instagram:{RESET} ").strip()

    profile['additional_info'] = input(f"\n  {BOLD}Additional Notes:{RESET} ").strip()

    return profile

def display_profile(profile):
    print(f"\n{GREEN}[+] TARGET PROFILE SUMMARY:{RESET}")
    print(f"{CYAN}{'='*67}{RESET}")

    if profile.get('full_name'):
        print(f"  {BOLD}Name:{RESET}          {profile['full_name']}")
    if profile.get('email'):
        print(f"  {BOLD}Email:{RESET}         {profile['email']}")
    if profile.get('phone'):
        print(f"  {BOLD}Phone:{RESET}         {profile['phone']}")
    if profile.get('company'):
        print(f"  {BOLD}Company:{RESET}       {profile['company']}")
    if profile.get('job_title'):
        print(f"  {BOLD}Job Title:{RESET}     {profile['job_title']}")
    if profile.get('location'):
        print(f"  {BOLD}Location:{RESET}      {profile['location']}")

    social = profile.get('social_media', {})
    if any(social.values()):
        print(f"\n  {BOLD}Social Media:{RESET}")
        if social.get('linkedin'):
            print(f"    {CYAN}├─ LinkedIn:{RESET}  {social['linkedin']}")
        if social.get('twitter'):
            print(f"    {CYAN}├─ Twitter:{RESET}   {social['twitter']}")
        if social.get('facebook'):
            print(f"    {CYAN}├─ Facebook:{RESET}  {social['facebook']}")
        if social.get('instagram'):
            print(f"    {CYAN}└─ Instagram:{RESET} {social['instagram']}")

    if profile.get('additional_info'):
        print(f"\n  {BOLD}Notes:{RESET}         {profile['additional_info']}")

    print(f"{CYAN}{'='*67}{RESET}")

def save_profile(profile):
    targets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'targets')
    os.makedirs(targets_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    name_safe = profile.get('full_name', 'target').replace(' ', '_').lower()
    filename_json = os.path.join(targets_dir, f'profile_{name_safe}_{timestamp}.json')
    filename_txt = os.path.join(targets_dir, f'profile_{name_safe}_{timestamp}.txt')

    profile['timestamp'] = datetime.now().isoformat()
    profile['created_by'] = 'TheZero SocialEng v2.0'

    with open(filename_json, 'w') as f:
        json.dump(profile, f, indent=4)

    with open(filename_txt, 'w') as f:
        f.write("="*67 + "\n")
        f.write("TARGET PROFILE\n")
        f.write("="*67 + "\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write("PERSONAL INFORMATION\n")
        f.write("-"*67 + "\n")
        if profile.get('full_name'):
            f.write(f"Name:          {profile['full_name']}\n")
        if profile.get('email'):
            f.write(f"Email:         {profile['email']}\n")
        if profile.get('phone'):
            f.write(f"Phone:         {profile['phone']}\n")
        if profile.get('location'):
            f.write(f"Location:      {profile['location']}\n")

        f.write("\nPROFESSIONAL INFORMATION\n")
        f.write("-"*67 + "\n")
        if profile.get('company'):
            f.write(f"Company:       {profile['company']}\n")
        if profile.get('job_title'):
            f.write(f"Job Title:     {profile['job_title']}\n")

        social = profile.get('social_media', {})
        if any(social.values()):
            f.write("\nSOCIAL MEDIA PROFILES\n")
            f.write("-"*67 + "\n")
            if social.get('linkedin'):
                f.write(f"LinkedIn:      {social['linkedin']}\n")
            if social.get('twitter'):
                f.write(f"Twitter:       {social['twitter']}\n")
            if social.get('facebook'):
                f.write(f"Facebook:      {social['facebook']}\n")
            if social.get('instagram'):
                f.write(f"Instagram:     {social['instagram']}\n")

        if profile.get('additional_info'):
            f.write("\nADDITIONAL NOTES\n")
            f.write("-"*67 + "\n")
            f.write(f"{profile['additional_info']}\n")

        f.write("\n" + "="*67 + "\n")

    print(f"\n{GREEN}[+] Profile saved:{RESET}")
    print(f"    {CYAN}├─ JSON:{RESET} {filename_json}")
    print(f"    {CYAN}└─ TXT:{RESET}  {filename_txt}")

def profile_target():
    os.system('clear')

    print(f"""
{BOLD}{GREEN}TARGET PROFILER{RESET}
{CYAN}═══════════════════════════════════════════════════════════════════{RESET}

{YELLOW}Create comprehensive target profiles for security assessments{RESET}
{RED}Authorized use only - Obtain proper permissions{RESET}

""")

    profile = collect_profile_data()

    display_profile(profile)

    save = input(f"\n{BOLD}Save profile? (y/n):{RESET} ").strip().lower()
    if save == 'y':
        save_profile(profile)
        print(f"{GREEN}[+] Profile saved successfully{RESET}")

    input(f"\n{BOLD}Press Enter to continue...{RESET}")
