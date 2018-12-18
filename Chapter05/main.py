import falcon
import json
import requests
import base64
from splunkquery import run
from splunk_alexa import alexa
from channel import channel_connect, set_data
from encodedecode import encode, decode
import jwt
from passlib.hash import pbkdf2_sha256

class Splunk():
    def on_post(self, req, resp):
        data = req.bounded_stream.read()
        try:
            useragent = json.loads(data)["ua"]
        except:
            useragent = "web"
        if useragent == "web":
            try:
                url = json.loads(data)["query"]
            except:
                resp.body = "Incorrect/No key present in your data"
                return
            run(url, resp)
            return
        elif useragent == "alexa":
            data = json.loads(data)["query"]
            alexa(data, resp)


class Encode():
    def on_post(self, req, resp):
        data = req.bounded_stream.read()
        try:
            data = json.loads(data)["encode"]
        except:
            print("Encode key is missing")
            resp.body = "encode key is missing"
            return
        encoded = encode(data).split(':')[1]
        resp.body = json.dumps({"encoded": encoded})


class Decode():
    def on_post(self, req, resp):
        data = req.bounded_stream.read()
        try:
            data = json.loads(data)["decode"]
        except:
            print("decode key is missing")
            resp.body = "decode key is missing"
            return
        decoded = decode(data)
        resp.body = json.dumps(decoded)


class GenerateToken():
    def on_post(self, req, resp):
        data = req.bounded_stream.read()
        try:
            uname = json.loads(data)["username"]
            passw = json.loads(data)["password"]
        except:
            print("key missing")
            resp.body = "username/password key is missing"
            return
        ##### Statically keep a token username and password for testing
        if uname.lower() != "john" and passw.lower() != "testpass":
            resp.body = json.dumps("Incorrect Username/Password")
            return
        hashed = pbkdf2_sha256.using(salt_size=12).hash("test")
        with open('token.txt', 'w') as f:
            f.write(hashed)
        resp.body = json.dumps({"token": hashed.split("29000$")[1]})


class TokenTest():
    def on_post(self, req, resp):
        data = req.bounded_stream.read()
        try:
            token = json.loads(data)["token"]
            token = "$pbkdf2-sha256$29000$" + token
        except:
            print("key token is missing")
            resp.body = "token 'key' is missing"
            return
        with open('token.txt', 'r') as f:
            token_old = f.read()
        if token == token_old:
            resp.body = json.dumps("Hello John!")
            return
        else:
            resp.body = json.dumps("Token does not exist")
            return


# falcon.API instance , callable from gunicorn
app = falcon.API()

# instantiate all classes
gentoken = GenerateToken()
Bot3V = Bot_BECJ82A3V()
splunk = Splunk()
encod = Encode()
decod = Decode()
tokentest = TokenTest()
# map URL to the respective classes for endpoint provisioning
app.add_route("/token/test", tokentest)
app.add_route("/token/generate", gentoken)
app.add_route("/decode", decod)
app.add_route('/encode', encod)
app.add_route("/splunk/runquery", splunk)

