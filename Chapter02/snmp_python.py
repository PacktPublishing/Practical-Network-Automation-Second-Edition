from pysnmp.hlapi import *

for n in range(1, 3):
    server_ip="192.168.20.{0}".format(n)
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData('mytest', mpModel=0),
               UdpTransportTarget((server_ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
    )
    print ("\nFetching stats for...", server_ip)
    for varBind in varBinds:
        print (varBind[1])
