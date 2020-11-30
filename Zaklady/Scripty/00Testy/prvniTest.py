"""
Způsob jakým bych já odpověděl na otázky, které byly v testu 26.11.2020
"""
import logging
from random import randint

def prvniAlgoritmus(jmeno,prijmeni,rozsah):
	"""První algoritmus

	Args:
		jméno (str): křestní jméno
		prijmeni (str): příjmení 
		rozsah (int): velikost prohledávaného vzorku
	"""
	try:
		for cislo in range(1,rozsah):
			if cislo%len(jmeno+prijmeni)==0: print('x') if cislo%len(jmeno)==0 else print(cislo*2)
			elif cislo%len(jmeno)!=0: print(cislo)
	except Exception as e: logging.exception("Nastala vyjímka")

def vytvor2DPole(x,y, od, do):
	"""Vytvor 2D pole

	Args:
		x (int): počet sloupců
		y (int): počet řádků 
		od (int): nejnižší možná hodnota v poli
		do (int): nejvyšší možná hodnota v poli

	Returns:
		list: vrací vygenerované 2D pole náhodných hodnot
	"""
	try: return [[randint(od, do) for radek in range(x)] for sloupec in range(y)]
	except Exception as e: logging.exception("Nastala vyjímka")

def druhyAlgoritmus(pole,prijmeni):
	"""Druhý algoritmus

	Args:
		pole (list): 2D pole k vyhodnocení
		prijmeni (str): přijmení 

	Returns:
		tuple: vrací maximum, minimum a počet shod v matici
	"""
	try:
		maximum,minimum,pocet=pole[0][0],pole[0][0],0
		for radek in pole:
			for prvek in radek:
				if prvek == len(prijmeni): pocet+=1
				if prvek<minimum: minimum=prvek
				elif prvek>maximum: maximum=prvek
		return maximum,minimum,pocet
	except Exception as e: logging.exception("Nastala vyjímka")

def tretiAlgoritmus(n):
	"""Třetí algoritmus

	Args:
		n (int): číslo, nad kterým má být proveden faktoriál

	Returns:
		int: vrací faktoriál čísla n 
	"""
	try:
		if n==1: return 1
		else: return n*tretiAlgoritmus(n-1)
	except Exception as e: logging.exception("Nastala vyjímka")

jmeno=input("Zadej jméno: ")
prijmeni=input("Zadej prijmeni: ")

print("\nNásleduje výpis čísel splňujících podmínky")
prvniAlgoritmus(jmeno,prijmeni,100)

pole=vytvor2DPole(5,5,0,100)
print("\nNásleduje výpis náhodně vygenerovaného pole")
for radek in pole:print(radek)

x=druhyAlgoritmus(pole,prijmeni)

print(f"Maximum v poli je {x[0]}; minimum je {x[1]}; počet výskytů {len(prijmeni)} je {x[2]}")

while True:
	try:
		cislo=input("\nFAktoriál jakého čísla chcete spočítat: ")
		cislo=int(cislo)
		break
	except Exception as e: logging.exception("Nastala vyjímka zkuste to znovu")

print(f"Faktoriál je {tretiAlgoritmus(cislo)}")