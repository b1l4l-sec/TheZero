import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAPTURES_DIR = os.path.join(BASE_DIR, 'captures')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000

CAPTURE_INTERVAL = 3000
IMAGE_QUALITY = 0.85
VIDEO_WIDTH = 640
VIDEO_HEIGHT = 480

MAX_FRAME_SIZE = 5 * 1024 * 1024

REQUIRED_PACKAGES = [
    'flask',
    'flask_cors',
    'cv2',
    'PIL',
    'requests',
    'pyngrok'
]
