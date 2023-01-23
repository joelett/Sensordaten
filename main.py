import requests
import json

res = requests.get('https://api.sensor.community/v1/')
response = json.loads(res.text)

print("hello")