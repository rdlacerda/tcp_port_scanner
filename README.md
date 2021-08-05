# A simple tcp scanner

# How to use
./portscanner.py ips.txt ports.txt <br>
Where ips.txt is a list of ips to check one by line and ports.txt is a list os ports to check one by line <br>

# Ex:
./portscanner.py ips.txt ports.txt <br>
Checking host 192.168.1.1 192.168.1.1 <br>
Port 80 [OPEN] <br>
Port 443 [OPEN] <br>
Port 53 [CLOSED] <br>

Checking host 192.168.1.2 192.168.1.2 <br>
Port 80 [OPEN] <br>
Port 443 [OPEN] <br>
Port 53 [CLOSED] <br>
