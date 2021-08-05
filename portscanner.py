#!/usr/bin/env python3

import socket
import sys

if len(sys.argv) < 3:  
    print("Error! Sintaxe: %s hosts_file ports_file" % sys.argv[0])
    sys.exit(1) 

socket.setdefaulttimeout(3)

try:
    host= open(sys.argv[1], 'r')
    port= open(sys.argv[2], 'r')
    hosts = host.readlines() 
    ports = port.readlines()
    host.close()
    port.close()
except:
    print('Fail! IO error')
    sys.exit(1)

for host_check in hosts:
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        tcp_host_check = host_check.rstrip('\n')

        try:
            dns = socket.gethostbyname(tcp_host_check)
        except socket.gaierror:
            print('Error when translating DNS name %s' %tcp_host_check)
            sys.exit(1)
        
        print("Checking host %s %s" %(tcp_host_check, dns))

        for port_check in ports:
            tcp_port_check = int(port_check.rstrip('\n'))

            if con.connect_ex((dns,tcp_port_check)): 
                print('Port %d [CLOSED]' % tcp_port_check)  
            else:
                print("Port %d [OPEN]" %   tcp_port_check)

        print('')
        con.close() 
