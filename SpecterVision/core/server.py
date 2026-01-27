import os
import base64
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import datetime
from core.session_manager import SessionManager
from utils.file_handler import get_next_frame_number, save_frame, ensure_directories
from utils.logger import logger
# Added print_warning to the import list below:
from config.banner import print_success, print_error, print_info, print_warning, Colors
from config.settings import SERVER_HOST, SERVER_PORT

app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
            static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'))
CORS(app)

session_manager = SessionManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'online',
        'timestamp': datetime.now().isoformat(),
        'active_sessions': len(session_manager.sessions)
    })

@app.route('/upload_frame', methods=['POST'])
def upload_frame():
    try:
        data = request.get_json()

        session_id = data.get('session_id')
        timestamp = data.get('timestamp')
        frame_data = data.get('frame_data')
        mode = data.get('mode', 'standard')

        if not session_id or not frame_data:
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400

        session = session_manager.get_session(session_id)
        if not session:
            ip_address = request.remote_addr
            user_agent = request.headers.get('User-Agent', 'unknown')
            session_dir = session_manager.create_session(session_id, ip_address, user_agent)
            logger.info(f"New session created: {session_id} from {ip_address}")
        else:
            session_dir = session['directory']

        if frame_data.startswith('data:image'):
            frame_data = frame_data.split(',')[1]

        frame_bytes = base64.b64decode(frame_data)

        frame_number = get_next_frame_number(session_dir)

        filepath, filename = save_frame(session_dir, frame_bytes, frame_number)

        session_manager.update_frame_count(session_id)

        print(f"  {Colors.GREEN}[CAPTURE]{Colors.RESET} Session: {session_id[:20]}... | Frame: {Colors.CYAN}{frame_number}{Colors.RESET} | Mode: {mode}")

        logger.info(f"Frame captured: {filename} for session {session_id}")

        return jsonify({
            'success': True,
            'frame_number': frame_number,
            'filename': filename,
            'filepath': filepath,
            'timestamp': timestamp
        })

    except Exception as e:
        logger.error(f"Error uploading frame: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

def run_server():
    ensure_directories()

    print()
    print(f"{Colors.CYAN}{'='*64}{Colors.RESET}")
    print(f"{Colors.BOLD}  FLASK WEB SERVER{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*64}{Colors.RESET}")
    print()

    print_info("Starting Flask server...")
    print()
    print(f"  {Colors.BOLD}Server Address:{Colors.RESET} http://localhost:{SERVER_PORT}")
    print(f"  {Colors.BOLD}Status:{Colors.RESET}        {Colors.GREEN}RUNNING{Colors.RESET}")
    print()
    print_warning("Keep this terminal open while using the application")
    print_info("Press Ctrl+C to stop the server")
    print()
    print(f"{Colors.CYAN}{'='*64}{Colors.RESET}")
    print()

    try:
        app.run(host=SERVER_HOST, port=SERVER_PORT, debug=False, use_reloader=False)
    except KeyboardInterrupt:
        print()
        print_info("Shutting down server...")
        print_success("Server stopped")
    except Exception as e:
        print_error(f"Server error: {str(e)}")

if __name__ == '__main__':
    run_server()
