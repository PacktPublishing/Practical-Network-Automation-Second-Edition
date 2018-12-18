import splunklib.client as client
import splunklib.results as results
import requests
import warnings
from urllib.parse import unquote
from netmiko import ConnectHandler

warnings.filterwarnings("ignore")

HOST = "52.163.189.222"
PORT = 8089
USERNAME= "username"
PASSWORD ="password"

###mapping of routers to IPs
device_name={}
device_name['rtr1']="192.168.20.1"
device_name['rtr2']="192.168.20.2"
device_name['rtr3']="192.168.20.3"
device_name['rtr4']="192.168.20.4"

print (device_name)

# Create a Service instance and log in 
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

kwargs_oneshot = {"earliest_time": "-120d@d",
                  "count": 10
                  }

url="""search index="main" | where interface_name="Loopback45" | dedup interface_name,router_name | stats values(interface_name) values(interface_status) by router_name"""
#url = unquote(urlencoded)
#oneshotsearch_results = service.jobs.oneshot(searchquery_oneshot, **kwargs_oneshot)

oneshotsearch_results = service.jobs.oneshot(url, **kwargs_oneshot)

# Get the results and display them using the ResultsReader
reader = results.ResultsReader(oneshotsearch_results)
for item in reader:
    if ("up" not in item['values(interface_status)']):
        print ("\nIssue found in %s " % (item['router_name']))
        print ("Remediation in progress....")
        device = ConnectHandler(device_type='cisco_ios', ip=device_name[item['router_name']], username='test', password='test')
        remediateconfig=["interface loopback 45", "no shut"]
        device.send_config_set(remediateconfig)

        ### validate if interface is now up (this is where we can add additional actions like notifications ,etc
        output = device.send_command("show interfaces loopback 45")
        if ("line protocol is up" in output):
            print ("Remediation succeeded. Interface is now back to normal")
        else:
            print ("Remdiation Failed. Need to manually validate\n")
