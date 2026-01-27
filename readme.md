# TheZero - Offensive Security & OSINT Swiss Army Knife 🚀

![TheZero Banner](https://raw.githubusercontent.com/b1l4l-sec/TheZero/main/Crypto&portScan/logo.py)

**Author:** [b1l4l-sec](https://github.com/b1l4l-sec)  
**Version:** 2.0  
**Platforms:** Linux (Kali recommended), macOS, WSL  
**License:** Educational/Research Use Only

---

## Introduction

**TheZero** is a professional modular penetration testing & OSINT (Open Source Intelligence) framework for red teams, security researchers, and CTF competitors. Its goal is to streamline reconnaissance, credential and vault management, biometric surveillance, social engineering, and network/crypto operations into a single, streamlined toolkit.

> "Every master was once a beginner. Every hero was once a zero."  

---

## 🔥 Module Overview

### 1. PasswordManager
- Encrypted vaults with integrity checks.
- Salted hashing, secure key handling, and CLI utilities.

### 2. SocialEng (Social Engineering)
A comprehensive OSINT and social engineering suite for lawful security assessments.
- **Email harvesting**: Multi-domain, multi-source, export to JSON/TXT.
- **Phone number validation**: International formats, carrier, timezone.
- **Username generator**: Pattern combos, birth year, export.
- **Target profiling**: Full-profile creation with exports.
- **Social media enumeration**: Checks 10+ platforms for username presence.

*See full details at [`SocialEng/README.md`](SocialEng/README.md).*

### 3. Crypto & Port Scanner
- **Port Scanner**: Find open ports, analyze hosts.
- **Cryptography Tools**: Fast Base64/Base32 encode/decode.
- **UI**: Colorful, interactive terminal output.
- **Platform**: Written in Python, tested on Kali Linux.

*Usage:*
```bash
python3 Crypto&portScan/main.py
```

### 4. SpecterVision (Biometric Surveillance Lab)
Automated, professional-grade biometric surveillance for red team ops & research:
- CLI and Web (Flask) interface
- Automated camera frame capture w/ session management
- Real-time emotion/motion detection via TensorFlow.js (browser)
- Remote access using ngrok for training/POC
- Dependency auto-installed, organized output/capture management

*Quick start:*
```bash
cd SpecterVision
chmod +x setup.sh
./setup.sh
python3 spectervision.py
```
*See [`SpecterVision/readme.md`](SpecterVision/readme.md) for full instructions!*


### 5. DoDOS – Network Stress Testing (CTF/Education Only!)
- Ethical DoS testing for lab, CTF, or explicitly authorized scenarios.
- Big legal warnings, strict anti-abuse rules.

---

## Project Structure

```
TheZero/
├── PasswordManager/
│   └── vault/.integrity    # Vault hash & salt control
├── SocialEng/
│   ├── README.md           # Full OSINT tool suite docs
│   ├── targets/            # Output: emails, usernames, profiles, enum results
│   └── modules/            # Python implementation
├── Crypto&portScan/
│   ├── main.py             # CLI for port scanning & crypto tools
│   ├── logo.py             # Terminal banners & visuals
│   └── readme              # Quick usage and features
├── SpecterVision/
│   ├── core/               # Flask backend, session manager, file handler
│   ├── static/             # Web assets (JS, CSS)
│   ├── setup.sh            # Automated installer
│   └── readme.md           # Full biometric tool docs
├── DoDOS/
│   └── dodos.py            # Legal/CTF DoS testing CLI
└── ... (other supporting modules)
```

---

## 🚦 Legal & Ethical Usage

### YOU MAY:
- Use for **authorized penetration testing** with prior WRITTEN consent
- Use in **CTF competitions, research labs, or training**
- Learn and experiment in your own legal, isolated environment

### YOU MUST NOT:
- Run any attacks or scans on targets without **explicit authorization**
- Violate privacy, abuse cloud resources or harass individuals
- Use for any illegal activity

**Any misuse is strictly prohibited and may carry severe legal penalties. By using TheZero, you accept full responsibility for lawful, ethical use.**

---

## 🤝 Contributing & Community

PRs and suggestions welcome! Please open issues for bugs or feature requests.  
Connect via [GitHub](https://github.com/b1l4l-sec/TheZero).

---

## 👏 Credits

Made with ❤️ by [b1l4l-sec](https://github.com/b1l4l-sec) and inspired by the open-source community.

---

## Links
- **[SocialEng - Full Module Readme](SocialEng/README.md)**
- **[SpecterVision - Biometric Surveillance Docs](SpecterVision/readme.md)**

---
