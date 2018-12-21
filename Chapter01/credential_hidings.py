import getpass 
import base64
#ask for username .. will be displayed when typed
uname=input("Enter your username :")

#ask for password ... will not be displayed when typed
#(try in cmd or invoke using python command)
p = getpass.getpass(prompt="Enter your password: ")

#construct credential with *.* as seperator between username and password
creds=uname+"*.*"+p

###Encrypt a given set of credentials
def encryptcredential(pwd):
  rvalue=base64.b64encode(pwd.encode())
  return rvalue

###Decrypt a given set of credentials    
def decryptcredential(pwd):
    rvalue=base64.b64decode(pwd)
    rvalue=rvalue.decode()
    return rvalue


encryptedcreds=encryptcredential(creds)

print ("Simple creds: "+creds)
print ("Encrypted creds: "+str(encryptedcreds))
print ("Decrypted creds: "+decryptcredential(encryptedcreds))



