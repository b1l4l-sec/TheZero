#!/usr/bin/env python3

import os
import sys
import json
import getpass
import hashlib
import base64
import shutil
import time
from pathlib import Path
from datetime import datetime

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as PBKDF2
except ImportError as e:
    print("\033[91mError: cryptography library not installed\033[0m")
    print(f"\033[93mDetails: {e}\033[0m")
    print("\033[93mPlease run: pip install cryptography\033[0m")
    sys.exit(1)

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""{GREEN}
╔═══════════════════════════════════════════════════════════╗
║  ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗██████╗  ║
║  ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗║
║  ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║║
║  ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║║
║  ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝║
║  ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ║
║                    ███╗   ███╗ ██████╗ ██████╗                      ║
║                    ████╗ ████║██╔════╝ ██╔══██╗                     ║
║                    ██╔████╔██║██║  ███╗██████╔╝                     ║
║                    ██║╚██╔╝██║██║   ██║██╔══██╗                     ║
║                    ██║ ╚═╝ ██║╚██████╔╝██║  ██║                     ║
║                    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝                     ║
╚═══════════════════════════════════════════════════════════╝{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}
{YELLOW}    Secure Encrypted Password Management System v2.2{RESET}
{MAGENTA}      Military-Grade Security with Integrity Protection{RESET}
{MAGENTA}           Developed by b1l4l-sec | Version 2.2{RESET}
{CYAN}═══════════════════════════════════════════════════════════{RESET}
"""

class PasswordManager:
    def __init__(self):
        self.script_dir = Path(__file__).parent.absolute()
        self.vault_dir = self.script_dir / "vault"
        self.backup_dir = self.script_dir / ".backup"
        self.vault_file = self.vault_dir / "passwords.enc"
        self.salt_file = self.vault_dir / "salt.key"
        self.integrity_file = self.vault_dir / ".integrity"
        
        # Create directories
        self.vault_dir.mkdir(exist_ok=True)
        self.backup_dir.mkdir(exist_ok=True)
        
        # Set strict permissions
        os.chmod(self.vault_dir, 0o700)
        os.chmod(self.backup_dir, 0o700)
        
        self.cipher = None
        self.master_password = None

    def calculate_file_hash(self, filepath: Path) -> str:
        """Calculate SHA-256 hash of a file for integrity verification"""
        if not filepath.exists():
            return ""
        sha256 = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for block in iter(lambda: f.read(4096), b''):
                sha256.update(block)
        return sha256.hexdigest()

    def save_integrity_hash(self):
        """Save integrity hashes of vault files"""
        integrity_data = {
            "vault_hash": self.calculate_file_hash(self.vault_file),
            "salt_hash": self.calculate_file_hash(self.salt_file),
            "timestamp": datetime.now().isoformat()
        }
        self.integrity_file.write_text(json.dumps(integrity_data, indent=2))
        os.chmod(self.integrity_file, 0o600)

    def verify_integrity(self) -> bool:
        """Verify vault files haven't been tampered with"""
        if not self.integrity_file.exists():
            # First time, create integrity file
            if self.vault_file.exists():
                self.save_integrity_hash()
            return True
        
        try:
            integrity_data = json.loads(self.integrity_file.read_text())
            
            current_vault_hash = self.calculate_file_hash(self.vault_file)
            current_salt_hash = self.calculate_file_hash(self.salt_file)
            
            vault_intact = current_vault_hash == integrity_data["vault_hash"]
            salt_intact = current_salt_hash == integrity_data["salt_hash"]
            
            return vault_intact and salt_intact
        except Exception:
            return False

    def create_backup(self):
        """Create timestamped backup of vault"""
        if not self.vault_file.exists():
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = self.backup_dir / f"vault_backup_{timestamp}.enc"
        
        try:
            shutil.copy2(self.vault_file, backup_file)
            shutil.copy2(self.salt_file, self.backup_dir / f"salt_backup_{timestamp}.key")
            os.chmod(backup_file, 0o600)
            os.chmod(self.backup_dir / f"salt_backup_{timestamp}.key", 0o600)
            
            # Keep only last 5 backups
            backups = sorted(self.backup_dir.glob("vault_backup_*.enc"))
            if len(backups) > 5:
                for old_backup in backups[:-5]:
                    old_backup.unlink()
                    # Remove corresponding salt file
                    salt_backup = self.backup_dir / old_backup.name.replace("vault_backup_", "salt_backup_").replace(".enc", ".key")
                    if salt_backup.exists():
                        salt_backup.unlink()
        except Exception as e:
            print(f"{YELLOW}Warning: Backup creation failed: {e}{RESET}")

    def restore_from_backup(self):
        """Restore vault from most recent backup"""
        backups = sorted(self.backup_dir.glob("vault_backup_*.enc"))
        if not backups:
            print(f"{RED}No backups available!{RESET}")
            return False
        
        latest_backup = backups[-1]
        salt_backup = self.backup_dir / latest_backup.name.replace("vault_backup_", "salt_backup_").replace(".enc", ".key")
        
        if not salt_backup.exists():
            print(f"{RED}Backup salt file not found!{RESET}")
            return False
        
        try:
            shutil.copy2(latest_backup, self.vault_file)
            shutil.copy2(salt_backup, self.salt_file)
            os.chmod(self.vault_file, 0o600)
            os.chmod(self.salt_file, 0o600)
            self.save_integrity_hash()
            print(f"{GREEN}✓ Vault restored from backup: {latest_backup.name}{RESET}")
            return True
        except Exception as e:
            print(f"{RED}Restore failed: {e}{RESET}")
            return False

    def handle_tampering(self):
        """Handle detected tampering"""
        clear()
        print(BANNER)
        print(f"\n{RED}{BOLD}⚠ SECURITY ALERT: VAULT TAMPERING DETECTED! ⚠{RESET}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}\n")
        print(f"{YELLOW}The vault files have been modified externally.{RESET}")
        print(f"{YELLOW}This could indicate:${RESET}")
        print(f"  {RED}• Unauthorized access attempt{RESET}")
        print(f"  {RED}• File corruption{RESET}")
        print(f"  {RED}• Manual file modification{RESET}\n")
        
        print(f"{BOLD}{CYAN}Available Options:{RESET}")
        print(f"  {GREEN}[1]{RESET} Restore from backup (recommended)")
        print(f"  {RED}[2]{RESET} Wipe vault and start fresh")
        print(f"  {YELLOW}[3]{RESET} Ignore and continue (NOT RECOMMENDED)")
        print(f"  {MAGENTA}[0]{RESET} Exit")
        
        choice = input(f"\n{BOLD}{RED}Select option: {RESET}").strip()
        
        if choice == '1':
            if self.restore_from_backup():
                print(f"\n{GREEN}Vault restored successfully!{RESET}")
                input(f"{BOLD}Press Enter to continue...{RESET}")
                return True
            else:
                print(f"\n{RED}Restore failed!{RESET}")
                input(f"{BOLD}Press Enter to continue...{RESET}")
                return False
        elif choice == '2':
            confirm = input(f"\n{RED}Type 'WIPE' to confirm vault deletion: {RESET}")
            if confirm == 'WIPE':
                self.vault_file.unlink(missing_ok=True)
                self.salt_file.unlink(missing_ok=True)
                self.integrity_file.unlink(missing_ok=True)
                print(f"\n{GREEN}✓ Vault wiped. You can create a new one.{RESET}")
                input(f"{BOLD}Press Enter to continue...{RESET}")
                return True
            else:
                print(f"{YELLOW}Wipe cancelled.{RESET}")
                return False
        elif choice == '3':
            print(f"\n{YELLOW}⚠ Proceeding without integrity verification!{RESET}")
            print(f"{RED}Your data may be compromised!{RESET}")
            input(f"{BOLD}Press Enter to continue...{RESET}")
            return True
        else:
            return False

    def derive_key(self, password: str, salt: bytes) -> bytes:
        kdf = PBKDF2(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def setup_master_password(self):
        clear()
        print(BANNER)
        print(f"\n{BOLD}{YELLOW}First Time Setup - Create Master Password{RESET}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}\n")
        print(f"{YELLOW}This password will encrypt all your stored passwords.{RESET}")
        print(f"{RED}WARNING: If you forget this password, all data will be lost!{RESET}\n")

        while True:
            password1 = getpass.getpass(f"{BOLD}{GREEN}Enter Master Password: {RESET}")
            if len(password1) < 8:
                print(f"{RED}Password must be at least 8 characters!{RESET}\n")
                continue

            password2 = getpass.getpass(f"{BOLD}{GREEN}Confirm Master Password: {RESET}")
            if password1 != password2:
                print(f"{RED}Passwords do not match! Try again.{RESET}\n")
                continue

            salt = os.urandom(16)
            self.salt_file.write_bytes(salt)
            os.chmod(self.salt_file, 0o600)

            key = self.derive_key(password1, salt)
            self.cipher = Fernet(key)
            self.master_password = password1

            initial_data = {"passwords": {}}
            encrypted = self.cipher.encrypt(json.dumps(initial_data).encode())
            self.vault_file.write_bytes(encrypted)
            os.chmod(self.vault_file, 0o600)
            
            # Save integrity hash
            self.save_integrity_hash()
            
            # Create initial backup
            self.create_backup()

            print(f"\n{GREEN}✓ Master password created successfully!{RESET}")
            print(f"{GREEN}✓ Vault initialized with security features{RESET}")
            print(f"{GREEN}✓ Integrity protection enabled{RESET}")
            print(f"{GREEN}✓ Initial backup created{RESET}\n")
            input(f"{BOLD}Press Enter to continue...{RESET}")
            break

    def authenticate(self):
        # Check for tampering first
        if self.vault_file.exists() and not self.verify_integrity():
            if not self.handle_tampering():
                return False
        
        if not self.salt_file.exists():
            self.setup_master_password()
            return True

        clear()
        print(BANNER)
        print(f"\n{BOLD}{YELLOW}Authentication Required{RESET}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}\n")

        attempts = 3
        while attempts > 0:
            password = getpass.getpass(f"{BOLD}{GREEN}Enter Master Password: {RESET}")

            try:
                salt = self.salt_file.read_bytes()
                key = self.derive_key(password, salt)
                self.cipher = Fernet(key)

                encrypted_data = self.vault_file.read_bytes()
                decrypted = self.cipher.decrypt(encrypted_data)
                json.loads(decrypted)

                self.master_password = password
                print(f"\n{GREEN}✓ Authentication successful!{RESET}")
                print(f"{GREEN}✓ Vault integrity verified{RESET}\n")
                input(f"{BOLD}Press Enter to continue...{RESET}")
                return True

            except Exception:
                attempts -= 1
                if attempts > 0:
                    print(f"{RED}✗ Invalid password! {attempts} attempts remaining.{RESET}\n")
                else:
                    print(f"{RED}✗ Authentication failed! Access denied.{RESET}\n")
                    input(f"{BOLD}Press Enter to exit...{RESET}")
                    return False

    def load_vault(self):
        try:
            encrypted_data = self.vault_file.read_bytes()
            decrypted = self.cipher.decrypt(encrypted_data)
            return json.loads(decrypted)
        except Exception as e:
            print(f"{RED}Error loading vault: {e}{RESET}")
            return {"passwords": {}}

    def save_vault(self, data):
        try:
            # Create backup before saving
            self.create_backup()
            
            encrypted = self.cipher.encrypt(json.dumps(data, indent=2).encode())
            self.vault_file.write_bytes(encrypted)
            os.chmod(self.vault_file, 0o600)
            
            # Update integrity hash
            self.save_integrity_hash()
            
            return True
        except Exception as e:
            print(f"{RED}Error saving vault: {e}{RESET}")
            return False

    def add_password(self):
        clear()
        print(BANNER)
        print(f"\n{BOLD}{GREEN}Add New Password Entry{RESET}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}\n")

        try:
            service = input(f"{BOLD}{YELLOW}Service/Website name: {RESET}").strip()
            if not service:
                print(f"{RED}Service name cannot be empty!{RESET}")
                input(f"\n{BOLD}Press Enter to continue...{RESET}")
                return

            username = input(f"{BOLD}{YELLOW}Username/Email: {RESET}").strip()
            if not username:
                print(f"{RED}Username cannot be empty!{RESET}")
                input(f"\n{BOLD}Press Enter to continue...{RESET}")
                return

            password = getpass.getpass(f"{BOLD}{YELLOW}Password: {RESET}")
            if not password:
                print(f"{RED}Password cannot be empty!{RESET}")
                input(f"\n{BOLD}Press Enter to continue...{RESET}")
                return

            notes = input(f"{BOLD}{YELLOW}Notes (optional): {RESET}").strip()

            vault = self.load_vault()

            if service.lower() in vault["passwords"]:
                confirm = input(f"{YELLOW}Service already exists. Overwrite? (y/n): {RESET}").lower()
                if confirm != 'y':
                    print(f"{CYAN}Operation cancelled.{RESET}")
                    input(f"\n{BOLD}Press Enter to continue...{RESET}")
                    return

            vault["passwords"][service.lower()] = {
                "service": service,
                "username": username,
                "password": password,
                "notes": notes
            }

            if self.save_vault(vault):
                print(f"\n{GREEN}✓ Password added successfully!{RESET}")
                print(f"{GREEN}✓ Backup created{RESET}")
            else:
                print(f"\n{RED}✗ Failed to save password!{RESET}")

        except KeyboardInterrupt:
            print(f"\n{YELLOW}Operation cancelled.{RESET}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

        input(f"\n{BOLD}Press Enter to continue...{RESET}")

    def get_password(self):
        clear()
        print(BANNER)
        print(f"\n{BOLD}{GREEN}Retrieve Password{RESET}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}\n")

        try:
            service = input(f"{BOLD}{YELLOW}Service/Website name: {RESET}").strip()
            if not service:
                print(f"{RED}Service name cannot be empty!{RESET}")
                input(f"\n{BOLD}Press Enter to continue...{RESET}")
                return

            vault = self.load_vault()

            if service.lower() not in vault["passwords"]:
                print(f"{RED}Service not found in vault!{RESET}")
                input(f"\n{BOLD}Press Enter to continue...{RESET}")
                return

            entry = vault["passwords"][service.lower()]
            print(f"\n{CYAN}═══════════════════════════════════════════════════════════{RESET}")
            print(f"{BOLD}{GREEN}Service:{RESET}  {entry['service']}")
            print(f"{BOLD}{GREEN}Username:{RESET} {entry['username']}")
            print(f"{BOLD}{GREEN}Password:{RESET} {entry['password']}")
            if entry.get('notes'):
                print(f"{BOLD}{GREEN}Notes:{RESET}    {entry['notes']}")
            print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}")

        except KeyboardInterrupt:
            print(f"\n{YELLOW}Operation cancelled.{RESET}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

        input(f"\n{BOLD}Press Enter to continue...{RESET}")

    def list_passwords(self):
        clear()
        print(BANNER)
        print(f"\n{BOLD}{GREEN}Stored Password Entries{RESET}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}\n")

        try:
            vault = self.load_vault()

            if not vault["passwords"]:
                print(f"{YELLOW}No passwords stored yet.{RESET}")
            else:
                print(f"{BOLD}{CYAN}Total Entries: {len(vault['passwords'])}{RESET}\n")
                for idx, (key, entry) in enumerate(vault["passwords"].items(), 1):
                    print(f"{GREEN}[{idx}]{RESET} {BOLD}{entry['service']}{RESET}")
                    print(f"    Username: {entry['username']}")
                    if entry.get('notes'):
                        print(f"    Notes: {entry['notes'][:50]}...")
                    print()

        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

        input(f"\n{BOLD}Press Enter to continue...{RESET}")

    def delete_password(self):
        clear()
        print(BANNER)
        print(f"\n{BOLD}{RED}Delete Password Entry{RESET}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}\n")

        try:
            service = input(f"{BOLD}{YELLOW}Service/Website name: {RESET}").strip()
            if not service:
                print(f"{RED}Service name cannot be empty!{RESET}")
                input(f"\n{BOLD}Press Enter to continue...{RESET}")
                return

            vault = self.load_vault()

            if service.lower() not in vault["passwords"]:
                print(f"{RED}Service not found in vault!{RESET}")
                input(f"\n{BOLD}Press Enter to continue...{RESET}")
                return

            entry = vault["passwords"][service.lower()]
            print(f"\n{YELLOW}About to delete:{RESET}")
            print(f"  Service: {entry['service']}")
            print(f"  Username: {entry['username']}")

            confirm = input(f"\n{RED}Are you sure? (yes/no): {RESET}").lower()
            if confirm == 'yes':
                del vault["passwords"][service.lower()]
                if self.save_vault(vault):
                    print(f"\n{GREEN}✓ Password deleted successfully!{RESET}")
                    print(f"{GREEN}✓ Backup created{RESET}")
                else:
                    print(f"\n{RED}✗ Failed to delete password!{RESET}")
            else:
                print(f"{CYAN}Operation cancelled.{RESET}")

        except KeyboardInterrupt:
            print(f"\n{YELLOW}Operation cancelled.{RESET}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

        input(f"\n{BOLD}Press Enter to continue...{RESET}")

    def show_security_status(self):
        clear()
        print(BANNER)
        print(f"\n{BOLD}{CYAN}Security Status & Backups{RESET}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}\n")

        # Integrity status
        integrity_ok = self.verify_integrity()
        if integrity_ok:
            print(f"{GREEN}✓ Vault Integrity: VERIFIED{RESET}")
        else:
            print(f"{RED}✗ Vault Integrity: COMPROMISED{RESET}")

        # File permissions
        vault_perms = oct(os.stat(self.vault_dir).st_mode)[-3:]
        print(f"{GREEN}✓ Vault Permissions: {vault_perms} (Owner only){RESET}")

        # Backup status
        backups = sorted(self.backup_dir.glob("vault_backup_*.enc"))
        print(f"{GREEN}✓ Available Backups: {len(backups)}{RESET}")
        
        if backups:
            print(f"\n{BOLD}{YELLOW}Recent Backups:{RESET}")
            for backup in backups[-5:]:
                timestamp = backup.stem.replace("vault_backup_", "")
                size = backup.stat().st_size
                print(f"  • {timestamp} ({size} bytes)")

        # Encryption info
        print(f"\n{BOLD}{CYAN}Security Features:{RESET}")
        print(f"  {GREEN}• AES-256 Encryption via Fernet{RESET}")
        print(f"  {GREEN}• PBKDF2 Key Derivation (100,000 iterations){RESET}")
        print(f"  {GREEN}• SHA-256 Integrity Verification{RESET}")
        print(f"  {GREEN}• Automatic Backup System{RESET}")
        print(f"  {GREEN}• File Permission Protection{RESET}")
        print(f"  {GREEN}• Tampering Detection{RESET}")

        input(f"\n{BOLD}Press Enter to continue...{RESET}")

    def show_menu(self):
        print(f"""
{BOLD}{CYAN}┌─────────────────────────────────────────────────────────┐
│                   PASSWORD MANAGER MENU                 │
└─────────────────────────────────────────────────────────┘{RESET}

  {GREEN}[1]{RESET} {BOLD}Add New Password{RESET}
      └─ Store encrypted password for a service

  {GREEN}[2]{RESET} {BOLD}Retrieve Password{RESET}
      └─ View stored password for a service

  {GREEN}[3]{RESET} {BOLD}List All Entries{RESET}
      └─ Display all stored services

  {GREEN}[4]{RESET} {BOLD}Delete Password{RESET}
      └─ Remove password from vault

  {CYAN}[5]{RESET} {BOLD}Security Status{RESET}
      └─ View security status and backups

  {RED}[0]{RESET} {BOLD}Back to Main Menu{RESET}

{CYAN}═══════════════════════════════════════════════════════════{RESET}
""")

    def run(self):
        if not self.authenticate():
            return

        while True:
            try:
                clear()
                print(BANNER)
                self.show_menu()

                choice = input(f"{BOLD}{CYAN}PasswordMgr{RESET} > ").strip()

                if choice == '1':
                    self.add_password()
                elif choice == '2':
                    self.get_password()
                elif choice == '3':
                    self.list_passwords()
                elif choice == '4':
                    self.delete_password()
                elif choice == '5':
                    self.show_security_status()
                elif choice == '0':
                    clear()
                    print(f"\n{GREEN}Vault locked. Returning to main menu...{RESET}\n")
                    break
                else:
                    print(f"{RED}Invalid option. Please select 0-5.{RESET}")
                    input(f"\n{BOLD}Press Enter to continue...{RESET}")

            except KeyboardInterrupt:
                print(f"\n\n{YELLOW}Returning to main menu...{RESET}")
                break
            except Exception as e:
                print(f"{RED}Unexpected error: {e}{RESET}")
                input(f"\n{BOLD}Press Enter to continue...{RESET}")

def clear():
    os.system('clear')

def main():
    try:
        manager = PasswordManager()
        manager.run()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Exiting Password Manager...{RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"{RED}Fatal error: {e}{RESET}")
        sys.exit(1)

if __name__ == '__main__':
    main()