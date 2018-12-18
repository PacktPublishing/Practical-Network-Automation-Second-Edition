from netmiko import ConnectHandler

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
    #push the generated config on router
    #create a list for generateconfig
    generatedconfig=generatedconfig.split("\n")
    device.send_config_set(generatedconfig)

    #step 3:
    #perform validations
    print ("********")
    print ("Performing validation for :",hostname+"\n")
    output=device.send_command("show logging")
    if ("encryption disabled, link up"):
        print ("Syslog is configured and reachable")
    else:
        print ("Syslog is NOT configured and NOT reachable")
    if ("Trap logging: level informational" in output):
        print ("Logging set for informational logs")
    else:
        print ("Logging not set for informational logs")

    print ("\nLoopback interface status:")
    output=device.send_command("show interfaces  description | in loopback interface")
    print (output)
    print ("************\n")


