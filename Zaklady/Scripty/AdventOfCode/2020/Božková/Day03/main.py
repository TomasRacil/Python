soubor = open("text.txt", "r")
text = str(soubor.read())
radky = text.split()

index = 0
soucet = 0
delkaR = len(radky[0])

for radek in radky:
	if index >= delkaR: 
		index -= delkaR
	
	if radek[index] == "#":
		soucet += 1

	index += 3

print(f"Prejedeme {soucet} stromu")

