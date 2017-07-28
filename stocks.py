import json
import urllib.request
from termcolor import colored

shouldExit = False

while not shouldExit:

    symbol = input('Enter a stock symbol (exit to quit): ')

    if symbol == 'exit':
        shouldExit = True

    response = urllib.request.urlopen('https://api.iextrading.com/1.0/stock/'+symbol+'/quote')

    json_response = response.read()
    json_data = json.loads(json_response)

    for key in json_data:
        print(colored(str(key) + ": ", 'red'), colored(str(json_data[key]), 'blue'))


print('PROGRAM EXITED')





