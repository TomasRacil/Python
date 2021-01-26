from Source.zadavani import * 
from Source.vypis import *
from Source.reseni import *
def main():
	print("Vítej v programu sudoku! Vypis cisla a automaticky se vám vyplni sudoku, zadávej ve tvaru 0-9")
	#print(zadavani.__doc__ + '\n')
	tabulka=zadavani()

	#print(vypis_sud.__doc__ + '\n')
	vypis_sud(tabulka)

	print("- - - - - - - - - - - - ")

	#print(reseni.__doc__ + '\n')
	reseni(tabulka)
	
	#print(vypis_sud.__doc__ + '\n')
	vypis_sud(tabulka)
if __name__ == '__main__':
    main()