import random
from os import path


# with open(path.join(path.dirname(path.realpath(__file__)),"vstup.txt"), "r") as soubor:
#     vstup =[[znak for znak in radek if znak.isdigit()] for radek in soubor.read().split('\n')]
#     # print(vstup)
    
#     print(sum([int(radek[0]+radek[-1]) for radek in vstup]))
#     # suma = 0
#     # for skupina_cisel in vstup:
#     #     if len(skupina_cisel)==0:
#     #         continue
#     #     suma+=int(skupina_cisel[0]+skupina_cisel[-1])
#     # print(suma)

cisla = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine") 
    
with open(path.join(path.dirname(path.realpath(__file__)), "vstup_full.txt"), "r") as soubor:
    
    vstup = [
        [znak for znak in radek if znak.isdigit()]
             for radek in soubor.read().split('\n')
             ]
    vstup = sum([int(cisla[0] + cisla[-1]) for cisla in vstup])
    print(vstup)
    
    
    soubor.seek(0)
    vstup = [
        [
            (
                znak
                if znak.isdigit()
                else next(
                    (
                        str(i)
                        for i, prefix in enumerate(cisla)
                        if radek[idx:].startswith(prefix)
                    ),
                    "",
                )
            )
            for idx, znak in enumerate(radek)
            if (znak.isdigit() or radek.startswith(cisla, idx))
        ]
        for radek in soubor.read().split("\n")
    ]
    # print(vstup)
    
    vstup = sum([int(cisla[0] + cisla[-1]) for cisla in vstup])
    print(vstup)