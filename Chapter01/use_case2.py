#As an admin, you need to provide a script to users to add/delete themselves based upon
#authentication status and if authenticated successfully, provide an option to change their passwords.

import getpass 
import base64
import os.path

###Check with credential storage file exists. Ifnot, then create one, otherwise read data from the current file
storedcreds=[]
if (os.path.isfile("usecase_creds.txt")):
    fopen=open("usecase_creds.txt")
    storedcreds=fopen.readlines()
else:
    fopen=open("usecase_creds.txt","w")


###Decrypt a given set of credentials    
def decryptcredential(pwd):
    rvalue=base64.b64decode(pwd)
    rvalue=rvalue.decode()
    return rvalue

###Encrypt a given set of credentials
def encryptcredential(pwd):
  rvalue=base64.b64encode(pwd.encode())
  return rvalue

#### this is used to deregister a authenticated user
def deregister(getencryptedcreds):
    with open("usecase_creds.txt") as f:
        newText=f.read().replace(getencryptedcreds+"\n","")

    with open("usecase_creds.txt", "w") as f:
        f.write(newText)
    print ("you are deregistered")
    
#this is to store the read encrypted creds from file into expanded username and password combo
storedcredsexpanded=[]
for item in storedcreds:
    item=item.strip()
    #to ensure we do not parse the blank values or blank lines
    if (len(item) > 2):
        tmpval=decryptcredential(item)
        storedcredsexpanded.append(tmpval)

#ask for username .. will be displayed when typed
uname=input("Enter your username :")

#ask for password ... will not be displayed when typed
#(try in cmd or invoke using python command)
p = getpass.getpass(prompt="Enter your password: ")

#construct credential with *.* as separator between username and password
creds=uname+"*.*"+p

#encrypted creds of the registered customers
#for testing username:password is customer1:password1 , customer2:password2, and so on...
getencryptedcreds=encryptcredential(creds)

#vlidate authentication of user
flag=False
usrauthenticated=False
for item in storedcreds:
    if (getencryptedcreds.decode() in item):
        flag=True


if (flag):
    print ("Authenticated successfully")
    usrauthenticated=True
else:
    print ("Authentication failed")
    #validate if user exists
    tmpvalue=decryptcredential(getencryptedcreds)
    #split username and password
    tmpvalue=tmpvalue.split("*.*")
    usrflag=False
    ###validate if this username exists otherwise give an option for new registration
    for item in storedcredsexpanded:
        item=item.split("*.*")
        if (tmpvalue[0] == item[0]):
            print ("User already exists but password incorrect. Please contact Admin for password reset")
            usrflag=True
            break

    #if user does not exist
    if (usrflag==False):
            readinput=input("User does not exist, Do you want to register yourself (Y/N) ")
            readinput=readinput.strip()
            readinput=readinput.lower()
            if (readinput == "y"):
                uname=input("Enter your username :")
                p = getpass.getpass(prompt="Enter your password: ")
                creds=uname+"*.*"+p
                getencryptedcreds=encryptcredential(creds)
                ## to convert bytes to string
                getencryptedcreds=getencryptedcreds.decode()

                ##open file in append mode
                fopen=open("usecase_creds.txt","a")
                fopen.write(getencryptedcreds+"\n")
                fopen.close()
                print ("User added successfully")


if (usrauthenticated):
    readinput=input("Do you want to deregister yourself (Y/N) ")
    readinput=readinput.strip()
    readinput=readinput.lower()
    if (readinput == "y"):
        deregister(getencryptedcreds.decode())
    else:
        readinput=input("Do you want to change your password (Y/N) ")
        readinput=readinput.strip()
        readinput=readinput.lower()
        if (readinput == "y"):
            p = getpass.getpass(prompt="Enter your password: ")
            creds=uname+"*.*"+p
            newencryptedcreds=encryptcredential(creds)
            newencryptedcreds=newencryptedcreds.decode()
            getencryptedcreds=getencryptedcreds.decode()

            ###updated the credential of the user
            with open("usecase_creds.txt") as f:
                newText=f.read().replace(getencryptedcreds, newencryptedcreds)

            with open("usecase_creds.txt", "w") as f:
                f.write(newText)
            print ("Your password is updated successfully")
            
