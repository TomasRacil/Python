from Moduly import *
import argparse
   
slova = list()

#vytvoření vlajky
parser = argparse.ArgumentParser(description='Vlajka pro pocet pismen')
parser.add_argument('-n', metavar='n', type=int, default=1, help='Zadej pocet pismen')
args = parser.parse_args()

def main():
    #přečte soubor a naplní list jejimy daty
    with open("slovnik.txt", "r", encoding="utf-8") as f:        
        for radek in f.readlines():
            slova.append(radek.strip())

    print(slova[index])
    while(konecHry==False):
        slovo = input("Zadej slovo: ")
        ByloZadano(slovo, slova, args.n)
   
if __name__ == '__main__':
    main()







    
