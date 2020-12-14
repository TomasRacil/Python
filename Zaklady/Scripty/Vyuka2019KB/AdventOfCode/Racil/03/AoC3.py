import math

#převedeme textový soubor do 2D listu,  prcházíme řádek po řádku každý řádek pak rozdělíme na jednotlivé zanky a ukládáme do seznamu
mapa = [[pole for pole in radek.strip()] for radek in open("stromy.txt", "r")]
#seznam s jednotlivými variantami tobogánu
varianty=[[1,1],[3,1],[5,1],[7,1],[1,2]]
#seznam pro zápis výsledků
vysledky=[]

#cyklus řešící problém pro jednotlivé varianty
for varianta in varianty:
	#x je x-ový index, y je y-ový index, pocet - ctromů na které je při procházení naraženo
	x,y,pocet=0,0,0
	#procházíme 2D pole dokud nenarazíme na jeho konec tedy poslední řádek
	while y<len(mapa):
		#pokud narazíme na strom navýšíme počet
		if mapa[y][x]=="#": pocet+=1
		#navýšení indexů v závislosti na variantě
		x,y=x+varianta[0],y+varianta[1]
		#pokud dojdeme na konec řádku přesuneme se na jeho začátek v zadání řečeno že vzor se opakuje do nekonačna směrem osy x
		if x>=len(mapa[0]): x-=len(mapa[0])
	#uložíme výsledky do našeho seznamu výsledků
	vysledky.append(pocet)
#matematická funkce prod() vynásobí všechny prvky seznamu
print(math.prod(vysledky))