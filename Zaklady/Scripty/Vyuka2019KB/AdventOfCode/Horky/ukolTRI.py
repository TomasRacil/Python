

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
	if rad>len(stromy):
		break
	if stromy[rad][prv]=="#":
		Pocet+=1
		print(stromy[rad][prv])
	"""if prv==24:
					prv=-7
				if prv==25:
					prv=-6
				if prv==26:
					prv=-5
				if prv==27:
					prv=-4
				if prv==28:
					prv=-3
				if prv==29:
					prv=-2"""
	if prv==30:
		prv=-1
	rad+=2
	prv+=1

print(Pocet)
#showMap(stromy)


#58*209*58*64*35
print(58*209*58*64*35)