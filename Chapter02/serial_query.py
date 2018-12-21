from netmiko import ConnectHandler
from datetime import datetime
startTime = datetime.now()

for n in range(1, 5):
 ip="192.168.20.{0}".format(n)
 device = ConnectHandler(device_type='cisco_ios', ip=ip, username='test', password='test')
 output = device.send_command("show run | in hostname")
 output=output.split(" ")
 hostname=output[1]
 print ("Hostname for IP %s is %s" % (ip,hostname))

print ("\nTotal execution time:")
print(datetime.now() - startTime)
