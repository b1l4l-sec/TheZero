from pyngrok import ngrok, conf
from config.banner import print_success, print_error, print_info, print_warning, Colors
from config.settings import SERVER_PORT

def start_ngrok_tunnel():
    print()
    print(f"{Colors.CYAN}{'='*64}{Colors.RESET}")
    print(f"{Colors.BOLD}  NGROK TUNNEL MANAGER{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*64}{Colors.RESET}")
    print()

    try:
        print_info("Initializing ngrok tunnel...")

        conf.get_default().region = 'us'

        public_url = ngrok.connect(SERVER_PORT, bind_tls=True)

        print()
        print_success("Tunnel established successfully!")
        print()
        print(f"  {Colors.BOLD}Local URL:{Colors.RESET}  http://localhost:{SERVER_PORT}")
        print(f"  {Colors.BOLD}Public URL:{Colors.RESET} {Colors.GREEN}{public_url}{Colors.RESET}")
        print()
        print_warning("Keep this terminal open to maintain the tunnel")
        print_info("Press Ctrl+C to stop the tunnel")
        print()

        try:
            import time
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print()
            print_info("Shutting down tunnel...")
            ngrok.disconnect(public_url)
            print_success("Tunnel closed")

    except Exception as e:
        print_error(f"Failed to start ngrok tunnel: {str(e)}")
        print_warning("Make sure ngrok is configured correctly")
        print_info("Visit https://ngrok.com for setup instructions")

    print()
    print_info("Press Enter to return to main menu...")
    input()
