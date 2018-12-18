import socket

def getfromhostname(hostname):
    print ("AS info for hostname :"+hostname)
    ip = socket.gethostbyname(hostname)
    from cymruwhois import Client
    c=Client()
    r=c.lookup(ip)
    print (r.asn)
    print (r.owner)

def getfromip(ip):
    print ("AS info for IP : "+ip)
    from cymruwhois import Client
    c=Client()
    r=c.lookup(ip)
    print (r.asn)
    print (r.owner)


getfromhostname("microsoft.com")
getfromip("216.58.192.14")
