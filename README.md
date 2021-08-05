# A simple tcp scanner

# How to use
./portscanner.py ips.txt ports.txt 
Where ips.txt is a list of ips to check one by line and ports.txt is a list os ports to check one by line

#Ex:
./portscanner.py ips.txt ports.txt 
Checking host 192.168.1.1 192.168.1.1
Port 80 [OPEN]
Port 443 [OPEN]
Port 53 [CLOSED]

Checking host 192.168.1.2 192.168.1.2
Port 80 [OPEN]
Port 443 [OPEN]
Port 53 [CLOSED]
