import requests
import urllib


endpoint="endpointip"

def generatetoken(uname,password):
        url="http://"+endpoint+"/token/generate"
        payload ='{"username":"'+uname+'","password":"'+password+'"}'
        print (payload)
        r = requests.post(url = url, data=payload)
        output=r.json()
        print (output)
        

##### A user has already been registered with password 'testpass'
print ("\nScenario 1: Provide INCorrect username and password combination to generate token")
generatetoken("abhishek","testpass123")

print ("\nScenario 2: Provide Correct username and password combination to generate token")
generatetoken("John","testpass")



