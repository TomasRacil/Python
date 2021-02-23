from moduls.notifie import *
from moduls.serverRequest import *
import time

data = serverRequest() #fukce nacte a vrati data ze serveru 
if data != None:
	lastDeath = data['deceased'] #vytahneme z dat pocet smrti
	notifie("Dosavadní počet úmrtí na Covid-19",data['deceased']) #vytvori se notifikaci s poctem smrti
	while True:
		time.sleep(600) #pocka se 10 minut
		data = serverRequest() #znova se nactou data ze serveru
		if lastDeath < data['deceased']: #pokovad se pocet mrtvich zvysil vytvori se notifikace s narustem
			notifie("Počet mrtvích na Covid-19 se zvýšil o",data['deceased']-lastDeath)