import requests
from flask import json

values={'id':'111','title':'test','pwd':'AZD123DFA'}
headers = {'content-type': 'application/json',"Accept": "application/json", 'user-agent':'test android', 'Range': 'bytes=20480-'}
# r = requests.post('http://localhost:8000/log/upload_log',headers=headers, data=json.dumps(values))
r = requests.get('http://127.0.0.1:8000/log/get_file',stream=True, headers=headers, data=json.dumps(values))
# print(r.text)
with open("a.zip", "wb") as code:
     code.write(r.content)