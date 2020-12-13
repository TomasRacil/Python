soubor = open("D:/skola UNOB/Python/adventofcode/mapa.txt", "r")

mapa = [[pole for pole in radek.strip()] for radek in soubor]	#nechapu????

"""
mapa=[[]]
for radek in soubor:
	radek.split()
	#mapa.append(radek.strip())
	for prvek in radek:
		mapa.append(prvek.split())
"""

"""
for prvek in mapa:
	print(mapa)
	print("\n")
#mapa=[][]
"""

print("Kontrola: \n")
print(mapa)
print(mapa[1])
print(mapa[5])
print(mapa[-1])