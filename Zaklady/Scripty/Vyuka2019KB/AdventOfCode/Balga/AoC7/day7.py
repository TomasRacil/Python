with open("input7.txt") as file:																#// Otevře soubor input7.txt v read-only modu
	data = file.readlines()																		#// Přečte všechny celý soubor po řádcích
	data = [ line.strip() for line in data ]													#// Odstraní whitespace znaky na začátku a konci každého řádku (mezery, \n atd..)
		
def get_num_bags(color):																		#// Vytvoří funkci get_num_bags s parametrem color
	lines = [line for line in data if color in linie and line.index(color) != 0]				#// Najde všechny řádky, kde je ta barva a slovo té barvy nezačíná na začátku řádku
	
	allColors = []																				#// Vynulování allColors

	if len(lines) == 0:																			#// Kontrola jestli počet prvků v lines není 0
		return[]																				#// Pokud je, tak nic nevrátím

	else:
		colors=[ line[:line.index("bags")] for line in lines ]									#// Najde index začátku slova bags na všech řádcích
		colors=[ color for color in colors if color not in allColors ]							#// Přečte barvu před bags pro všechny řádky

		for color in colors:																	#// cykluje všemi barvami co jsme našli
			allColors.append(color)																#// přidá barvu do allColors
			bags = get_num_bags(color)															#// Zavolá se get_num_bags pro barvy co jsme našli a vrátí nám počet unikátních barev
			allColors += bags																	#// Tyto unikátní barvy přidáme do allColors
		
		uniqueColors = []																		#// Vynulujeme uniqueColors
		for color in allColors:																	#// Cyklujeme v allColors
			if color not in uniqueColors:														#// Pokud daná barva ještě není v uniqueColors
				uniqueColors.append(color)														#// tak ji tam přidáme, jinak s ní nic neděláme

		return uniqueColors																		#// vrátíme unikátní barvy

	colors = get_num_bags("shiny gold")															#// Zavolá se get_num_bags funkce na shiny gold
	print(len(colors))																			#// Vypíše se počet unikátních barev
