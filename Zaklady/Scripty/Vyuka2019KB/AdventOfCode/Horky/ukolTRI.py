

stromy = [radek.strip() for radek in open("D:/skola UNOB/Python/adventofcode/mapa.txt", "r")]

def showMap(pole):
	for radek in pole:
		print(radek)

for radek in stromy:
	stromy[stromy.index(radek)]=list(radek)

rad=0 #(1)
prv=0
Pocet=0
#print(stromy[1][3])

for radek in stromy:
	if stromy[rad][prv]=="#":
		Pocet+=1
		print(stromy[rad][prv])
	if prv==28:
		prv=-3
	if prv==29:
		prv=-2
	if prv==30:
		prv=-1
	rad+=1
	prv+=3

print(Pocet)
#showMap(stromy)