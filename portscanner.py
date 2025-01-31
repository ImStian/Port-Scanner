import pyfiglet
import sys
import socket
import threading
from datetime import datetime
from tqdm import tqdm  # Import tqdm for progress bar

# Display banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Defining a target
if len(sys.argv) != 2:
    print("Invalid amount of Argument")
    print("Usage: python script_name.py <target>")
    sys.exit()

# Translate hostname to IPv4
try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Invalid hostname provided. Could not resolve.")
    sys.exit()

input('Press Enter to start scanning...')
print("\033[F\033[K", end="")  # Moves cursor up one line and clears it


# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

open_ports = []  # List to store open ports
lock = threading.Lock()  # Lock to protect shared resources
total_ports = 49151  # Total number of ports to scan (1-49151)

def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)  # Set timeout for faster scanning
        if s.connect_ex((target, port)) == 0:  # Check if port is open
            with lock:  # Use lock to append safely to open_ports list
                open_ports.append(port)

def scan_ports():
    threads = []
    # Create a tqdm progress bar, with the total number of ports
    with tqdm(total=total_ports, desc="Scanning ports", unit="port") as pbar:
        for port in range(1, total_ports + 1):
            thread = threading.Thread(target=scan_port, args=(port,))
            threads.append(thread)
            thread.start()

            # Update progress bar after starting each thread
            pbar.update(1)

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

    print("Scanning Completed at: " + str(datetime.now()))
    print("Open Ports: ", open_ports)

def grab_banner(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)  # Give the service time to respond
            s.connect((target, port))
            s.send(b"Hello\r\n") # sending generic request
            banner = s.recv(1024)  # Try to grab response
            print(f"Port {port} banner: {banner.decode().strip()}")
    except:
        print(f"Port {port} open but no banner received.")

def grab_banners_for_open_ports():
    input('Press Enter to start banner grabbing...')
    # Grab banner for each open port
    for port in open_ports:
        grab_banner(target, port)

# Run the port scanning function
scan_ports()

# Start banner grabbing after scanning
grab_banners_for_open_ports()
