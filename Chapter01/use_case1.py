#As a travel agency, there are three customers registered with the agency.
#Ask is to provide a package for a city using the pre-defined preferences
#for any two customers. Additionally there needs to be a suggestion on
#weather for next seven days, and to provide an enhanced end user
#experience, ask a single question to determine check in time
#and type of transport for the journey.
#

import getpass 
import base64
import requests
from collections import Counter
import re


#ask for username .. will be displayed when typed
uname=input("Enter your username :")

#ask for password ... will not be displayed when typed
#(try in cmd or invoke using python command)
p = getpass.getpass(prompt="Enter your password: ")

#construct credential with *.* as separator between username and password
creds=uname+"*.*"+p

#encrypted creds of the registered customers
#for testing username:password is customer1:password1 , customer2:password2, and so on...

#create a dictionary:
customers={
    "customer1":b'Y3VzdG9tZXIxKi4qcGFzc3dvcmQx',
    "customer2":b'Y3VzdG9tZXIyKi4qcGFzc3dvcmQy',
    "customer3":b'Y3VzdG9tZXIzKi4qcGFzc3dvcmQz'
    }


###Decrypt a given set of credentials    
def decryptcredential(pwd):
    rvalue=base64.b64decode(pwd)
    rvalue=rvalue.decode()
    return rvalue

###Encrypt a given set of credentials
def encryptcredential(pwd):
  rvalue=base64.b64encode(pwd.encode())
  return rvalue

#to validate if a customer is legitimate
flag=True

### procedure for validated customer
def validatedcustomer(customer):
    print ("Hello "+customer)
    inputcity=input("Which city do you want to travel (ex London/Paris/Chicago): ")
    inputaddinfo=input("Any specific checkin time [AM/PM] and preferred mode of travel [car/bus]: ")

    #### extract the regex values from additional info
    regex=re.compile('\d+:\d+\s[AP]M')
    time=re.findall(regex,inputaddinfo)
    if "car" in inputaddinfo:
        transport="car"
    else:
        if "bus" in inputaddinfo:
            transport="bus"

    ### create sentence based upon the additional info provided
    print ("\n\nYou have selected to checkin at "+time[0]+", and your preferred transport will be "+transport+" .")
    
    getcityinfo=validatecity(inputcity)

    ### this is to sort the dictionary from highest to lowest based upon weather types
    sorted_d = [(k, getcityinfo[k]) for k in sorted(getcityinfo, key=getcityinfo.get, reverse=True)]
    
    ###iterate through the weathers to construct a sentence
    sentence="Weather prediction for next 5 days is (chance of) "
    for item in sorted_d:
        sentence=sentence+" "+item[0]+": "+str(item[1])+"%,"
    print (sentence)
    
    
### to validate the average weather for that city for next 5 days
def validatecity(inputcity):
    #create empty list
    weathers=[]
    weatherpercentage={}
    #remove any additional spaces accidently entered
    inputcity=inputcity.strip()
    urlx="https://samples.openweathermap.org/data/2.5/forecast?q="+inputcity+"&appid=b6907d289e10d714a6e88b30761fae22"
    #send the request to URL using GET Method
    r = requests.get(url = urlx)
    output=r.json()
    ### this is to parse the type of weather and count them in a list
    for item in output['list']:
        weathers.append(item['weather'][0]['description'])
    countweather=Counter(weathers)
    #### this is to find the percentage of each weather type from the given output (36 variations are returned from API)
    for item in countweather:
        weatherpercentage[item]=int((countweather[item]/36) * 100)
    return weatherpercentage        
    
### validate if the username is part of any customers
if (uname in customers):
    encryptedcreds=encryptcredential(creds)
    getcustomercreds=customers[uname]
    ### validate if the credentials provided is the same as stored credentials for that customer
    if not(str(encryptedcreds.decode()) == str(getcustomercreds.decode())):
        flag=False
else:
    flag=False
    

if not(flag):
    print ("Unauthorized customer.")
else:
    validatedcustomer(uname)
