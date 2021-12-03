import time
soubor = open ("input.txt","r").readlines()  #otevreni souboru+cteni po radcich
start = time.time()
pom=0
for i in soubor:            #prvni cyklus
    for cislo2 in soubor:   #cyklus v cyklu
        cislo1 = int(i.strip()) #ulozeni 1. cisla
        cislo2 = int(cislo2.strip())    #ulozeni 2. cisla

        if (cislo1==pom): break
        else:
            if (cislo1+cislo2==2020):
                print(f"Hledana 2 cisla jsou => {cislo1},{cislo2}")
                soucin=cislo1*cislo2
                pom=cislo2
                print(f"->Kontrola:\t\t {cislo1} + {cislo2} = 2020\n->Soucin cisel:\t {cislo1} * {cislo2} = {soucin}\n")

#SECOND STAR -> hledani 3 cisel jejich soucet da 2020
for i in soubor:            #prvni cyklus
    for cislo2 in soubor:   #cyklus v cyklu
        cislo1 = int(i.strip()) #ulozeni 1. cisla
        cislo2 = int(cislo2.strip())    #ulozeni 2. cisla
        for cislo3 in soubor:
            cislo3 = int(cislo3.strip())    #ulozeni 3. cisla

            if (cislo1==pom): break
            else:
                if (cislo1+cislo2+cislo3==2020):
                    print(f"Hledana 3 cisla jsou => {cislo1},{cislo2},{cislo3}")
                    soucin=cislo1*cislo2*cislo3
                    pom=cislo2
                    print(f"->Kontrola:\t\t {cislo1} + {cislo2} + {cislo3}= 2020\n->Soucin cisel:\t {soucin}\n")

stop = time.time()
cas = (stop-start)*1000
print(f"Hledani trvalo {cas} ms.")