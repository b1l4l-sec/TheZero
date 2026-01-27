# SpecterVision

```
 _______                     __              ___ ___ _     _
|   _   .-----.-----.----.--|  |.-----.----.|   |   |_|___|_| .-----.----.
|   1___|  _  |  -__|  __|  _  ||  -__|   _| \     /| |   | | |  _  |     |
|____   |   __|_____|____|_____||_____|__|    \___/ |_|_|_|_| |_____|__|__|
|_______|__|   [ v1.0.0-Beta | Biometric Security Research ]
```

## Professional Biometric Surveillance & Security Research Platform

SpecterVision is a comprehensive CLI-based penetration testing tool designed for authorized cybersecurity research and educational purposes. Built specifically for Kali Linux, it provides automated biometric surveillance capabilities with real-time camera capture, session management, and remote access functionality.

---

## Features

- **Professional CLI Interface** - Interactive terminal-based control panel with ASCII banner
- **Automated Camera Capture** - Captures frames every 3 seconds automatically without user interaction
- **Session Management** - Organized session directories with metadata and sequential frame numbering
- **Web-Based Interface** - Responsive HTML5 interface accessible via browser
- **ngrok Integration** - Remote access capability through secure tunnels
- **Real-Time Detection** - Optional emotion detection and motion detection features
- **Dependency Management** - Automatic installation and verification of required packages
- **Professional Design** - Clean, business-oriented interface with no distractions
- **Security Focused** - Built with security research and penetration testing in mind

---

## System Requirements

- **Operating System**: Kali Linux 2023.x or later (also compatible with Ubuntu/Debian)
- **Python**: Python 3.8 or higher
- **Browser**: Firefox, Chrome, or Chromium
- **Internet**: Required for ngrok and TensorFlow.js CDN
- **Camera**: Webcam or integrated camera
- **RAM**: Minimum 2GB, Recommended 4GB+
- **Storage**: 500MB free space for application and captures

---

## Installation

### Method 1: Automated Setup (Recommended)

```bash
cd spectervision
chmod +x setup.sh
./setup.sh
```

### Method 2: Manual Installation

```bash
cd spectervision

sudo apt-get update
sudo apt-get install -y python3 python3-pip

pip3 install -r requirements.txt

mkdir -p captures logs

chmod +x spectervision.py
```

---

## Usage

### Starting SpecterVision

```bash
python3 spectervision.py
```

Or if executable permissions are set:

```bash
./spectervision.py
```

### Main Menu Options

```
[1] Launch Local Server (Port 5000)
    - Starts Flask web server on localhost:5000
    - Automatically opens browser to the web interface
    - Use this for local testing and operation

[2] Start ngrok Tunnel (Global Access)
    - Creates a public URL for remote access
    - Displays both local and public URLs
    - Keeps tunnel active until Ctrl+C

[3] Open Captures Directory
    - Opens file manager to view captured sessions
    - Shows all saved frames and metadata

[4] Check System Dependencies
    - Displays status of all required packages
    - Shows which packages are installed/missing
    - Attempts to install missing packages

[0] Exit
    - Clean shutdown of the application
```

### Web Interface Workflow

1. **Initialize Camera** - Click "Initialize Camera" button to request camera permissions
2. **Automatic Capture** - Frames are captured every 3 seconds automatically
3. **Monitor Session** - Watch frame counter and session information update in real-time
4. **Detection Modes** (Optional):
   - Enable Emotion Detection for face recognition overlay
   - Enable Motion Detection for movement highlighting
5. **End Session** - Click "End Session" to stop capture and save all data

---

## Project Structure

```
spectervision/
├── spectervision.py          # Main CLI entry point
├── requirements.txt          # Python dependencies
├── setup.sh                  # Automated installation script
├── README.md                 # This file
├── core/                     # Core application modules
│   ├── server.py            # Flask web server
│   ├── session_manager.py   # Session handling
│   ├── dependency_checker.py # Package management
│   └── ngrok_manager.py     # Tunnel management
├── config/                   # Configuration files
│   ├── settings.py          # Application settings
│   └── banner.py            # ASCII art and colors
├── utils/                    # Utility modules
│   ├── file_handler.py      # File operations
│   └── logger.py            # Logging system
├── static/                   # Web interface assets
│   ├── css/
│   │   └── style.css        # Professional styling
│   └── js/
│       ├── camera.js        # Camera management
│       ├── capture.js       # Automated capture
│       ├── emotion.js       # Emotion detection
│       └── motion.js        # Motion detection
├── templates/
│   └── index.html           # Web interface
├── captures/                 # Session data (auto-generated)
└── logs/                     # Application logs (auto-generated)
```

---

## Session Data Structure

Each camera session creates a unique directory:

```
captures/
└── client_20260104_143022_A7B3F/
    ├── metadata.json         # Session information
    ├── frame_001.jpg         # First captured frame
    ├── frame_002.jpg         # Second captured frame
    ├── frame_003.jpg         # Third captured frame
    └── ...
```

### Metadata Format

```json
{
    "session_id": "client_20260104_143022_A7B3F",
    "start_time": "2026-01-04T14:30:22.123456",
    "ip_address": "127.0.0.1",
    "user_agent": "Mozilla/5.0...",
    "frames_captured": 0
}
```

---

## Detection Features

### Emotion Detection
- Powered by TensorFlow.js Face Landmarks Detection
- Detects up to 5 faces in real-time
- Draws green bounding boxes around detected faces
- Labels each face with "Face Detected"

### Motion Detection
- Pixel-by-pixel frame comparison
- Highlights movement areas in red
- Adjustable sensitivity thresholds
- Real-time motion indicator overlay

---

## Troubleshooting

### Camera Not Working

**Problem**: Camera permission denied or video not showing

**Solutions**:
- Ensure browser has camera permissions enabled
- Check if another application is using the camera
- Try a different browser (Firefox, Chrome, Chromium)
- For HTTPS requirement on remote connections, use ngrok tunnel

### Dependencies Not Installing

**Problem**: Package installation fails

**Solutions**:
```bash
sudo apt-get update
sudo apt-get install -y python3-dev build-essential
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

### ngrok Tunnel Fails

**Problem**: Cannot create public tunnel

**Solutions**:
- Check internet connection
- Visit https://ngrok.com and create a free account
- Run: `ngrok authtoken YOUR_TOKEN`
- Restart SpecterVision

### Port Already in Use

**Problem**: Flask server cannot start on port 5000

**Solutions**:
```bash
sudo lsof -ti:5000 | xargs kill -9
```

Or edit `config/settings.py` to change `SERVER_PORT` to a different port.

### No Frames Captured

**Problem**: Frames not saving to disk

**Solutions**:
- Check write permissions: `chmod -R 755 captures/`
- Ensure sufficient disk space: `df -h`
- Check logs: `tail -f logs/spectervision_*.log`

---

## Security Considerations

### Authentication
- By default, Flask server runs on 0.0.0.0 (accessible to local network)
- ngrok tunnels are public by default - use with caution
- Consider implementing authentication for production use

### Data Privacy
- All captured frames are stored locally in plaintext
- Session metadata includes IP addresses
- Ensure compliance with applicable privacy laws
- Delete sensitive data after research is complete

### Network Security
- Flask debug mode is disabled by default
- CORS is enabled for cross-origin requests
- Use HTTPS in production environments
- Monitor access logs regularly

---

## Legal Disclaimer

**IMPORTANT**: This tool is designed exclusively for **authorized educational and security research purposes**.

### Authorized Uses:
- Penetration testing engagements with written authorization
- Capture The Flag (CTF) competitions and challenges
- Cybersecurity training and education
- Defensive security research and tool development
- Personal security testing on owned devices

### Prohibited Uses:
- Unauthorized surveillance or monitoring of individuals
- Recording without explicit consent in jurisdictions where required
- Any form of illegal spying or privacy invasion
- Violation of computer fraud and abuse laws
- Any activity that violates local, state, or federal laws

**Users are solely responsible for ensuring compliance with all applicable laws and regulations. The developers assume no liability for misuse of this tool.**

---

## License

This project is released under the MIT License.

```
MIT License

Copyright (c) 2026 SpecterVision

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Contributing

This is a security research tool. Contributions should focus on:
- Security improvements
- Bug fixes
- Performance optimizations
- Documentation enhancements
- Additional detection algorithms

---

## Support

For issues, questions, or contributions, please refer to the project documentation.

**Remember**: Always obtain proper authorization before conducting security research or penetration testing.

---

**SpecterVision v1.0.0-Beta**
*Professional Biometric Surveillance & Security Research Platform*
