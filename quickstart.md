# TheZero - Quick Start Guide v2.0

## Installation (One Command)

```bash
cd TheZero && chmod +x Setup.sh && ./Setup.sh
```

Wait 2-3 minutes for complete installation.

## Launch TheZero

```bash
./thezero.py
```

## Menu Structure

```
TheZero Main Menu v2.0
├── [1] Crypto & Port Scanner Suite
│   ├── [1] Ports Scanner
│   ├── [2] Cryptography x64 (Base64/32)
│   ├── [3] Caesar Cipher
│   ├── [4] Password Generator
│   └── [5] Back to Main Menu
│
├── [2] SpecterVision Surveillance
│   ├── [1] Launch Local Server
│   ├── [2] Start ngrok Tunnel
│   ├── [3] Open Captures Directory
│   ├── [4] Check Dependencies
│   └── [0] Back to Main Menu
│
├── [3] Social Engineering Framework (NEW)
│   ├── [1] Email Harvesting
│   ├── [2] Phone Number Validation
│   ├── [3] Username Generation
│   ├── [4] Target Profiling
│   ├── [5] Social Media Enumeration
│   └── [0] Back to Main Menu
│
├── [4] View Documentation
│   ├── [1] Crypto & Port Scanner Help
│   ├── [2] SpecterVision Help
│   ├── [3] Social Engineering Help
│   └── [0] Back to Main Menu
│
└── [0] Exit
```

## Common Tasks

### Scan a Network
1. Launch TheZero: `./thezero.py`
2. Select `[1]` - Crypto & Port Scanner Suite
3. Select `[1]` - Ports Scanner
4. Enter target IP or hostname
5. Type `back` when done

### Harvest Emails (NEW)
1. Launch TheZero: `./thezero.py`
2. Select `[3]` - Social Engineering Framework
3. Select `[1]` - Email Harvesting
4. Enter target URL
5. Results saved to `SocialEng/targets/`

### Generate Usernames (NEW)
1. Launch TheZero: `./thezero.py`
2. Select `[3]` - Social Engineering Framework
3. Select `[3]` - Username Generation
4. Enter first name and last name
5. View generated variations

### Capture Camera Frames
1. Launch TheZero: `./thezero.py`
2. Select `[2]` - SpecterVision
3. Select `[1]` - Launch Local Server
4. Browser opens automatically
5. Click "Initialize Camera"
6. Frames captured every 3 seconds
7. Press Ctrl+C to return to main menu

### Generate Strong Password
1. Launch TheZero: `./thezero.py`
2. Select `[1]` - Crypto & Port Scanner Suite
3. Select `[4]` - Password Generator
4. Enter desired length parameters
5. Copy generated password

## Troubleshooting

### Setup Failed
```bash
rm -rf venv
./Setup.sh
```

### Permission Denied
```bash
chmod +x setup.sh thezero.py
```

### Port 5000 in Use
```bash
sudo lsof -ti:5000 | xargs kill -9
```

### Python Not Found
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
```

## File Locations

- **Captured Images**: `SpecterVision/captures/`
- **Target Data**: `SocialEng/targets/`
- **Logs**: `SpecterVision/logs/`
- **Virtual Environment**: `venv/`

## Tips

- thezero.py automatically activates the virtual environment
- Use `Ctrl+C` in sub-tools to return to main menu
- Type `back` or `exit` to return to previous menu
- Check documentation with option `[4]`

## Legal Reminder

Always obtain authorization before:
- Scanning networks
- Recording camera footage
- Gathering intelligence
- Conducting security tests

---

**Developer**: b1l4l-sec | **Version**: 2.0 | **GitHub**: https://github.com/b1l4l-sec

**Need Help?** Select option `[4]` from the main menu for detailed documentation.
