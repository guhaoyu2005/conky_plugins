#!/usr/bin/env python3
#
# Conky catfact plugin
# 
import sys
import json
import urllib.request
import traceback    

DATA_URL = 'https://catfact.ninja/fact'
DATA_API = ''

try:
    data_url = DATA_URL + DATA_API
    data = urllib.request.urlopen(url=data_url)
    data = json.load(data)
except:
    #print(traceback.format_exc())
    print("(˵Φ ω Φ˵)")
    exit(0)

if int(data['length']) == len(data['fact']):
    print(data['fact'])
else:
    print("(˵Φ ω Φ˵)")
