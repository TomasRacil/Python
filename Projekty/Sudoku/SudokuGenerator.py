from Zdroj.Pracespolem import *
from Zdroj.Grafika import *
import argparse

def main():
    """parser = argparse.ArgumentParser(description='Argumenty předáváme pomocí -přikaz')
    parser.add_argument('-l', metavar='Level - Nastaveni obtiznosti 1-3', type=int, default=1,
                        help='Úroveň obtížnosti nízká')
    args = parser.parse_args()
    print(args.accumulate(args.))"""
    """#print(f"předáno vlajkou {args}")"""
    print("V případě zájmu udělejte prosím výstřižek sudoku")
    obtiznost = int(input("Zadejte obtiznost (1-3): \n"))
    if(obtiznost>3):
        print(f"Zvolili jste spatnou obtiznost")
    elif(obtiznost<1):
        print(f"Zvolili jste spatnou obtiznost")

    #print(praceBod.__doc__ + '\n')
    praceBod(bod,2)

    #print(vymazBod.__doc__ + '\n')
    vymazBod(bod, obtiznost)

    #print(drawbod.__doc__ + '\n')
    drawbod(bod)

    #print(konzole.__doc__ + '\n')
    konzole(bod)

if __name__ == '__main__':
    main()