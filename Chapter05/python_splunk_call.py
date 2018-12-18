import requests
import urllib


endpoint="endpointip"

#Splunk query : index="main" earliest=0 | where interface_name="Loopback45" | dedup interface_name,router_name
#| where interface_status="up" | stats values(interface_name) values(interface_status) by router_name | table router_name

def getresult(query):
        url="http://"+endpoint+"/splunk/runquery"
        payload ='{"query":"'+query+'"}'
        r = requests.post(url = url, data=payload)
        output=r.json()
        print (output)



###pass the Splunk query in encoded URL format
getresult("""search%20index%3D%22main%22%20earliest%3D0%20%7C%20where%20interface_name%3D%22Loopback45%22%20%7C%20dedup%20interface_name%2Crouter_name%20%7C%20where%20interface_status%3D%22up%22%20%7C%20stats%20values%28interface_name%29%20values%28interface_status%29%20by%20router_name%20%7C%20table%20router_name""")


