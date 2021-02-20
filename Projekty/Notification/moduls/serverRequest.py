import requests
import json

def serverRequest():
	try:
		r = requests.get('https://api.apify.com/v2/key-value-stores/K373S4uCFR9W1K8ei/records/LATEST?disableRedirect=true')
	except:
		print('Nelze se připojit k serveru')
		r = None
	return json.loads(r.text)