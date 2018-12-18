from netmiko import ConnectHandler
from threading import Thread
from pysnmp.entity.rfc3413.oneliner import cmdgen


cmdGen = cmdgen.CommandGenerator()
threads = []


def pushconfig(ip,interface,description):
    print ("\nUpdating the config on "+ip)
    device = ConnectHandler(device_type='cisco_ios', ip=ip, username='test', password='test')
    configcmds=["interface "+interface, "description "+interface+" "+description]
    device.send_config_set(configcmds)
    checkloopback45(ip,interface)
    
def checkloopback45(ip,interface):
     loopbackpresent=False
     cmdGen = cmdgen.CommandGenerator()
     errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
    cmdgen.CommunityData('mytest'),
    cmdgen.UdpTransportTarget((ip, 161)),
    0,25,
    '1.3.6.1.2.1.31.1.1.1.18','1.3.6.1.2.1.2.2.1.2','1.3.6.1.2.1.31.1.1.1.1'
    )
     for varBindTableRow in varBindTable:
        tval=""
        for name, val in varBindTableRow:
            if (("Loopback45" in str(val)) or ("Lo45" in str(val))):
                tval=tval+"MIB: "+str(name)+" , Interface info: "+str(val)+"\n"
                loopbackpresent=True
            
        if (loopbackpresent):
            tval=tval+"IP address of the device: "+ip
            print (tval+"\n")
            if ("test interface created" in tval):
                pushconfig(ip,"Loopback45","Mgmt loopback interface")

                

checkloopback45("192.168.20.1","Loopback45")
