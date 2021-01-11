from exchangeratesapi import Api


api = Api()
api.get_rates()

def VytisknoutDostupneMeny():
    print("Vsechny dostupne meny")
    vsechnyMeny=""
    for i in range(len(dostupneMeny)):
        vsechnyMeny+=dostupneMeny[i]
        vsechnyMeny+=" "

    print(vsechnyMeny)

def UdelatPrevod():
    print("TODO")
    print("Kterou menu chcete prevest?")
    menaVstup=ZadejMenu()
    print("Jakou castku chcete prevest?")
    castkaVstup=zadatInt()
    print("Na kterou menu chcete prevest?")
    menaVystup=ZadejMenu()

    castkaVystup=ProvedVypocet(menaVstup,menaVystup,castkaVstup)
    castkaVystup=round(castkaVystup*100)/100.0
    print(castkaVstup+" "+menaVstup+" prevedeno na "+str(castkaVystup)+" "+menaVystup)

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
def UkazatKurzy():
    zadanaMena=ZadejMenu()
    kurzy=DostanKurzy(zadanaMena)

    for i in range(len(kurzy)):
        print(kurzy[i][0]+" "+kurzy[i][1])
def ProvedVypocet(menaVstup,menaVystup,castkaVstup):
    kurzy=DostanKurzy(menaVstup)
    kurz=0
    for i in range(len(kurzy)):
        if kurzy[i][0]==menaVystup:
            kurz=kurzy[i][1]
            break
    vystup=float(castkaVstup)*float(kurz)
    
    return vystup
def DostanKurzy(zadanaMena):
    kurzy=str(api.get_rates(zadanaMena)).split(",")
    for i in range(len(kurzy)):     
        kurzy[i]=kurzy[i].replace("'",'')
        kurzy[i]=kurzy[i].replace("{",'')
        kurzy[i]=kurzy[i].replace("}",'')
        kurzy[i]=kurzy[i].replace(" ",'')

        kurzy[i]=kurzy[i].split(":")

        if("rates" in kurzy[i][0]):
            del kurzy[i][0]

    if("date" in kurzy[len(kurzy)-1][0]):
        del kurzy[len(kurzy)-1]
    if("base" in kurzy[len(kurzy)-1][0]):
        del kurzy[len(kurzy)-1]
    return kurzy
def ZadejMenu():

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

print("Hello World!!!")

dostupneMeny=["CAD","HKD","ISK","PHP","DKK","HUF","CZK","GBP","RON","SEK","IDR","INR","BRL","RUB","HRK","JPY","THB","CHF","EUR","MYR","BGN","TRY","CNY","NOK","NZD","ZAR","USD","MXN","SGD","AUD","ILS","KRW","PLN"]

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
        UdelatPrevod()

    if volba==3:
        UkazatKurzy()

    if volba==4:
        ukoncit=True

