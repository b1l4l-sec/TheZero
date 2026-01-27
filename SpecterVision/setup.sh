#!/bin/bash

echo "=============================================="
echo "  SpecterVision Setup Script (Venv Mode)"
echo "  Biometric Surveillance & Security Research"
echo "=============================================="

# 1. Install System Dependencies
echo "[INFO] Installing Python3 Venv..."
sudo apt-get update -qq
sudo apt-get install -y python3-venv python3-pip -qq

# 2. Create Virtual Environment
echo "[INFO] Creating Virtual Environment (venv)..."
python3 -m venv venv

# 3. Install Requirements inside the Venv
echo "[INFO] Installing Python dependencies in venv..."
./venv/bin/pip install --upgrade pip --quiet
./venv/bin/pip install -r requirements.txt --quiet

# 4. Create necessary directories
echo "[INFO] Creating necessary directories..."
mkdir -p captures logs

# 5. Set executable permissions
chmod +x spectervision.py

echo ""
echo "=============================================="
echo "  Installation Complete!"
echo "=============================================="
echo "To run SpecterVision, use the launcher:"
echo "  source venv/bin/activate && python3 spectervision.py"
echo "=============================================="
