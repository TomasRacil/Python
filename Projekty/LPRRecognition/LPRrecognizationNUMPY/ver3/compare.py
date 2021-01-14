def Porovnani(): 
#Funkce pro porovnani a zapis vysledku

	vysledky = open("database.txt", "r").readlines()
	spravne = open("spravne.txt", "r").readlines()
	porovnani = open("porovnani.txt", "w")
	#Otevreni potrebnych souboru

	for i in range(0,len(vysledky)):
	#Projde vsechny zaznamy ve vysledcich
		vysledky[i] = vysledky[i].strip()
		spravne[i] = spravne[i].strip()
		#Zbaveni se vsech zbytecnych symbolu (\n)

		cislo1, spz1 = vysledky[i].split(";")
		cislo2, spz2 = spravne[i].split(";")
		#Rozdeleni na cislo zaznamu a SPZ

		if cislo1 == cislo2:
			if spz1 == spz2:
				porovnani.write(cislo1+";"+spz2+";"+spz1+";MATCH\n")
				#V pripade spravneho rozpoznani SPZ 

			else:
				porovnani.write(cislo1+";"+spz2+";"+spz1+";WRONG\n")
				#V pripade spatneho rozpoznani SPZ

	porovnani.close()
	#Zavreni souboru



def Vyhodnoceni():
#Funkce pro vyhodnoceni vysledku z porovnavani

	spravne = open("porovnani.txt", "r").readlines()
	matchSum = 0

	for line in spravne:
	#Cyklus projde vsechna porovnani
		line = line.split(";")

		if "MATCH" in line[-1]:
			matchSum += 1
			#V pripade spravneho zaznamu se pricte ++ spravnych zaznamu

	matchSum = matchSum/len(spravne) * 100
	#Vypocet procentualni uspesnosti

	print("\n\nUspesnost: %.2f procent" % matchSum)