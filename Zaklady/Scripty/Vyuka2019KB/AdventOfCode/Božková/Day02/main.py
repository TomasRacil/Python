soubor = open("soubor.txt", "r")
spravneH = 0

for radek in soubor:
	interval, pismeno, heslo = radek.split(" ")
	minimum, maximum = interval.split("-")
	pismeno = pismeno.strip(":")
	
	pocetP = heslo.count(pismeno)

	if pocetP >= int(minimum) and pocetP <= int(maximum): spravneH = spravneH + 1

print(f"Bylo nalezeno {spravneH} spravnych hesel.")