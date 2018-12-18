import requests
from orionsdk import SwisClient
npm_server = 'npm_serverip'
username = 'test'
password = 'test123'
verify = False
if not verify:
 from requests.packages.urllib3.exceptions import InsecureRequestWarning
 requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
swis = SwisClient(npm_server, username, password)

keyvalue="mytestrouter"
results = swis.query("SELECT Caption AS NodeName, IPAddress FROM Orion.Nodes WHERE NodeName =@id",id=keyvalue)
if results['results'] == []:
 print("query didn't return any output. node might not be present in SolarWinds DataBase")
else:
 uri = results['results'][0]['IPAddress']
 print (uri)

