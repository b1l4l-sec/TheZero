import json
from datetime import datetime
from utils.file_handler import create_session_directory, save_metadata

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, session_id, ip_address='unknown', user_agent='unknown'):
        session_dir = create_session_directory(session_id)

        metadata = {
            'session_id': session_id,
            'start_time': datetime.now().isoformat(),
            'ip_address': ip_address,
            'user_agent': user_agent,
            'frames_captured': 0
        }

        save_metadata(session_dir, metadata)

        self.sessions[session_id] = {
            'directory': session_dir,
            'metadata': metadata,
            'frame_count': 0
        }

        return session_dir

    def get_session(self, session_id):
        return self.sessions.get(session_id)

    def update_frame_count(self, session_id):
        if session_id in self.sessions:
            self.sessions[session_id]['frame_count'] += 1
            return self.sessions[session_id]['frame_count']
        return 0

    def end_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]
