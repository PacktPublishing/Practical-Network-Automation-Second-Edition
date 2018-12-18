import requests
import urllib


endpoint="endpoint ip address"

def getencode(query):
        url="http://"+endpoint+"/encode"
        payload ='{"encode":"'+query+'"}'
        r = requests.post(url = url, data=payload)
        output=r.json()
        for value in output.values():
            encodedvalue=value
        return encodedvalue

def getdecode(encodedstring):
        url="http://"+endpoint+"/decode"
        payload ='{"decode":"'+encodedstring+'"}'
        r = requests.post(url = url, data=payload)
        output=r.json()
        print (output)

encodedvalue=getencode("abhishek[:]password")
print (encodedvalue)

getdecode(encodedvalue)


