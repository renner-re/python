
#!/usr/bin/python3

import socket
from tqdm import tqdm

def get_open_ports(target, port_range, verbose=True):
    open_ports = []

    try:
        # Check if IPv4 or IPv6 address
        family = socket.AF_INET6 if ":" in target else socket.AF_INET
        target_ip = socket.getaddrinfo(target, None, family)[0][4][0]
    except socket.gaierror:
        return "An error occurred contacting the host.\n"
 
    start_port, end_port = port_range
    
    for port in tqdm(range(start_port, end_port + 1), desc="Scanning ports"):
        sock = socket.socket(family, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()  
    return open_ports

if __name__ == "__main__":
    target = input("Enter website or IP Address (IPv4 or IPv6):\n")
    port_range = input("Enter a port range (e.g., 1-65535) or press Enter for default range 1-1024:\n")

    if not port_range:
        start_port, end_port = 1, 1024
    else:
        start_port, end_port = map(int, port_range.split('-'))

    open_ports = get_open_ports(target, (start_port, end_port))

    if isinstance(open_ports, str):
        print(open_ports)
    elif len(open_ports) == 0:
        print("No open ports found.")
    else:
        print("Open ports:", open_ports)
