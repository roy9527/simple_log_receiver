import requests
from flask import json

values={'id':'111','title':'test','pwd':'AZD123DFA'}
headers = {'content-type': 'application/json',"Accept": "application/json"}
r = requests.post('http://localhost:5000/log/upload_log',headers={'Content-Type': 'application/json'}, data=json.dumps(values))
print(r.text)