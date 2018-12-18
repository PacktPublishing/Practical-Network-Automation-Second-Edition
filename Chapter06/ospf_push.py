from netmiko import ConnectHandler
import time

ospfbaseconfig="""
router ospf 1
network 192.168.20.0 0.0.0.255 area 0
"""

###convert to a list to send to routers
ospfbaseconfig=ospfbaseconfig.split("\n")

def pushospfconfig(routerip,ospfbaseconfig):
    uname="test"
    passwd="test"
    device = ConnectHandler(device_type='cisco_ios', ip=routerip, username=uname, password=passwd)
    xcheck=device.send_config_set(ospfbaseconfig)
    print (xcheck)
    outputx=device.send_command("wr mem")
    print (outputx)
    device.disconnect()


def validateospf(routerip):
    uname="test"
    passwd="test"
    device = ConnectHandler(device_type='cisco_ios', ip=routerip, username=uname, password=passwd)
    cmds="show ip ospf neighbor"
    outputx=device.send_command(cmds)
    if ("FULL/" in outputx):
        print ("On router "+routerip+" neighborship is full")
    else:
        print ("On router "+routerip+" neighborship is not in FULL state")
    device.disconnect()

routers=['192.168.20.1','192.168.20.3']
for routerip in routers:
    pushospfconfig(routerip,ospfbaseconfig)
### we give some time for ospf to establish
print ("Now sleeping for 10 seconds....")
time.sleep(10) # 10 seconds

for routerip in routers:
    validateospf(routerip)


