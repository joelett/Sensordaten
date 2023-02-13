import requests
import json
from datetime import date
import re

def initialGet(ddate):
    res = requests.get('https://archive.sensor.community/'+str(ddate.year)+'-'+f"{ddate.month:02d}"+'-'+f"{ddate.day-1:02d}"+'/')
    #res = requests.get('https://archive.sensor.community/2023-02-11/')
    print(re.search("<a href=\"(.+?)\">",str(res.content)))

initialGet(date.today())