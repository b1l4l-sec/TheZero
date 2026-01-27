#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${GREEN}"
echo "████████╗██╗  ██╗███████╗███████╗███████╗██████╗  ██████╗ "
echo "╚══██╔══╝██║  ██║██╔════╝╚══███╔╝██╔════╝██╔══██╗██╔═══██╗"
echo "   ██║   ███████║█████╗    ███╔╝ █████╗  ██████╔╝██║   ██║"
echo "   ██║   ██╔══██║██╔══╝   ███╔╝  ██╔══╝  ██╔══██╗██║   ██║"
echo "   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║╚██████╔╝"
echo "   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝"
echo -e "${NC}"
echo -e "${CYAN}════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}         Professional Pentesting Suite - Setup${NC}"
echo -e "${CYAN}           Developed by b1l4l-sec | v2.3${NC}"
echo -e "${CYAN}════════════════════════════════════════════════════════${NC}\n"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${BOLD}${YELLOW}[1/9] Checking System Requirements...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Python3 not found. Installing...${NC}"
    sudo apt-get update -qq
    sudo apt-get install -y python3 python3-pip python3-venv
else
    echo -e "${GREEN}✓ Python3 found${NC}"
fi

echo -e "\n${BOLD}${YELLOW}[2/9] Installing System Dependencies...${NC}"
sudo apt-get update -qq
sudo apt-get install -y \
    python3-dev \
    python3-pip \
    python3-venv \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    xdg-utils \
    -qq 2>&1 | grep -v "Setting up\|Processing\|Preparing" || true
echo -e "${GREEN}✓ System dependencies installed${NC}"

echo -e "\n${BOLD}${YELLOW}[3/9] Creating Virtual Environment...${NC}"
if [ -d "venv" ]; then
    echo -e "${YELLOW}Removing existing virtual environment...${NC}"
    rm -rf venv
fi
python3 -m venv venv
echo -e "${GREEN}✓ Virtual environment created${NC}"

echo -e "\n${BOLD}${YELLOW}[4/9] Activating Virtual Environment...${NC}"
source venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}"

echo -e "\n${BOLD}${YELLOW}[5/9] Upgrading pip...${NC}"
pip install --upgrade pip --quiet
echo -e "${GREEN}✓ pip upgraded${NC}"

echo -e "\n${BOLD}${YELLOW}[6/9] Installing Python Dependencies...${NC}"
echo -e "${CYAN}Installing SpecterVision dependencies...${NC}"
if [ -f "SpecterVision/requirements.txt" ]; then
    pip install -r SpecterVision/requirements.txt --quiet
    echo -e "${GREEN}✓ SpecterVision dependencies installed${NC}"
fi

echo -e "${CYAN}Installing SocialEng dependencies...${NC}"
pip install requests beautifulsoup4 phonenumbers lxml --quiet
echo -e "${GREEN}✓ SocialEng dependencies installed${NC}"

echo -e "${CYAN}Installing DoDOS dependencies...${NC}"
pip install scapy colorama --quiet
echo -e "${GREEN}✓ DoDOS dependencies installed${NC}"

echo -e "${CYAN}Installing PasswordManager dependencies...${NC}"
pip install cryptography --quiet
echo -e "${GREEN}✓ PasswordManager dependencies installed${NC}"

echo -e "${CYAN}Installing MASTERLock dependencies...${NC}"
pip install cryptography pyinstaller --quiet
echo -e "${GREEN}✓ MASTERLock dependencies installed${NC}"

echo -e "\n${BOLD}${YELLOW}[7/9] Setting Permissions...${NC}"
chmod +x thezero.py
chmod +x "Crypto&portScan/thezero.py" 2>/dev/null || true
chmod +x SpecterVision/spectervision.py 2>/dev/null || true
chmod +x SpecterVision/setup.sh 2>/dev/null || true
chmod +x SocialEng/socialeng.py 2>/dev/null || true
chmod +x HackWIN/hackwin.py 2>/dev/null || true
chmod +x DoDOS/dodos.py 2>/dev/null || true
chmod +x PasswordManager/password_manager.py 2>/dev/null || true
chmod +x MASTERLock/masterlock.py 2>/dev/null || true
echo -e "${GREEN}✓ Executable permissions set${NC}"

echo -e "\n${BOLD}${YELLOW}[8/9] Creating necessary directories...${NC}"
mkdir -p "Crypto&portScan" 2>/dev/null || true
mkdir -p "SpecterVision/captures" 2>/dev/null || true
mkdir -p "SpecterVision/logs" 2>/dev/null || true
mkdir -p "SocialEng/targets" 2>/dev/null || true
mkdir -p "SocialEng/modules" 2>/dev/null || true
mkdir -p "HackWIN" 2>/dev/null || true
mkdir -p "DoDOS/modules" 2>/dev/null || true
mkdir -p "PasswordManager/vault" 2>/dev/null || true
mkdir -p "PasswordManager/.backup" 2>/dev/null || true
mkdir -p "MASTERLock/modules" 2>/dev/null || true
echo -e "${GREEN}✓ Directories created${NC}"

echo -e "\n${BOLD}${YELLOW}[9/9] Securing Password Manager Vault...${NC}"

# Set strict file permissions on vault directory
if [ -d "PasswordManager/vault" ]; then
    chmod 700 "PasswordManager/vault"
    echo -e "${GREEN}✓ Vault folder protected (700)${NC}"
fi

# Set strict permissions on backup directory
if [ -d "PasswordManager/.backup" ]; then
    chmod 700 "PasswordManager/.backup"
    echo -e "${GREEN}✓ Backup folder protected (700)${NC}"
fi

# Secure any existing vault files
if [ -f "PasswordManager/vault/passwords.enc" ]; then
    chmod 600 "PasswordManager/vault/passwords.enc"
    echo -e "${GREEN}✓ Vault file secured (600)${NC}"
fi

if [ -f "PasswordManager/vault/salt.key" ]; then
    chmod 600 "PasswordManager/vault/salt.key"
    echo -e "${GREEN}✓ Salt file secured (600)${NC}"
fi

if [ -f "PasswordManager/vault/.integrity" ]; then
    chmod 600 "PasswordManager/vault/.integrity"
    echo -e "${GREEN}✓ Integrity file secured (600)${NC}"
fi

echo -e "${CYAN}Security measures applied:${NC}"
echo -e "  ${YELLOW}• Vault folder: Only accessible by you (700)${NC}"
echo -e "  ${YELLOW}• Vault files: Read/Write only by you (600)${NC}"
echo -e "  ${YELLOW}• Hidden backup location created${NC}"
echo -e "  ${YELLOW}• Integrity verification enabled${NC}"

echo -e "\n${GREEN}"
echo "════════════════════════════════════════════════════════"
echo "           INSTALLATION COMPLETE!"
echo "════════════════════════════════════════════════════════"
echo -e "${NC}"
echo -e "${BOLD}${CYAN}To start TheZero:${NC}"
echo -e "  ${YELLOW}./thezero.py${NC}"
echo ""
echo -e "${BOLD}${CYAN}Or:${NC}"
echo -e "  ${YELLOW}python3 thezero.py${NC}"
echo ""
echo -e "${CYAN}Note: Virtual environment activates automatically${NC}"
echo -e "${YELLOW}Developer: b1l4l-sec | GitHub: https://github.com/b1l4l-sec${NC}"
echo ""
echo -e "${BOLD}${RED}⚠ SECURITY NOTICE:${NC}"
echo -e "${YELLOW}Password Manager vault is now protected with:${NC}"
echo -e "${YELLOW}  • File integrity verification${NC}"
echo -e "${YELLOW}  • Automatic backup system${NC}"
echo -e "${YELLOW}  • Strict file permissions${NC}"
echo -e "${YELLOW}  • Tampering detection${NC}"
echo ""
echo -e "${GREEN}════════════════════════════════════════════════════════${NC}\n"