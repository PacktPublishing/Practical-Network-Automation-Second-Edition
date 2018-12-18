from netmiko import ConnectHandler
import os

template="""logging host 192.168.20.5 transport tcp port 514
logging trap 6
interface loopback 30
description "{rtr} loopback interface\""""

username = 'test'
password="test"

#step 1
#fetch the hostname of the router for the template
for n in range(1, 5):
    ip="192.168.20.{0}".format(n)
    device = ConnectHandler(device_type='cisco_ios', ip=ip, username='test', password='test')
    output = device.send_command("show run | in hostname")
    output=output.split(" ")
    hostname=output[1]
    generatedconfig=template.replace("{rtr}",hostname)

    #step 2
    #create different config files for each router ready to be pushed on routers.
    configfile=open(hostname+"_syslog_config.txt","w")
    configfile.write(generatedconfig)
    configfile.close()

#step3 (Validation)
#read files for each of the router (created as routername_syslog_config.txt)
print ("Showing contents for generated config files....")
for file in os.listdir('./'):
    if file.endswith(".txt"):
        if ("syslog_config" in file):
            hostname=file.split("_")[0]
            fileconfig=open(file)
            print ("\nShowing contents of "+hostname)
            print (fileconfig.read())
            fileconfig.close()
        

