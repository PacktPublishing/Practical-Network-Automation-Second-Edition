import base64
  
def encode(data):
    encoded=base64.b64encode(str.encode(data))
    if '[:]' in data:
        text="Encoded string: "+encoded.decode('utf-8')
        return text
    else:
        text="sample string format username[:]password"
        return text
    return encoded
def decode(data):
    try:
        decoded=base64.b64decode(data)
        decoded=decoded.decode('utf-8')
    except:
        print("problem while decoding String")
        text="Error decoding the string. Check your encoded string."
        return text
    if '[:]' in str(decoded):
        print("[:] substring exists in the decoded base64 credentials")
        # split based on the first match of "[:]"
        credentials = str(decoded).split('[:]',1)
        username = str(credentials[0])
        password = str(credentials[1])
        status = 'success'
    else:
        text="encoded string is not in standard format, use username[:]password"
        return text
    temp_dict = {}
    temp_dict = {'username':username,'password':password}
    return temp_dict
