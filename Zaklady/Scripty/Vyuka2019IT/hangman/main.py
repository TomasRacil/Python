from modules import get_random_word
from re import finditer
from os import system, name


print(__name__)
if __name__=="__main__":
    slovo = get_random_word()
    print(slovo)
    hadane_slovo = "_"*len(slovo)
    while True:
        print(hadane_slovo)
        tip = input("Zadej pismeno: ")
        indexy = [m.start() for m in finditer(tip, slovo)] if tip!='' else []
        for index in indexy:
            docasna_promena=list(hadane_slovo)
            docasna_promena[index]=tip
            hadane_slovo=''.join(docasna_promena)
        
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        
        if hadane_slovo.find('_')==-1:
            print(hadane_slovo)
            print("Slovo uspesne uhadnuto!")
            break;
