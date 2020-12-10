radky = open("soubor.txt", "r").readlines()
found = False

for radek in radky:
	cislo = int(radek.strip())

	for cisla in radky:
		cisla = int(cisla.strip())

		if (cislo + cisla == 2020):
			soucin = cislo*cisla
			print(f"Soucet {cislo} + {cisla} = 2020 a jejich soucin {cislo} * {cisla} = {soucin}")
			found = True

	if (found == True):
		break