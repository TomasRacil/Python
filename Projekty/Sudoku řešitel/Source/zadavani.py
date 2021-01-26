class NeniVRozsahu(Exception):
	pass
def zadavani():
	"""zadavani - cyklus pro definovaní 2d pole a zadávání čísel a ošetření vstupu
	Args:
				
	Returns:
		tabulka s vloženými hodnotami
	"""
	#cyklus pro definovaní 2d pole uživatel zadává čísla 1 po druhém...
	tabulka =[[0]*9]*9
	tabulka = []; sloupec = []
	for i in range(0,9):
		tabulka += [0]
	for i in range (0,9):
		tabulka[i] = [0]*9
	#Plnění pole s ošetřením vstupu 
	for i in range (0,9):
		for j in range (0,9):
			while True:
				print ('Zvol čísla od 0-9 - Radek: ',i+1,' Sloupec: ',j+1)
				try:
					tabulka[i][j]=int(input())
					if tabulka[i][j] not in range(0,10): raise NeniVRozsahu
					break
				except NeniVRozsahu:
					print("Neni v rozsahu")
				except ValueError:
					print("Neni cislo")
				except Exception as e:
					print(f"Neocekavana vyjimka: {type(e)}")
	return tabulka