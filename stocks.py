import json
import urllib.request
from termcolor import colored

response = urllib.request.urlopen('https://api.iextrading.com/1.0/stock/goog/quote')
json_response = response.read()
json_data = json.loads(json_response)

for key in json_data:
    print (colored(str(key) + ": ", 'red'), colored(str(json_data[key]), 'blue'))



