# TheZero v2.3 - Changes Summary

## Date: 2026-01-26
## Developer: b1l4l-sec

---

## Major Changes

### 1. NEW MODULE: MASTER Lock Ransomware Simulation

Added comprehensive ransomware simulation toolkit for CTF challenges and security education.

**Features:**
- Symmetric encryption (Fernet/AES-128 CBC)
- Full-screen lock GUI with Matrix aesthetics
- Windows executable compilation
- Educational CTF payload generator
- Safe default target directory
- Full file recovery capability

**Files Created:**
```
MASTERLock/
├── masterlock.py               # Main entry point
├── README.md                   # Comprehensive documentation
└── modules/
    ├── __init__.py
    ├── crypto_engine.py        # Encryption/decryption core
    └── payload.py              # Windows executable payload
```

**Menu Location:** Option [4] in main menu

---

## Updated Files

### thezero.py
- Added MASTER Lock menu option [4]
- Renumbered existing options:
  - HackWIN: [4] → [5]
  - DoDOS: [5] → [6]
  - Password Manager: [6] → [7]
  - Documentation: [7] → [8]
- Added `launch_masterlock()` function
- Added `show_masterlock_help()` function
- Updated documentation menu with MASTER Lock help [4]
- Updated version to 2.3
- Updated error message: "0-7" → "0-8"

### setup.sh
- Added MASTERLock dependencies installation
  - `cryptography` - Already installed, used for encryption
  - `pyinstaller` - NEW, for Windows executable compilation
- Added `chmod +x MASTERLock/masterlock.py`
- Added `mkdir -p MASTERLock/modules`
- Updated version banner to v2.3

---

## New Menu Structure

```
TheZero Main Menu v2.3
├── [1] Crypto & Port Scanner Suite
├── [2] SpecterVision Surveillance
├── [3] Social Engineering Framework
├── [4] Deploy MASTER Lock (NEW)
├── [5] HackWIN Payload Generator (moved from [4])
├── [6] DoDOS Stress Testing (moved from [5])
├── [7] Password Manager (moved from [6])
├── [8] View Documentation (moved from [7])
└── [0] Exit

MASTER Lock Sub-Menu
├── [1] Deploy MASTER Lock
├── [2] Build Windows Executable
├── [3] Test Decryption Tool
├── [4] View Documentation
└── [0] Back to Main Menu

Documentation Menu
├── [1] Crypto & Port Scanner Help
├── [2] SpecterVision Help
├── [3] Social Engineering Help
├── [4] MASTER Lock Help (NEW)
├── [5] HackWIN Help (moved from [4])
├── [6] DoDOS Help (moved from [5])
├── [7] Password Manager Help (moved from [6])
└── [0] Back to Main Menu
```

---

## Dependencies Added

### Python Packages
- **pyinstaller** - Compiles Python scripts to standalone executables
- **cryptography** - Already installed, used for Fernet encryption

### Installation
```bash
pip install pyinstaller cryptography
```

Or run the updated setup script:
```bash
./setup.sh
```

---

## MASTER Lock Features Detail

### Payload Generation
- **Key Generation:** Cryptographically secure Fernet key
- **Configuration:** Custom contact information for ransom note
- **Storage:** Key saved as `secret.key` for recovery
- **Target:** Default `C:\CTF_Challenge\VictimFiles` (safe placeholder)

### Encryption Engine
- **Algorithm:** Fernet (AES-128 in CBC mode with HMAC)
- **Operation:** Recursive directory encryption
- **Functions:**
  - `encrypt_file()` - Encrypt single file
  - `decrypt_file()` - Decrypt single file
  - `encrypt_directory()` - Recursive encryption
  - `decrypt_directory()` - Recursive decryption

### Windows Executable
- **Compilation:** PyInstaller
- **Options:** `--noconsole --onefile`
- **Output:** `dist/MASTERLock.exe`
- **Size:** Approximately 10-15 MB
- **Features:** Standalone, no Python runtime required

### GUI Lock Screen
- **Framework:** tkinter (Python standard library)
- **Style:** Full-screen, Matrix theme (black/#00FF00)
- **Features:**
  - Always on top
  - Close button disabled
  - Custom ransom message
  - Contact information display
  - Key input interface
  - Automatic decryption on valid key

---

## Legal & Security Warnings

### Enhanced Authorization Checks
- Legal warning displayed on launch
- User must confirm written authorization
- Comprehensive consequences outlined
- Clear authorized uses listed
- Prohibited activities specified

### Warning Text Includes:
- CTF competition authorization
- Security training lab requirements
- Personal testing guidelines
- Criminal prosecution risks
- Civil liability warnings
- Developer liability disclaimer

---

## Technical Implementation

### Architecture
```
MASTERLock/
├── masterlock.py                  # Main CLI interface
│   ├── Menu system
│   ├── Configuration dialogs
│   ├── Legal warnings
│   ├── Build commands
│   └── Module imports
│
└── modules/
    ├── crypto_engine.py           # Encryption core
    │   ├── generate_key()
    │   ├── save_key()
    │   ├── load_key()
    │   ├── encrypt_file()
    │   ├── decrypt_file()
    │   ├── encrypt_directory()
    │   └── decrypt_directory()
    │
    └── payload.py                 # Standalone executable
        ├── Encryption logic
        ├── GUI implementation
        ├── Key verification
        └── Automatic decryption
```

### Encryption Process
1. Generate Fernet key (32 bytes, URL-safe base64)
2. Save key to `secret.key`
3. Recursively walk target directory
4. Read each file in binary mode
5. Encrypt with Fernet
6. Overwrite original file with encrypted data

### Decryption Process
1. Load key from `secret.key`
2. Display GUI lock screen
3. Wait for key input
4. Verify entered key
5. If valid, recursively decrypt all files
6. Restore original file contents
7. Close application

### GUI Implementation
- **Main Screen:**
  - Title: "You got hacked from a my MASTER"
  - Warning: "YOUR FILES HAVE BEEN ENCRYPTED"
  - Contact: Customizable contact information
  - Button: "you wanna unlock your shits?"

- **Key Input Screen:**
  - Title: "ENTER DECRYPTION KEY"
  - Input: Text entry field (50 characters wide)
  - Button: "Verify Key"
  - Status: Success/error messages

---

## Usage Examples

### Generate Payload Example
```
1. Launch TheZero: ./thezero.py
2. Select [4] - Deploy MASTER Lock
3. Confirm authorization: yes
4. Select [1] - Deploy MASTER Lock
5. Enter contact: attacker@ctf.local
6. Key saved to: MASTERLock/secret.key
```

### Build Executable Example
```
1. Select [2] - Build Windows Executable
2. Review PyInstaller command
3. Confirm build: yes
4. Wait 1-2 minutes
5. Executable: dist/MASTERLock.exe
```

### CTF Deployment Example
```
# On target Windows system:
1. mkdir C:\CTF_Challenge\VictimFiles
2. echo "Flag{test}" > C:\CTF_Challenge\VictimFiles\flag.txt
3. Copy MASTERLock.exe to system
4. Execute MASTERLock.exe
5. Files encrypted, GUI displays
6. Enter key from secret.key
7. Files decrypt, app closes
```

---

## File Permissions

All new files automatically set to executable:
```bash
chmod +x MASTERLock/masterlock.py
chmod +x MASTERLock/modules/payload.py
```

---

## Testing Checklist

- [x] MASTER Lock launches from main menu
- [x] Legal warning displays correctly
- [x] Payload generation works
- [x] Key saved to secret.key
- [x] PyInstaller command displays
- [x] Build instructions clear
- [x] Documentation displays
- [x] Ctrl+C interrupts gracefully
- [x] Returns to main menu properly
- [x] Help text in documentation menu
- [x] Setup.sh installs dependencies
- [x] Directories created correctly
- [x] All syntax checks pass

---

## PyInstaller Build Command

```bash
pyinstaller --noconsole --onefile --name MASTERLock \
            --add-data "modules;modules" \
            modules/payload.py
```

**Options:**
- `--noconsole` - No console window (GUI only)
- `--onefile` - Single executable file
- `--name MASTERLock` - Output filename
- `--add-data` - Include modules directory

**Output:**
- `build/` - Temporary build files
- `dist/MASTERLock.exe` - Final executable
- `MASTERLock.spec` - PyInstaller spec file

---

## Backward Compatibility

### No Breaking Changes
- All existing functionality preserved
- Menu options renumbered but accessible
- No data migration needed
- Virtual environment compatible

### Menu Navigation Changes
- Previous option [4] (HackWIN) → Now [5]
- Previous option [5] (DoDOS) → Now [6]
- Previous option [6] (Password Manager) → Now [7]
- Previous option [7] (Documentation) → Now [8]

---

## Security Considerations

### What This Tool Does
✓ Demonstrates ransomware encryption techniques
✓ Provides CTF challenge infrastructure
✓ Educates on malware behavior
✓ Tests incident response procedures
✓ Trains security professionals

### What This Tool Does NOT Do
✗ Target system files (safe directory only)
✗ Spread to other systems (no worm)
✗ Communicate over network (no C2)
✗ Escalate privileges (user-level only)
✗ Establish persistence (no startup)
✗ Exfiltrate data (no data leakage)

### Safety Features
- Placeholder target directory
- Local key storage for recovery
- No network communication
- No privilege escalation
- No persistence mechanisms
- Full reversibility guaranteed

---

## Future Enhancements

Potential additions for next version:
- Multiple encryption algorithms (AES-256, RSA)
- Custom target directory selection
- Encryption progress indicator
- File type filtering
- Exclusion list support
- Backup creation before encryption
- Automated testing framework

---

## Credits

**Developer:** b1l4l-sec
**GitHub:** https://github.com/b1l4l-sec
**Version:** 2.3
**Date:** 2026-01-26
**License:** Educational Use Only

---

## Disclaimer

This tool is provided for educational purposes and authorized security testing only. The developer assumes no liability for misuse. Users are solely responsible for ensuring compliance with all applicable laws and regulations.

**Use Cases:**
- CTF (Capture The Flag) competitions
- Security training laboratories
- Malware analysis education
- Incident response training
- Defensive security research

**Prohibited Uses:**
- Unauthorized deployment on any system
- Extortion or financial gain
- Distribution without disclosure
- Production system testing
- Any illegal activity

**Legal Notice:**
Unauthorized use of ransomware simulation tools may violate:
- Computer Fraud and Abuse Act (CFAA)
- State computer crime statutes
- International cybercrime laws
- Terms of service agreements

Always obtain explicit written authorization before deploying this tool.

---

**Status:** PRODUCTION READY ✓

All changes implemented and tested successfully.

---

*Generated: 2026-01-26*
*Developer: b1l4l-sec*
*Project: TheZero Penetration Testing Suite v2.3*
