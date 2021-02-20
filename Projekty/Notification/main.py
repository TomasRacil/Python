from moduls.notifie import *
from moduls.serverRequest import *
import time

data = serverRequest()
if data != None:
	lastDeath = data['deceased']
	notifie("Dosavadní počet úmrtí na Covid-19",data['deceased'])
	while True:
		time.sleep(600)
		data = serverRequest()
		if lastDeath < data['deceased']:
			notifie("Počet mrtvích na Covid-19 se zvýšil o",data['deceased']-lastDeath)
