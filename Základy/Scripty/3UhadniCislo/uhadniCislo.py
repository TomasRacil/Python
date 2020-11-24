from random import randint

hraj=True

while hraj:
	print("Hra uhodni číslo od 0 do 100!")
	if input("Pokud již nechceš hrát zadej 'q': ")=='q':break
	else:
		cislo = randint(0, 100)
		while hraj:
			tip=input("\nZadej svů tip na číslo (pokud chceš skončit  zadej 'q'): ")
			if tip=='q': 
				hraj=False
				break
			try:
				tip=int(tip)
				if tip==cislo:
					print(f"{tip} ano to je správné číslo.\nGRATULUJI!!\n"+"*"*30+"\n")
					break
				elif tip<cislo: 
					if(cislo-tip)>10: print("Tvůj tip je výrazně menší než hledané číslo\n")
					else: print("Tvůj tip je trošku menší než hledané číslo\n")
				else: 
					if(tip-cislo)>10: print("Tvůj tip je výrazně větší než hledané číslo\n")
					else: print("Tvůj tip je trošku větší než hledané číslo\n")
			except: print("Toto není platná volba zadej buď číslo nebo 'q'\n")