"""9. Vytvořte program, tahání nejkratší sirky zadáte počet osob a jejich jména a program náhodně zvolí jednu z těchto osob.(1)"""
"""MagdalenaHlavicova"""
from random import randint
import random

vyber = True
print("Vítejte v programu na náhodný výběr osoby")
print ("*"*41)

while vyber:
    pocet = int(input("Zadejte počet osob: "))

    cyklus = 0
    seznamOsob = []
    """Vytvoření prázdného seznamu"""
    
    for cyklus in range(0, pocet):
        osoba = input("Zadejte jméno osoby: ")  
        seznamOsob.append(osoba)
        """Funkce, která přečte vstup od uživatele a zadané jméno uloží do seznamu"""

    print("Náhodný výběr jména je: ", random.choice(seznamOsob))
    """Funkce, která ze seznamu náhodně vybere jméno"""

    pokracovani = input("Chcete vybrat jiné jméno? (A - ano) (N - Ne) \n")
    if  pokracovani.lower().strip() == "a" :
        vyber = True
    else:
        print ("Loučíme se s Vámi!!")
        print ("*"*19)
        vyber = False

    


