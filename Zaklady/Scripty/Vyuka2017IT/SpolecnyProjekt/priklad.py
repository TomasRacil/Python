import random
def potkanisnadrizenym():
	print("Jde proti mně Mjr... Ajejeje co se asi ted stane???")
	akce = True
	while akce:
		iterakce = input("Budu pokračovat čelně proti němu-(A) Nebo mohu zkusit štěstí a zkusit jinou cestu-(N)\n")
		if iterakce.lower().strip() == "a":
			prvni=int(random.randint(1,6))
			druhy=int(random.randint(1,6))
			treti=int(random.randint(1,6))
			ctvrty=int(random.randint(1,6))
			suma = prvni+druhy+treti+ctvrty
			
			"""	Využívám 4 × kostku z duvodu menší pravděpodobosti hodit minimum a maximum, namisto 1 funkce s generatorem 4-24,
			kde je stejná šance na hození jakéhokoliv číslo. V této verzi zatím jen genereruji náhodna čísla, která určí 
			náhodnou možnost, využil jsem cyklu pro případ, že by někdo zadal i něco jiného, kromě volby možnosti a/n.  """
			if suma<11:
				print("Vojáku co ta vaše ustrojenost? Kdyby mi fungovali dávicí reflexy, tak bych teď zvracel!")
				akce=False
			elif suma > 11 and suma < 16:
				print("Vojaku ke mně!")
				akce=False
			else:
				print("V pořádku pokračujte!")
				akce=False
		elif iterakce.lower().strip() == "n":
			sance=int(random.randint(0,20))
			if sance <10:
				print("A sakra tohle nevyslo to zase schytám na nástupu...")
				akce=False
			else:
				print("Vyslo to! Můžu si říkat dítě štěstěny :)")
				akce=False
		else:
			print("Neplatné rozhodnutí! Zkus to zadat ve správnem tvaru, nauč se psát!")

potkanisnadrizenym()