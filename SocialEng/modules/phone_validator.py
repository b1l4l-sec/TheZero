import phonenumbers
from phonenumbers import geocoder, carrier, timezone

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

def validate_and_analyze(phone_number):
    try:
        parsed = phonenumbers.parse(phone_number, None)

        is_valid = phonenumbers.is_valid_number(parsed)
        is_possible = phonenumbers.is_possible_number(parsed)

        print(f"\n{GREEN}[+] Phone Number Analysis:{RESET}")
        print(f"    {CYAN}├─ Number:{RESET}          {phone_number}")
        print(f"    {CYAN}├─ Valid:{RESET}           {GREEN if is_valid else RED}{'Yes' if is_valid else 'No'}{RESET}")
        print(f"    {CYAN}├─ Possible:{RESET}        {GREEN if is_possible else RED}{'Yes' if is_possible else 'No'}{RESET}")

        if is_valid or is_possible:
            formatted_international = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            formatted_national = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
            formatted_e164 = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)

            print(f"    {CYAN}├─ International:{RESET}   {formatted_international}")
            print(f"    {CYAN}├─ National:{RESET}        {formatted_national}")
            print(f"    {CYAN}├─ E164 Format:{RESET}     {formatted_e164}")

            country = geocoder.description_for_number(parsed, 'en')
            if country:
                print(f"    {CYAN}├─ Country:{RESET}         {country}")

            carrier_name = carrier.name_for_number(parsed, 'en')
            if carrier_name:
                print(f"    {CYAN}├─ Carrier:{RESET}         {carrier_name}")

            timezones = timezone.time_zones_for_number(parsed)
            if timezones:
                print(f"    {CYAN}└─ Timezone(s):{RESET}     {', '.join(timezones)}")
        else:
            print(f"\n{RED}[-] Invalid phone number format{RESET}")

    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"\n{RED}[-] Error parsing number: {e}{RESET}")
        print(f"{YELLOW}[!] Format examples:{RESET}")
        print(f"    +1234567890")
        print(f"    +44 20 1234 5678")
        print(f"    +33 1 23 45 67 89")

def validate_phone():
    import os
    os.system('clear')

    print(f"""
{BOLD}{GREEN}PHONE NUMBER VALIDATOR{RESET}
{CYAN}═══════════════════════════════════════════════════════════════════{RESET}

{YELLOW}Validate and analyze international phone numbers{RESET}
{YELLOW}Include country code (e.g., +1, +44, +33){RESET}

""")

    phone = input(f"{BOLD}Enter phone number with country code:{RESET} ").strip()

    if not phone:
        print(f"{RED}[-] No phone number provided{RESET}")
        input(f"\n{BOLD}Press Enter to continue...{RESET}")
        return

    print(f"\n{CYAN}{'='*67}{RESET}")
    validate_and_analyze(phone)
    print(f"{CYAN}{'='*67}{RESET}")

    input(f"\n{BOLD}Press Enter to continue...{RESET}")
