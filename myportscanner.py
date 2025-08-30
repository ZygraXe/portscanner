#!/usr/bin/python3

import sys
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

def i_scan(target, port):
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(1)
		result = s.connect_ex((target,port))
		if result ==0:
			return port
		s.close()
	except:
		pass
	return None

def main():
	if len(sys.argv)!=2:
		print("syntax error \n syntax:python3 myportscanner.py target")
		sys.exit(1)
	target=sys.argv[1]
	try:
		target_ip = socket.gethostbyname(target)
	except socket.gaierror:
        	print(f"Error: Unable to resolve hostname {target}")
        	sys.exit(1)

	print(50*'-')
	print("Scanning started...")
	print(f"Scanning {target_ip}")
	print(f"Scan started at {datetime.now()}")
	print(50*'-')

	open_ports = []
	try:
		with ThreadPoolExecutor(max_workers=100) as executor:
			futures = [executor.submit(i_scan, target_ip, port) for port in range (1,65536)]
			for f in as_completed(futures):
				port = f.result()
				if port:
					print(f"{port} is open")
					open_ports.append(port)
	except KeyboardInterrupt:
		print("The scan was interrupted")
		sys.exit(0)
	if open_ports:
		print(f"The open ports are {open_ports}")
	else:
		print("No open port found")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("The scan got interrupted")
		sys.exit(0)

