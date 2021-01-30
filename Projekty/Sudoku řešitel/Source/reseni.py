def prazdne_pole(board):
	"""Prazdne pole - funkce pro zjištění pradného/nulového prvku v sudoku
	Args:
	board --- sudoková matice
	Returns:
	Adresa prvku s prázdným polem(i,j)
	"""
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board [i][j] == 0:
				return (i, j)
	return None
def prochazeni(board, cislo, pozice):
	"""prochazeni - funkce která nám prochází matici a kontroluje zdali se stejné číslo, které se dolňuje
		se nachází na -radku/sloupci/boxu
	Args:
	board --- sudoková matice
	cislo --- cislo, které se porovnává
	pozice --- pozice toho cisla
	Returns:
	True/False jestli se dané číslo nachazí v radku/sloupci/boxu
	"""
	for i in range (len(board[0])):
		if board[pozice[0]][i]== cislo and pozice[1] != i:
			return False
	for i in range (len(board)):
		if board[i][pozice[1]]== cislo and pozice[0] != i:
			return False
	sektor_x = pozice[1] //3
	sektor_y = pozice[0] //3
	"""mapování sudoku rozdělení 9x9 na boxy 9x3x3,(prvni box obsahuje prvky z řádku 0-2 a sloupce 0-2). To nám poslouží pro kontrolu
	zda ji v matici 3x3 už dané číslo vypsáno. """
	for i in range(sektor_y*3, sektor_y*3 + 3):
		for j in range(sektor_x*3, sektor_x*3 + 3):
			if board[i][j] == cislo and (i, j) != pozice:
				return False
	return True
def reseni(board):
	"""reseni - Backtracking, zjistujeme jestli máme konečně řešení hotové, pokud ne tak se opakuje, a generuji se cisla 
	do té doby než máme nalezené řešení. Pokud řešení nesedí tak se zpětně vrací, k poslednímu číslu a to změní.
	Args:
	board --- sudoková matice
	Returns:
	True/False jestli máme hotovo.
	"""
	najdi=prazdne_pole(board)
	if not najdi:
		return True
	else:
		radek, sloupec = najdi
	for i in range(1, 10):
		if prochazeni(board, i, (radek, sloupec)):
			board[radek][sloupec] = i

			if reseni(board):
				return True

			board[radek][sloupec] = 0
	return False