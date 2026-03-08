import urllib.request
import json
import os
from dotenv import load_dotenv
load_dotenv()
token=os.getenv("token")

print("ENTER THE USERNAME OF THE ACCOUNT:")
username=input()



req=urllib.request.Request(os.getenv("url"))#making an request 
req.add_header("Authorization",f"Bearer{token}")#adding headers in thre request

x=urllib.request.urlopen(url)#opening the url
data=x.read().decode("utf-8")#converting bytes into json

with open("parash.json", "w") as f:
    json.dump(json.loads(data),f)