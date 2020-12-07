#slovnik={ 2020-int(line.strip()):int(line.strip()) for line in open("2000.txt", "r")}

cisla=[int(line.strip()) for line in open("2000.txt", "r")]
zbytky=[2020-cislo for cislo in cisla]

for cislo in cisla:
	if cislo in zbytky: 
		print(f"prvni: {cislo}; druhe: {2020-cislo}; součin {cislo*(2020-cislo)}")
		break

for cislo in open("2000.txt", "r"):
	zbytek=2020-int(cislo.strip())
	for cislo1 in open("2000.txt", "r"):
		if zbytek==int(cislo1.strip()):	print(zbytek*int(cislo.strip()))