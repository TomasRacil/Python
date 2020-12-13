import argparse
import os

minCharacters=2 #jaká je minimální délka stringu, aby byl definovaný jako slovo
maxDelka=1 #potřebné pro UI
remove=[',', '?', '!', '_', ')', '(', '.', ':', '-', ']', '[', '*', '\'', ';', '"'] # znaky, které se odstraní
database = [] #unikátní databáze - obsahuje každé klíčové slovo pouze jednou
              #dvourozměrné pole - index 0: slovo, index 1: výskyt slova
c=0

parser=argparse.ArgumentParser(description="Vlajka ve formátu -hodnota")
parser.add_argument('-min', metavar="minPocetPismen", type=str, default=2, help="Zadejte minimalni pocet pismen, aby byl retezec povazovan za slovo")
args = parser.parse_args()
try:
    minCharacters = int(args.min)
except:
    print("\nNeplatny argument! Bude pouzita defaultni hodnota (min=2)\n\n")
    minCharacters=2


def Sort(pole): #bubble sort
    n=len(pole)

    for i in range(n-1):
        for j in range(n-i-1):
            if pole[j][1] < pole[j+1][1]:
                tempSlovo=pole[j][0]
                tempVyskyt=pole[j][1]
                pole[j][0]=pole[j+1][0]
                pole[j][1]=pole[j+1][1]
                pole[j+1][0]=tempSlovo
                pole[j+1][1]=tempVyskyt

def Vypis(pole):
    os.system('cls')
    print(f"\nPocet pouzitych slov: {len(pole)}")
    print("======================================\n")
    print("Slovo", end='')
    for i in range(maxDelka - 3):
        print(" ", end='')
    print("Vyskyt")
    print("--------------------------------------")

    for slovo in pole:
        print(f"{slovo[0]}", end='')
        for i in range(maxDelka + 1 - len(slovo[0])):
            print(" ", end='')
        print(f"{slovo[1]}")

def StatusBar(completed, total):
    os.system('cls')
    print("\nProbiha vypocet\n\n")
    procenta=completed/(total/100)
    dily=round(procenta/2.5)

    for i in range(dily):
        print("=",end='')
    for i in range(40-dily):
        print(" ", end='')
    print(f"| {round(procenta)}%")


file = open("data.txt", "r")
text=str(file.read())
data=text.split() #celý obsah souboru se nahraje do data a rozdělí se podle mezer a \n na slova

for i in range(len(data)): #vymažeme nechtěné znaky (obsaženy v listu remove) a převede vše na malá písmena
    for znak in remove:
        data[i]=data[i].replace(znak, '')
        data[i]=data[i].lower()

celkem = int(len(data))
refresh = round((celkem/100) * 3.65)

for word in data:
    c += 1
    if c % refresh == 0:
        StatusBar(c, celkem)

    nalezeno=False

    for i in range(len(database)):
        if database[i][0]==word:
            database[i][1]+=1
            nalezeno=True

    if not nalezeno:
        if len(word)>=minCharacters:
            database.append([word, 1])
            if len(word)>maxDelka:
                maxDelka=len(word)


Sort(database)
Vypis(database)

input()