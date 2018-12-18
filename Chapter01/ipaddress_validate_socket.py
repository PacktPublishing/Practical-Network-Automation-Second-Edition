import socket

addr=input("Enter IP address: ")

try:
    socket.inet_aton(addr)
    print ("IP address is valid")
except socket.error:
    print ("IP address is NOT valid")
