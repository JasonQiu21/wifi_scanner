import socket
import subprocess
import ipaddress
from tqdm import tqdm
from getmac import get_mac_address


def my_ip():
    if not socket.gethostbyname_ex(socket.gethostname())[2][0].startswith('127.'):
        return socket.gethostbyname_ex(socket.gethostname())[2]
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',53))
        return s.getsockname()[0]


def get_ips():
    ips = []
    #generate list of ips to ping
    net_addr = '192.168.1.0/24' #change if your local network is formatted differently
    ip_net = ipaddress.ip_network(net_addr)
    all_hosts = list(ip_net.hosts())

    print("pinging ips...")
    #ping said ips
    for i in tqdm(range(len(all_hosts))):
        if str(all_hosts[i]) != my_ip():
            p = subprocess.Popen(['ping', '-c', '1', '-w', '1', str(all_hosts[i])], stdout=subprocess.PIPE).communicate()[0]

            if not '0 received' in p.decode('utf-8'):
                ips.append(str(all_hosts[i]))
        else: pass
    return ips

for i in get_ips():
    print(f'IP: {i}', end = ', ')
    print(f'MAC: {get_mac_address(ip=i)}')