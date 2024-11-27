# import random
from random import randrange as rr

rr(100)

def vytvor_matici(pocet_radku, pocet_sloupcu)->list[list[int]]:
    return [[rr(10) for _ in range(pocet_sloupcu)] for _ in range(pocet_radku)]

def vytiskni_matici(matice)->None:
    for radek in matice:
        for hodnota in radek:
            print(hodnota, end='\t')
        print()
    print()
        
def secti_matice(matice_1, matice_2)->list[list[int]]:
    matice_3 = vytvor_matici(len(matice_1), len(matice_1[0]))
    for r, radek in enumerate(matice_2):
        for s, hodnota in enumerate(radek):
            matice_3[r][s]=matice_1[r][s]+hodnota
    return matice_3

if __name__ == "__main__":
    pocet_radku= int(input("Pocet radku: "))
    pocet_sloupcu = int(input("Pocet sloupcu: "))
    matice_1 = vytvor_matici(pocet_radku,pocet_sloupcu)
    print([dvojice for dvojice in enumerate(matice_1)])
    vytiskni_matici(matice_1)
    matice_2 = vytvor_matici(pocet_radku,pocet_sloupcu)
    vytiskni_matici(matice_2)
    vytiskni_matici(secti_matice(matice_1,matice_2))
    
    