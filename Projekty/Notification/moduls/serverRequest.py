import requests
import json

"""
funkce se pokusi ziskat data z api serveru
data ziska ve forme javascript objektu
a pak je prevede na python list
"""
def serverRequest():
	try:
		r = requests.get('https://api.apify.com/v2/key-value-stores/K373S4uCFR9W1K8ei/records/LATEST?disableRedirect=true')
	except:
		#pokovad se request nepovede vypise zpravu
		print('Nelze se připojit k serveru')
		r = None
	return json.loads(r.text)