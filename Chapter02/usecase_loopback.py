from netmiko import ConnectHandler
from threading import Thread
from pysnmp.entity.rfc3413.oneliner import cmdgen


cmdGen = cmdgen.CommandGenerator()
threads = []

def pushconfig(ip,interface):
        print ("\nConfiguring router %s now..." % (ip))
        device = ConnectHandler(device_type='cisco_ios', ip=ip, username='test', password='test')
        configcmds=["interface "+interface, "description "+interface+" test interface created"]
        device.send_config_set(configcmds)
        checkloopback45(ip,interface)
        
def checkloopback45(ip,interface):
     loopbackpresent=False
     cmdGen = cmdgen.CommandGenerator()
     errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
    cmdgen.CommunityData('mytest'),
    cmdgen.UdpTransportTarget((ip, 161)),
    0,25,
    '1.3.6.1.2.1.2.2.1.2'
    )
     for varBindTableRow in varBindTable:
        for name, val in varBindTableRow:
            if (interface in val.prettyPrint()):
                loopbackpresent=True
                break
     if loopbackpresent:
        print ("\nFor IP %s interface %s is present" % (ip,interface))
     else:
        print ("\nFor IP %s interface %s is NOT present. Pushing the config" % (ip,interface))
        pushconfig(ip,interface)
                
for n in range(1, 5):
 ip="192.168.20.{0}".format(n)
 t = Thread(target=checkloopback45, args= (ip,"Loopback45",))
 t.start()
 threads.append(t)

#wait for all threads to completed
for t in threads:
    t.join()
