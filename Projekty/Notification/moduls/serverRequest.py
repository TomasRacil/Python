import requests
import json

def serverRequest():
	try: 
		#funkce se pokusi ziskat data ze serveru
		r = requests.get('https://api.apify.com/v2/key-value-stores/K373S4uCFR9W1K8ei/records/LATEST?disableRedirect=true')
	except:
		#pokovad se to nepovede vypise zpravu
		print('Nelze se připojit k serveru')
		r = None
	return json.loads(r.text)