from random import randint

class Error(Exception):
    pass

class VysokeCislo(Error):
    def __init__(self, message="Cislo je moc vysoke"):
        self.message=message
        super().__init__(self.message)

class NizkeCislo(Error):
    def __init__(self, message="Cislo je moc nizke"):
        self.message=message
        super().__init__(self.message)


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
        try:
            if vstup_uzivatel>nahodne_generovane_cislo:
                raise NizkeCislo
            else:
                raise VysokeCislo
        except NizkeCislo as e:
            print(e)
        except VysokeCislo as e:
            print(e)
        
        rozdil=abs(vstup_uzivatel-nahodne_generovane_cislo)

        if rozdil>=50: print("Hledane cislo je daleko")
        elif rozdil>=20: print("Hledane cislo je pomerne blizko")
        else: print("Jsi blizko")


    
