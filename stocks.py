import json
import urllib.request

response = urllib.request.urlopen('https://python.org')
html = response.read()