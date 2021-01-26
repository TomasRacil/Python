def vypis_sud(board):
	"""vypis_sud - funkce pro vypis sudoku v citelnem tvaru
	Args:
	board --- sudoková matice
	Returns:
	"""
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