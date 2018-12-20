import falcon
import json
import requests
import base64
from splunkquery import run
from splunk_alexa import alexa
from channel import channel_connect,set_data
class Bot_BECJ82A3V():
    def on_get(self,req,resp):
        # Handles GET request
        resp.status=falcon.HTTP_200 # Default status
        resp.body=json.dumps({"Server is Up!"})
    def on_post(self,req,resp):
        # Handles POST Request
        print("In post")
        data=req.bounded_stream.read()
        try:
            bot_id=json.loads(data)["event"]["bot_id"]
            if bot_id=="BECJ82A3V":
                print("Ignore message from same bot")
                resp.status=falcon.HTTP_200
                resp.body=""
                return
        except:
            print("Life goes on. . .")
        try:
            # Aythenticating end point to Slack
            data=json.loads(data)["challenge"]
            # Default status
            resp.status=falcon.HTTP_200
            # Send challenge string back as response
            resp.body=data
        except:
            # URL already verified
            resp.status=falcon.HTTP_200
            resp.body=""
        print(data)
        data=json.loads(data)
        #Get the channel and data information
        channel=data["event"]["channel"]
        text=data["event"]["text"]
        # Authenticate Agent to access Slack endpoint
        token="xoxp-xxxxxx"
        # Set parameters
        print(type(data))
        print(text)
        set_data(channel,token,resp)
        # Proceess request and connect to slack channel
        channel_connect(text)
        return

# falcon.API instance , callable from gunicorn
app= falcon.API()

# instantiate helloWorld class
Bot3V=Bot_BECJ82A3V()
# map URL to helloWorld class
app.add_route("/slack",Bot3V)
