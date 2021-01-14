#nedokončeno

from random import randint
import argparse
    
    
#vytvoření vlajky
parser = argparse.ArgumentParser(description='Vlajka pro pocet pismen')
parser.add_argument('-n', metavar='n', type=int, default=1, help='Zadej pocet pismen')
args = parser.parse_args()

n = (args.n)

# inicializace proměnných
slova = list()
pouzite = list()
hledane = list()
i = 0

#přečte soubor a naplní list jejimy daty
with open("slovnik.txt", "r", encoding="utf-8") as f:        
    for radek in f.readlines():
        slova.append(radek)
        
#deklarace prvního slova
prvniSlovo = randint(0, len(slova))
pouzite.append(slova[prvniSlovo])
print(slova[prvniSlovo])
podminka = True

while podminka:
    podminka1 = True
    x = input("Zadej slovo: ")
    m_pouzite = pouzite[-1]
    if x[0:n] == m_pouzite[-n: len(m_pouzite)]: 
        print("Neplatne slovo!")  
        break
    else:
        for i in range (len(slova)):
            slovo = slova[i]
            text = slovo[0:n]                       #první n písmena ve slově
            text1 = x[-(n): len(x)]                 #poslednich n písmen ve slově
            if text[0:n] == text1[0:n]:             #pokud jsou vybrané úseky slova stejné...
                text = text1
                hledane.append(slova[i])  

#pokud neexistuje žádné další vhodné slovo -> konec
        if len(hledane) == 0:     
            podminka = False
            break    
    vyber = randint(0, len(hledane))
    print("----------------------------------------")
    print(f"\n Odpověď počítače: {hledane[vyber]}")
    print("----------------------------------------")
    pouzite.append(hledane[vyber])                              #naplní list pouzite, ty už se ve hře nesmí objevit
    hledane.clear()                                             #vymaže list hledane, pro použití u dalšího slova      
    print("----------------------------------------") 
        
print("Konec")
