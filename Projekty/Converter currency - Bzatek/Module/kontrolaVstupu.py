def zadatInt():
    platnost=False
    while not platnost:
        cislo=input()
        try:
            if int(cislo)>0:
                platnost=True
                break
            else:
                print("Zadana castka musi byt kladna")
        except ValueError:
            print("Zadejte cislo")

        except Exception as e:
            print(f"Neočekávaná vyjímka: \n{e}")
            platnost=True
    return cislo

def ZadejMenu(dostupneMeny):

    platnost=False
    while not platnost:
        vstup=input('Zadej menu : ')
        for i in range(len(dostupneMeny)):
            if vstup==dostupneMeny[i]:
                platnost=True
                print("Zadana mena: "+vstup)
                break
        if not platnost: print("Toto neni dostupna mena")
    
    return vstup
