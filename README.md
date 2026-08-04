# Python Port Scanner

A simple multithreaded TCP port scanner written in Python. This tool scans all TCP ports (1-65535) on a target host and reports the open ports.

> ⚠️ This project was created for learning Python networking and basic cybersecurity concepts.

---

## Features

- Scan all TCP ports (1-65535)
- Multithreaded scanning using `ThreadPoolExecutor`
- Automatic hostname resolution
- Displays scan start time
- Lists all discovered open ports
- Handles invalid hostnames gracefully
- Supports interruption using `Ctrl + C`

---

## Requirements

- Python 3.x

No external libraries are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ZygraXe/python-port-scanner.git
cd python-port-scanner
```

---

## Usage

```bash
python3 myportscanner.py <target>
```

Example:

```bash
python3 myportscanner.py scanme.nmap.org
```

or

```bash
python3 myportscanner.py 192.168.1.10
```

---

## Example Output

```
--------------------------------------------------
Scanning started...
Scanning 45.33.32.156
Scan started at 2026-07-18 14:20:05
--------------------------------------------------
22 is open
80 is open
443 is open

The open ports are [22, 80, 443]
```

---

## How It Works

1. Resolves the target hostname to an IP address.
2. Creates up to 100 worker threads.
3. Attempts a TCP connection to every port from **1 to 65535**.
4. Reports ports that successfully accept a connection.
5. Displays a summary of all open ports after the scan completes.

---

## Project Structure

```
.
├── myportscanner.py
├── README.md
└── LICENSE
```

---

## Limitations

- TCP Connect Scan only (`socket.connect_ex`)
- No UDP scanning
- No service/version detection
- No banner grabbing
- No OS detection
- No output file support

---

## Future Improvements

- Export results to TXT/JSON/XML
- Custom port ranges
- Banner grabbing
- Service detection
- UDP scanning
- Progress indicator
- Colored terminal output
- Command-line arguments using `argparse`

---

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.

Do **not** scan networks or systems without explicit permission.

The author is not responsible for any misuse of this software.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
