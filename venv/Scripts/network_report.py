import subprocess
import socket
from datetime import datetime

def ping_device(ip):
    result = subprocess.run(
    ['ping', '-n', '1', '-w', '1000', ip],
    capture_output=True,
    text=True
    )
    return result.returncode == 0

def scan_port(ip, port, timeout=1):
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except socket.error:
        return False
    
def generate_report(devices, ports):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'network_report_{timestamp}.txt'

    with open(filename, 'w') as f:
        f.write('=' * 50 + '\n')
        f.write(' IT DASHBOARD - NETWORK REPORT\n')
        f.write(f' Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        f.write('=' * 50 + '\n\n')

        f.write('DEVICE STATUS\n')
        f.write('-' * 30 + '\n')
        for ip in devices:
            status = 'ONLINE' if ping_device(ip) else 'OFFLINE'
            f.write(f'{ip:<20} {status}\n')

        f.write('\nPORT SCAN (127.0.0.1)\n')
        f.write('-' * 30 + '\n')
        for port in ports:
            status = 'OPEN' if scan_port('127.0.0.1', port) else 'CLOSED'
            f.write(f'Port {port:<8} {status}\n')

        f.write('\n' + '=' * 50 + '\n')
        f.write(' END OF REPORT\n' )
        f.write('-' * 50 + '\n')

    print(f'Report saved to: {filename}')

devices = [
    '127.0.0.1',
    '8.8.8.8',
    '192.168.1.1',
]

ports = [80, 443, 22, 3389, 8080]

generate_report(devices, ports)