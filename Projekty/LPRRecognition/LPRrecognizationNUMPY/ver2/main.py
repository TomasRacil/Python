import LPR
import fSum
import time
import random

print("\nLPR 2021 - Rozpoznavani statni reg. znacky")
time.sleep(2)
print("\n\nVolby (zadejte prislusne cislo)\n1 - Precist konkretni zaznam\n2 - Precist nahodny zaznam\n3 - Precist celou databazi se zobrazenim obrazku\n4 - Precist celou databazi, zapsat do datbaze vysledky rozpoznavani\n0 - Ukoncit program")

Choose = False
files = fSum.fAmount("spz")

while not Choose:
    Choice = input("Volba: ")

    try:
        if int(Choice)>=0 and int(Choice)<=4: Choose=True
        else: print("Cislo mimo interval odpovedi. Znovu!")
    except Exception as e: 
        print(f"Chyba: {e}\nZnovu!")


if(int(Choice)==0): exit()
elif(int(Choice)==1):
    while Choose: 
        Choice = input(f"Zadejte cislo zaznamu (1 - {files}): ")
        if(0 < int(Choice) <= files): 
            Choose = False
            LPR.LPRmain(int(Choice), True)
elif(int(Choice)==2): LPR.LPRmain(random.randint(1, files), True)
elif(int(Choice)==3): database = True
elif(int(Choice)==4): database = False


if Choose and database:
    for n in range(1, files+1):
        try:
            LPR.LPRmain(n, database)
        except Exception as e:
            print(f"Chyba: {e}\nPřeskočeno!")
elif Choose and not database:
    data = open("database.txt", "w")

    for n in range(1, files+1):
        data.write(str(n)+";"+LPR.LPRmain(n, database)[:-1])