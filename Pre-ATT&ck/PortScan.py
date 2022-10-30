#create a port scanner 

import socket

host = input("Enter the host to be scanned: ")

#translate a host name to IPv4 / WORKS WITH DNS TO! 
ip = socket.gethostbyname(host)
print("Starting scan on host: ", ip)

#create a list to add open ports to
open_ports = []

#scan ports between 1 and 1024
for port in range(1, 1024):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    #returns an error indicator
    result = s.connect_ex((ip, port))
    if result == 0:
        open_ports.append(port)
        print("Port {} is open".format(port))
    else: 
        print("Port {} is closed".format(port))
    s.close()

print("Open ports are: ", open_ports)


# Path: Pre-ATT&ck\PortScan.
