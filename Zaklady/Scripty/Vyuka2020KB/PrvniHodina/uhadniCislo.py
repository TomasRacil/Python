from random import randint

print("Uhadni nahodne cislo")

nahodne_generovane_cislo=randint(0,100)
#print(nahodne_generovane_cislo)

#neuhadl=True

while True:

    vstup_uzivatel= input("Zadej svuj tip: ")
    vstup_uzivatel = int(vstup_uzivatel)

    if vstup_uzivatel==nahodne_generovane_cislo:
        print("Podarilo se ti uhadnout cislo")
        #neuhadl=False
        break
    else:
        print("Nepodarilo se ti uhadnout cislo")

        if vstup_uzivatel>nahodne_generovane_cislo:
            print("Hledane cislo je mensi")
        else:
            print("Hledane cislo je vetsi")
        
        rozdil=abs(vstup_uzivatel-nahodne_generovane_cislo)

        if rozdil>=50: print("Hledane cislo je daleko")
        elif rozdil>=20: print("Hledane cislo je pomerne blizko")
        else: print("Jsi blizko")


    
