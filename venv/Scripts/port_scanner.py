import socket 
from datetime import datetime

def scan_port(ip, port, timeout=1):
    """Check if a specific port is open on a device."""
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except socket.error:
        return False
    
def scan_device(ip, ports):
    """Scan a list of ports on a single device."""
    print(f'Port scan: {ip} - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print('-' * 40)

    for port in ports:
        status = 'OPEN' if scan_port(ip, port) else 'CLOSED'
        print(f'Port {port:<8} {status}')

    print('-' * 40)

target_ip = '127.0.0.1' #Own machine
common_ports = [80, 443, 22, 3389, 21, 8080]
scan_device(target_ip, common_ports)