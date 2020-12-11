import math
import time

#slovnik={ 2020-int(line.strip()):int(line.strip()) for line in open("2000.txt", "r")}

#čteme soubor řádek po řádku a u každého řádku použijeme metodu strip, která odstraní všechny bílé znaky ze začátku a konce řetězce 
#také ho převedeme na int pomocí castingu následně je ukládáme do seznamu
cisla=[int(line.strip()) for line in open("2000.txt", "r")]
#u každého prvku seznamu spočítáme rozdíl mezi 2020 a prvkem a výsledek uložíme do seznamu
zbytky=[2020-cislo for cislo in cisla]

#procházíme seznam a ověřujeme jestli jsou jednotlivé prvky v seznamu zbytky pokud ano vytiskneme čísla a jejich násobek
for cislo in cisla:
	if cislo in zbytky: 
		print(f"prvni: {cislo}; druhe: {2020-cislo}; součin {cislo*(2020-cislo)}")
		break
#cyklus, který funguje podobně jako předchozí, ale přistupuje k souboru v rámci cyklu
#prvně procházíme a najdeme zbytek po odečtení 2020 a čísla v souboru následně hledáme shodné číslo v souboru
#pokud najdeme vynásobíme

for cislo in open("2000.txt", "r"):
	zbytek=2020-int(cislo.strip())
	for cislo1 in open("2000.txt", "r"):
		if zbytek==int(cislo1.strip()):	print(zbytek*int(cislo.strip()))

#TODO použít indexování


print(math.prod(
	{int(line.strip()) for line in open("2000.txt", "r")}
	.intersection({2020-cislo for cislo in cisla})))

#TODO komentáře + lepší algoritmus
cisla={int(line.strip()) for line in open("2000.txt", "r")}
for cislo in cisla:
	zbytek1=2020-cislo
	for cislo1 in cisla:
		zbytek2=zbytek1-cislo1
		for cislo2 in cisla:
			if zbytek2 == cislo2:print(cislo,cislo1,cislo2,cislo*cislo1*cislo2)

