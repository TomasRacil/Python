
def resetPodm():
	prv=3
	

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

# Po 10 radcich se dostanu na konec sloupcu abych splnil podminky a pak se od 11 radku to stejne opakuje... 
rad=0 #(1)
prv=3
Pocet=0

for prvek in mapa:
	print(mapa[rad])
	if rad%11==0:
		resetPodm()
		if (mapa[rad][prv]=='#'):
			Pocet=Pocet+1
			print("\n\n"+str(mapa[rad][prv]))
	elif (mapa[rad][prv]=='#'):
		print("\n\n"+str(mapa[rad][prv]))
		Pocet=Pocet+1
		if prv==28:
			prv=-3
		if prv==29:
			prv=-2
		if prv==30:
			prv=-1
		prv=prv+3
	rad=rad+1

print(f"Pocet stromu je : {Pocet}")
print("Kontrola: \n")
#print(mapa)
print(mapa[1])
print(mapa[5])
print(mapa[-1])