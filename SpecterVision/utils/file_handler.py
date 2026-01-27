import os
import json
from datetime import datetime
from config.settings import CAPTURES_DIR

def create_session_directory(session_id):
    session_dir = os.path.join(CAPTURES_DIR, session_id)
    os.makedirs(session_dir, exist_ok=True)
    return session_dir

def save_metadata(session_dir, metadata):
    metadata_path = os.path.join(session_dir, 'metadata.json')
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=4)
    return metadata_path

def get_next_frame_number(session_dir):
    existing_frames = [
        f for f in os.listdir(session_dir)
        if f.startswith('frame_') and f.endswith('.jpg')
    ]
    return len(existing_frames) + 1

def save_frame(session_dir, frame_data, frame_number):
    filename = f"frame_{str(frame_number).zfill(3)}.jpg"
    filepath = os.path.join(session_dir, filename)

    with open(filepath, 'wb') as f:
        f.write(frame_data)

    return filepath, filename

def ensure_directories():
    os.makedirs(CAPTURES_DIR, exist_ok=True)
