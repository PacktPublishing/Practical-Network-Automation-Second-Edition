from netmiko import ConnectHandler
from datetime import datetime
from threading import Thread

startTime = datetime.now()

threads = []
def checkparallel(ip):
     device = ConnectHandler(device_type='cisco_ios', ip=ip, username='test', password='test')
     output = device.send_command("show run | in hostname")
     output=output.split(" ")
     hostname=output[1]
     print ("\nHostname for IP %s is %s" % (ip,hostname))
    
for n in range(1, 5):
 ip="192.168.20.{0}".format(n)
 t = Thread(target=checkparallel, args= (ip,))
 t.start()
 threads.append(t)

#wait for all threads to completed
for t in threads:
    t.join()


print ("\nTotal exection time:")
print(datetime.now() - startTime)
