uzivatelskeJmeno=None


def cteniZeSouboru (soubor="konfigurace.txt"):
	"""Funkce pro čtení ze souboru"""
	soubor = open(soubor, "r")
	return soubor

def zapisDoSouboru (uzivatelskeJmeno):
	"""Funkce pro zápis do souboru"""
	soubor = open("konfigurace.txt", "a")
	soubor.write("\n"+uzivatelskeJmeno)
	soubor.close()

def najdiJmeno (uzivatelskeJmeno):
	soubor=cteniZeSouboru()
	for radek in soubor:
		if radek == uzivatelskeJmeno: return True

	return False

print("Chcete hrát?")

chceHrat=input("pokud ano zadejte Y: ")

if chceHrat.lower() == 'y':

	zadalVek=False

	while not zadalVek:
		vek=input("Zadejte svůj věk: ")

		try:
			if int(vek)>=18:
				print("Hra zacina")

				uzivatelskeJmeno=input("Zadej své uživatelské jméno: ")

				uzivatelExistuje= najdiJmeno(uzivatelskeJmeno)

				if uzivatelExistuje:
					print("uživatel existuje")
				else:
					print("přidávám užvatel")
					zapisDoSouboru(uzivatelskeJmeno)

				

			elif int(vek)==17:
				print("Už jen jeden rok")

			else:
				print("nemůžeš hrát")

			zadalVek=True

		except ValueError:
			print("Toto není číslo, zadejte číslo")

		except Exception as e:
			print(f"Neočekávaná vyjímka: \n {e}")
			zadalVek=True


	print("program pokracuje")

else:
	print("Hra ukončena")

