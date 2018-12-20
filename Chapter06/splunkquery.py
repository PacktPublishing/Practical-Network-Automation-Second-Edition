import splunklib.client as client
import splunklib.results as results
import requests
import warnings
from urllib.parse import unquote
import json 
 
warnings.filterwarnings("ignore")
 
 
def run(urlencoded,resp):
    HOST = "splunkIP"
    PORT = 8089
    USERNAME= "abhishekratan"
    PASSWORD ="abhishekratan"
 
    # Create a Service instance and log in
    service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)
 
    kwargs_oneshot = {"earliest_time": "-30d@d",
                  "count": 10
                  }
 
 
 
 
    url = unquote(urlencoded)
    oneshotsearch_results = service.jobs.oneshot(url, **kwargs_oneshot)
    reader = results.ResultsReader(oneshotsearch_results)
    result=[]
    for item in reader:
        print(item)
        result.append(item)
    return_result=result
    result={"result":result}
    print(return_result)
    resp.body=json.dumps(result)
    return return_result
