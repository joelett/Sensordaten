import requests
import json

res = requests.get('https://https://archive.sensor.community/')
print(res.text)

#response = json.loads(res.text)

#print(response)