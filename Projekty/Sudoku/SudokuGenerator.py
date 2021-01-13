from Grafika import *
from Prácespolem import *
# Vytvoření prázdného 2D pole
def main():
    print("V případě zájmu udělejte prosím výstřižek sudoku")
    obtiznost = int(input("Zadejte obtiznost (1-3): \n"))
    if(obtiznost>3):
        print(f"Zvolili jste spatnou obtiznost")
    elif(obtiznost<1):
        print(f"Zvolili jste spatnou obtiznost")

    """obtiznostNastav()"""
    praceBod(bod,2)
    vymazBod(bod, obtiznost)
    drawbod(bod)
    konzole(bod)

if __name__ == '__main__':
    main()