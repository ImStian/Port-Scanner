# Port Scanner

A multi-threaded Python port scanner that scans a target for open ports and attempts to grab banners from the detected open ports. Uses `tqdm` for a progress bar and `pyfiglet` for a banner display.

## Features
- Multi-threaded scanning for efficiency
- Scans up to 49,151 ports
- Displays progress using a progress bar (`tqdm`)
- Attempts to grab banners from open ports
- Displays a clear output with start and end timestamps

## Prerequisites
Ensure you have the following Python packages installed:
```sh
pip install tqdm pyfiglet
```

## Usage
Run the script with a target hostname or IP address:
```sh
python portscanner.py <target>
```
Replace `<target>` with the domain name or IP address of the target system.

### Example
```sh
python portscanner.py example.com
```

## How It Works
1. Translates the provided hostname into an IPv4 address.
2. Initiates a multi-threaded scan of ports 1-49151.
3. Displays a progress bar while scanning.
4. Lists open ports at the end of the scan.
5. Allows the user to proceed with banner grabbing on detected open ports.

## Output Example
```
PORT SCANNER
--------------------------------------------------
Scanning Target: 192.168.1.1
Scanning started at: 2025-01-31 12:00:00
--------------------------------------------------
Scanning ports: 100%|██████████| 49151/49151 [00:30<00:00, 1615.6 ports/s]
Scanning Completed at: 2025-01-31 12:00:30
Open Ports: [22, 80, 443]

Press Enter to start banner grabbing...
Port 22 banner: OpenSSH 8.2p1 Ubuntu-4ubuntu0.5
Port 80 banner: Apache/2.4.41 (Ubuntu)
Port 443 open but no banner received.
```

## Notes
- This script is intended for educational and security research purposes only. Do not use it on systems without explicit permission.
- Increasing the number of threads can speed up scanning but may cause false negatives due to connection timeouts.

## License
This project is licensed under the MIT License.

## Disclaimer
Use this tool responsibly. Unauthorized scanning of networks or devices may be illegal and against terms of service agreements.

