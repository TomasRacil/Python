"""tabulka = [
	[7,8,0,4,0,0,1,2,0],
	[6,0,0,0,7,5,0,0,9],
	[0,0,0,6,0,1,0,7,8],
	[0,0,7,0,4,0,2,6,0],
	[0,0,1,0,5,0,9,3,0],
	[9,0,4,0,6,0,0,0,5],
	[0,7,0,3,0,0,0,1,2],
	[1,2,0,0,0,7,4,0,0],
	[0,4,9,2,0,6,0,0,7]
]"""
"""def najit reseni
if rereseni.value==1:
	return no
for moznost in hledany find moznost*pocet
x+= find(moznost(*pocet))
return sum(x)
"""
class NeniVRozsahu(Exception):
	pass
def zadavani():

	#cyklus pro definovaní 2d pole uživatel zadává čísla 1 po druhém...
	tabulka =[[0]*9]*9
	tabulka = []; sloupec = []
	for i in range(0,9):
	  tabulka += [0]
	for i in range (0,9):
	  tabulka[i] = [0]*9
	#Plnění pole s ošetřením vstupu 
	for i in range (0,9):
		for j in range (0,9):
			while True:
				print ('Zvol čísla od 0-9 - Radek: ',i+1,' Sloupec: ',j+1)
				try:
					tabulka[i][j]=int(input())
					if tabulka[i][j] not in range(0,10): raise NeniVRozsahu
					break
				except NeniVRozsahu:
					print("Neni v rozsahu")
				except ValueError:
					print("Neni cislo")
				except Exception as e:
					print(f"Neocekavana vyjimka: {type(e)}")

	""" if not tabulka[i][j] in range (0,10):
	while tabulka[i][j] not in range (0,10):
	print ('Zadej znovu... zvol čísla od 0-9 - Radek: ',i+1,' Sloupec: ',j+1)
	tabulka[i][j] = int(input())
	if tabulka[i][j] in range (0,10):
	break"""

			

	return tabulka
	  

	
#Vypis sudoku do přehlednější varianty
def vypis_sud(board):
	for i in range(len(board)):
		if i % 3 == 0 and i!= 0 :
			print("- - - - - - - - - - - - - ")
	#cyklus prochází řádek a pokud je počet znaku dělitelný 3 tak přidá print 
		for j in range(len(board[0])):
			if j % 3 == 0 and j != 0:
				print(" | ", end="")
	#cyklus prochází sloupec pokud je počet znaku  dělitelný 3 tak přidá print 			
			if j == 8:
				print (board[i][j])
	#když narazí na konec tak jen vypíše poslední číslo
			else:
				print(str(board[i][j]) + " ", end="")
	#pokud ani jedno tak defaulte vypíše číslo + mezeru
def prazdne_pole(board):
	#funkce pro zjištění prázdné buňky prochází cyklus a jakmile narazí na 0 vratí její souřadnice pokud je něco jiného nevrací nic
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board [i][j] == 0:
				return (i, j)
	return None
def prochazeni(board, cislo, pozice):
	for i in range (len(board[0])):
		if board[pozice[0]][i]== cislo and pozice[1] != i:
			return False
	for i in range (len(board)):
		if board[i][pozice[1]]== cislo and pozice[0] != i:
			return False
	#cyklus pro zjištění, jestli je číslom které se vkládá už na řádka nebo ve sloupci. 
	sektor_x = pozice[1] //3
	sektor_y = pozice[0] //3
	#mapování sudoku rozdělení 9x9 na boxy 9x3x3,(prvni box obsahuje prvky z řádku 0-2 a sloupce 0-2). To nám poslouží pro kontrolu
	#zda ji v matici 3x3 už dané číslo vypsáno. 
	for i in range(sektor_y*3, sektor_y*3 + 3):
		for j in range(sektor_x*3, sektor_x*3 + 3):
			if board[i][j] == cislo and (i, j) != pozice:
				return False
	return True
def reseni(board):
	#funkce pro plnění čísel do jednotlivých buňěk, 
	najdi=prazdne_pole(board)
	if not najdi:
		return True
	else:
		radek, sloupec = najdi
	#zjisti jestli máme hotovou sudoku pokud už není číslo které, by se mohlo doplnit tak se cyklus ukončí,
	for i in range(1, 10):
		if prochazeni(board, i, (radek, sloupec)):
			board[radek][sloupec] = i

			if reseni(board):
				return True

			board[radek][sloupec] = 0
	"""Využití backtracking, pokud dané vygenerované číslo nesedí s řešením, tak se prvek vynuluje a vrací se do
	předchozího kroku. 
	"""
	return False
print("Vítej v programu sudoku! Vypis cisla a automaticky se vám vyplni sudoku, zadávej ve tvaru 0-9")
tabulka=zadavani()
vypis_sud(tabulka)
print("- - - - - - - - - - - - ")
reseni(tabulka)
vypis_sud(tabulka)