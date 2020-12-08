import math

mapa = [[pole for pole in radek.strip()] for radek in open("stromy.txt", "r")]
varianty=[[1,1],[3,1],[5,1],[7,1],[1,2]]
vysledky=[]

for varianta in varianty:
	x,y,pocet=0,0,0
	while y<len(mapa):
		if mapa[y][x]=="#": pocet+=1
		x,y=x+varianta[0],y+varianta[1]
		if x>=len(mapa[0]): x-=len(mapa[0])
	vysledky.append(pocet)

print(math.prod(vysledky))