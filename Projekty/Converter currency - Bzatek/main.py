from Module import *

def VytisknoutDostupneMeny():
    """
    vytiskne vsechny dostupne meny mozne menit
    nahrava data z dostupne meny, prevede je na jeden string
    vytiskne string
    """
    print("Vsechny dostupne meny")
    vsechnyMeny=""
    for i in range(len(dostupneMeny)):
        vsechnyMeny+=dostupneMeny[i]
        vsechnyMeny+=" "
    print(vsechnyMeny)

def UkazatKurzy():
    zadanaMena=ZadejMenu(dostupneMeny)
    kurzy=DostanKurzy(zadanaMena)

    for i in range(len(kurzy)):
        print(kurzy[i][0]+" "+kurzy[i][1])


print("Hello World!!!") #zadny projekt se bez tohoto prikazu neobejde

dostupneMeny=GetValidCurrency() #promenna obsahuje pole men se kterymi lze pracovat
ukoncit=False 
while not ukoncit:
    vybral=False
    while not vybral:
            print("\n[1] Ukazat vsechny dostupne meny\n[2] Udelat prevod\n[3] Ukazat kurzy pro danou menu\n[4] Ukoncit")
            volba=input("\nZvolte akci: ")
            try:
                volba=int(volba)
                if volba==1 or volba==2 or volba==3 or volba==4:
                    vybral=True
            except ValueError:
                print("Toto není číslo, zadejte číslo")
            except Exception as e:
                print(f"Neočekávaná vyjímka: \n{e}")

    if volba==1:
        VytisknoutDostupneMeny()

    if volba==2:
        UdelatPrevod(dostupneMeny)

    if volba==3:
        UkazatKurzy()

    if volba==4:
        ukoncit=True

