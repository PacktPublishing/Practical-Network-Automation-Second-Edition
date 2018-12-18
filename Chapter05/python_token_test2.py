import requests
import urllib

endpoint="testip"

def authenticatetoken(token):
        url="http://"+endpoint+"/token/test"
        payload ='{"token":"'+token+'"}'
        print (payload)
        r = requests.post(url = url, data=payload)
        output=r.json()
        print (output)
        

##### A user has already been registered with password 'testpass'

print ("\nScenario 1: Validating incorrect token   ....")
authenticatetoken("rpXS2rtGGGGGaq2V0jqH$WNC2NCjHJe3BmMy.Wylq7eubA52Yj7UhCkDTQqv6nCM")

print ("\nScenario 2: Validating right token...")
authenticatetoken("rpXS2rtXaq2V0jqH$WNC2NCjHJe3BmMy.Wylq7eubA52Yj7UhCkDTQqv6nCM")






