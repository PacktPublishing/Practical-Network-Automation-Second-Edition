import json
import requests
import base64
from splunk_alexa import alexa
channl=""
token=""
resp=""
def set_data(Channel,Token,Response):
    global channl,token,resp
    channl=Channel
    token=Token
    resp=Response

def send_data(text):
        global channl,token,res
        print(channl)
        resp = requests.post("https://slack.com/api/chat.postMessage",data='{"channel":"'+channl+'","text":"'+text+'"}',headers={"Content-type": "application/json","Authorization": "Bearer "+token},verify=False)

def channel_connect(text):
    global channl,token,resp
    try: 
        print(text)
        arg=text.split(' ')
        print(str(arg))
        path=arg[0].lower()
        print(path in ["decode","encode"])
        if path in ["decode","encode"]:
            print("deecode api")
        else:
            result=alexa(arg,resp)
            text=""
            try:
                for i in result:
                    print(i)
                    print(str(i.values()))
                    for j in i.values():
                        print(j)
                        text=text+' '+j
                        #print(j)
                if text=="" or text==None:
                    text="None"
                send_data(text)
                return
            except:
                text="None"
                send_data(text)
                return
        decode=arg[1]
    except:
        print("Please enter a string to decode")
        text="<decode> argument cannot be empty"
        send_data(text)
        return
    deencode(arg,text)

def deencode(arg,text):
    global channl,token,resp
    decode=arg[1]
    if arg[1]=='--help':
        #print("Sinput")
        text="encode/decode <encoded_string>"
        send_data(text)
        return
    if arg[0].lower()=="encode":
        encoded=base64.b64encode(str.encode(decode))
        if '[:]' in decode:
            text="Encoded string: "+encoded.decode('utf-8')
            send_data(text)
            return
        else:
            text="sample string format username[:]password"
            send_data(text)
            return
    try:
        creds=base64.b64decode(decode)
        creds=creds.decode("utf-8")
    except:
        print("problem while decoding String")
        text="Error decoding the string. Check your encoded string."
        send_data(text)
        return
    if '[:]' in str(creds):
        print("[:] substring exists in the decoded base64 credentials")
        # split based on the first match of "[:]"
        credentials = str(creds).split('[:]',1)
        username = str(credentials[0])
        password = str(credentials[1])
        status = 'success'
    else:
        text="encoded string is not in standard format, use username[:]password"
        send_data(text)
        print("the encoded base64 is not in standard format username[:]password")
        username = "Invalid"
        password = "Invalid"
        status = 'failed'
    temp_dict = {}
    temp_dict['output'] = {'username':username,'password':password}
    temp_dict['status'] = status
    temp_dict['identifier'] = ""
    temp_dict['type'] = ""
    #result.append(temp_dict)
    print(temp_dict)
    text="<username> "+username+" <password> "+password
    send_data(text)
    print(resp.text)
    print(resp.status_code)
    return
