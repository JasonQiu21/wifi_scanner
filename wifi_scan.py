import nmap
import sys
import socket
from getmac import get_mac_address

def my_ip():
    if not socket.gethostbyname_ex(socket.gethostname())[2][0].startswith('127.'):
        return socket.gethostbyname_ex(socket.gethostname())[2]
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',53))
        return s.getsockname()[0]


nm = nmap.PortScanner()
nm.scan(hosts='192.168.1.0/24', arguments='-sn')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
hosts_list.remove((str(my_ip()), 'up'))
for host, i in hosts_list:
    print(f'IP: {host}', end = ', ')
    print(f'MAC: {get_mac_address(ip=str(host))}')
