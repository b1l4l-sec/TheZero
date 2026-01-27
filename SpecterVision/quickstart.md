# SpecterVision Quick Start Guide

## Instant Setup

# Download the compressed binary
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz

# Extract it
tar -xvzf ngrok-v3-stable-linux-amd64.tgz

# Move it to /usr/local/bin so the whole system can use it
sudo mv ngrok /usr/local/bin/

# Verify it works
ngrok --version

ngrok config add-authtoken YOUR_ACTUAL_TOKEN_HERE


```bash
cd spectervision
chmod +x setup.sh spectervision.py
./setup.sh
```
sudo apt-get update && sudo apt-get install -y libjpeg-dev zlib1g-dev python3-dev

# 1. Delete the broken virtual environment
rm -rf venv/

# 2. Run your setup script again
./setup.sh

## Run SpecterVision

source venv/bin/activate
python3 spectervision.py

## Quick Usage

1. **Select Option 1** - Launch Local Server
2. **Browser opens automatically** to http://localhost:5000
3. **Click "Initialize Camera"** - Grant camera permissions
4. **Automated capture starts** - Frames captured every 3 seconds
5. **Monitor session** - Watch frame counter increment
6. **End session** when done - All data saved to captures/

## Menu Options

- `[1]` Launch Local Server - Start web interface on port 5000
- `[2]` Start ngrok Tunnel - Get public URL for remote access
- `[3]` Open Captures Directory - View all captured sessions
- `[4]` Check System Dependencies - Verify package installation
- `[0]` Exit - Clean shutdown

## Captured Data Location

```
spectervision/captures/client_YYYYMMDD_HHMMSS_XXXXX/
├── metadata.json
├── frame_001.jpg
├── frame_002.jpg
└── ...
```

## Troubleshooting

### Camera not working?
- Allow camera permissions in browser
- Try Firefox or Chrome
- Check if another app is using camera

### Port 5000 in use?
```bash
sudo lsof -ti:5000 | xargs kill -9
```

### Dependencies missing?
```bash
pip3 install -r requirements.txt
```

## Remote Access with ngrok

1. Select option `[2]` from main menu
2. Copy the public ngrok URL displayed
3. Share URL with remote device
4. Access from anywhere with internet

## Detection Features

- **Emotion Detection** - Face recognition with bounding boxes
- **Motion Detection** - Highlights movement in red overlay
- Enable from web interface after camera initialization

---

**For detailed documentation, see README.md**
