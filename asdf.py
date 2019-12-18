# Import modules
import subprocess
import ipaddress
from tqdm import tqdm
import socket

def my_ip():
    if not socket.gethostbyname_ex(socket.gethostname())[2][0].startswith('127.'):
        return socket.gethostbyname_ex(socket.gethostname())[2]
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',53))
        return s.getsockname()[0]

# Prompt the user to input a network address
net_addr = input("Enter a network address in CIDR format(ex.192.168.1.0/24): ")

# Create the network
ip_net = ipaddress.ip_network(net_addr)

# Get all hosts on that network
all_hosts = list(ip_net.hosts())

#ping all networks on address
for i in tqdm(range(len(all_hosts)+1)):
    if all_hosts[i] != my_ip():
        p = subprocess.Popen(['ping', '-w', '1', str(all_hosts[i])], stdout=subprocess.PIPE).communicate()[0]

        if not '0 received' in p.decode('utf-8'):
            print(all_hosts[i])
    else: pass
