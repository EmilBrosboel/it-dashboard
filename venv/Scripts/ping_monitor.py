import subprocess
from datetime import datetime 

def ping_device(ip):
    """Ping a single IP address. Returns True if online, False if offline."""
    result = subprocess.run(
        ['ping', '-n', '1', 'w', '1000', ip],
        capture_output=True,
        text=True
    )
    return result.returncode == 0

def scan_network(ip_list):
    """Ping a list of IP addresses and print the results."""
    print(f'Network scan - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print('-' * 40)

    for ip in ip_list:
        status = 'ONLINE' if ping_device(ip) else 'OFFLINE'
        print(f'{ip:<20} {status}')

    print('-' * 40)

devices = [
    '192.168.1.218',
    '8.8.8.8',
    '192.168.1.1',
    '192.168.1.99',
]

scan_network(devices)