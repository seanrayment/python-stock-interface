import json
import urllib.request

response = urllib.request.urlopen('https://api.iextrading.com/1.0/stock/aapl/quote')
json_response = response.read()
print(json_response)