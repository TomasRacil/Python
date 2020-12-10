"""def cteniZeSouboru (soubor="cisla.txt"):
    #Funkce pro čtení ze souboru
    soubor = open(soubor, "r")
    return soubor
"""
"""	
pocet=0
soubor = open("D:/skola UNOB/Python/adventofcode/cisla.txt", "r")
#soubor = cteniZeSouboru()
for radek in soubor:
	print(int(radek))
	pocet=pocet+1
	listRadku = int(radek)
soubor.close()

print("Pocet radku: " )
print(pocet)


for x in 200:
	for y in 200:
		#int(cislo)=listRadku[x]
		#int(cislo2)=listRadku[y]

		if listRadku[x]+listRadku[y]==2020:

			print("Nalezena cisla: " + cislo +" a "+ cislo2)
			break
"""


soubor = open("D:/skola UNOB/Python/adventofcode/cisla.txt", "r")

cisla=[]
pocet=0
for radek in soubor:
	cisla.append(int(radek))
	pocet=pocet+1

for prvek in cisla:
	for prvek2 in cisla:
		for prvek3 in cisla:
			if prvek+prvek2+prvek3==2020:
				print(prvek)
				print(prvek2)
				#vysledek=prvek*prvek2
				print(prvek3)
				vysledek=prvek*prvek2*prvek3
				print(vysledek)

print("Pocet radku: " + str(pocet))

"""
for cislo in open("D:/skola UNOB/Python/adventofcode/cisla.txt", "r"):
	zbytek=2020-int(cislo.strip())
	for cislo1 in open("D:/skola UNOB/Python/adventofcode/cisla.txt", "r"):
		if zbytek==int(cislo1.strip()):print(zbytek*int(cislo.strip()))
"""