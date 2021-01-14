import LPR
import fSum
import time
import random
import compare

print("\nLPR 2021 - Rozpoznavani statni reg. znacky")
#Vytiskne nam hlavicku UI

time.sleep(2) 
#Program pocka 2 sekundy

print("\n\nVolby (zadejte prislusne cislo)\n1 - Precist konkretni zaznam\n2 - Precist nahodny zaznam\n3 - Precist celou databazi se zobrazenim obrazku\n4 - Precist celou databazi, zapsat do datbaze vysledky rozpoznavani\n5 - Porovnat celou databazi s vysledky a vyhodnotit\n0 - Ukoncit program")
#Vytiskne nam prislusne volby

Choose = False
Porovnej = False
#Inicializace bool pro odpovedi

files = fSum.fAmount("spz")
#Zjisteni poctu souboru ve slozce

while not Choose:
    #Cyklus pro ziskani vhodne odpovedi
    Choice = input("Volba: ")

    try:
        if int(Choice)>=0 and int(Choice)<=5: Choose=True
        else: print("Cislo mimo interval odpovedi. Znovu!")

    except Exception as e: 
        print(f"Chyba: {e}\nZnovu!")
    #Vytiskne nam chybu pri zadani spatne odpovedi


if(int(Choice)==0): exit()
#Ukonci program

elif(int(Choice)==1):
    while Choose: 
        Choice = input(f"Zadejte cislo zaznamu (1 - {files}): ")

        if(0 < int(Choice) <= files): 
            Choose = False
            LPR.LPRmain(int(Choice), True)
#Uzivatel zvoli zaznam a ten se zobrazi


elif(int(Choice)==2): 
    try:
        LPR.LPRmain(random.randint(1, files), True)
    except Exception as e:
        print(f"Chyba: {e}\n")
    #V pripade nenalezeni SPZ se vypise chyba
    
    Choose = False
#Zobrazi se nahodny zaznam

elif(int(Choice)==3): database = True
#Zobrazi se vsechny SPZ vcetne obrazku

elif(int(Choice)==4): database = False
#Projede vsechny SPZ a zapise vysledky do "database.txt"

elif(int(Choice)==5):
    database = False
    Porovnej = True
#Projede vsechny SPZ, zapise je do "database.txt", porovna se spravnymi vysledky a vyhodnoti procentualni presnost


if Choose and database: #Volba cislo 3 - projde vsechny SPZ a zobrazi je 
    for n in range(1, files+1):
    #Projede vsechny soubory ve zlozce
        try:
            LPR.LPRmain(n, database)
        except Exception as e:
            print(f"Chyba: {e}\nPřeskočeno!")
        #V pripade ze nenalezne zadnou SPZ, vypise se chyba



elif Choose and not database: #Volba cislo 4 a 5 - projde vsechny SPZ a zapise je do "database.txt"
    data = open("database.txt", "w")
    #Vytvori databazi pro zapis

    for n in range(1, files+1):
    #Projede vsechny soubory ve slozce
        try:
            data.write(str(n)+";"+LPR.LPRmain(n, database)+"\n")
        except Exception as e:
            data.write(str(n)+";"+"------\n")
        #V pripade nenalezeni SPZ se zapise prazdny zaznam

    data.close()


if Porovnej: #Volba cislo 5 
    compare.Porovnani()
    #Porovna SPZ a zapise do noveho .txt

    compare.Vyhodnoceni()
    #Z vyhodnocovaciho .txt vypocita procentualni presnost uspesneho urceni SPZ
