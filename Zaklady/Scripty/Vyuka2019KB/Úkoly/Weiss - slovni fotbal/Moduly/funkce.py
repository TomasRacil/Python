from random import randint

pouzite = []
hledane = list()
konecHry=False
nalezeno=False
skore = 0
index = randint(0, 925705)
 


def ByloZadano(slovo, slova, n):
    """
    Vstupy funkce:
    - slovo = zadané slovo od uživatele
    - slova = list slov získaného ze slovníku (ze souboru)
    - global pouzite = globální list - slova, která již byla použita
    - n = počet písmen na které se hraje (převzato z flagů, při spuštění)

    Funkce se podívá do listu "pouzite" a zkontroluje, zdali slovo, ktere se má porovnávat nebylo již použito
    Předává argumenty funkci PorovnaniZnaku
    # pokud je argument > 3, tak ukončí hru.. 
    """
    if (n > 3):
     print ("Chybne zadany argument. -n musi byt 1-3")
     konecHry=True;
     return 0;

    global pouzite
    
    if (slovo in pouzite):
            print("Toto slovo uz bylo zadano")
    else:
        PorovnaniZnaku(slovo, slova,n)

def PorovnaniZnaku(slovo, slova,n):
     """
     Vstupy funkce
     - slovo = zadané slovo od uživatele
     - slova = list slov získaného ze slovníku (ze souboru)
     - global index = pozice zadaného slova ve slovníku
     - n = počet písmen na které se hraje (převzato z flagů, při spuštění)

     Funkce zkontroluje, jestli první 2 písmena zadaného slova odpovídají posledním dvou písmen vygenerovaného slova
     Předává argumenty funkci NalezenoVeSlovniku
     """
     if (slovo[:n] != slova[index][-n:]):
        print ("Neodpovida poslednim pismenum slova: " + str(n) + " písmen.")
     else:
         NalezenoVeSlovniku(slovo, slova,n)
         

def NalezenoVeSlovniku(slovo, slova,n):
    """
    Vstupy funkce: 
    - slovo = zadané slovo od uživatele
    - slova = list slov získaného ze slovníku (ze souboru)
    - global skore = počet správně zadaných slov
    - global pouzite = globální list - slova, která již byla použita
    - n = počet písmen na které se hraje (převzato z flagů, při spuštění)

    Funkce hledá zadané slovo ve slovníku. Pokud ho tam najde, tak ho přidá do použitých slov, 
    zvýší skóre, vypíše ho na obrazovku a předává argumenty funkci ZmenIndex.
    Pokud slovo nenajde - vypíše o tom zprávu na obrazovku
    """
    global skore

    if(slovo in slova):
       pouzite.append(slovo)
       skore+=1;
       print ("\nSkore je: " + str(skore) + "\n")
       ZmenIndex(slovo, slova,n)
    else:
       print("Nenalezeno ve slovniku")


def ZmenIndex(slovo, slova,n):
    """
    Vstupy funkce: 
    - slovo = zadané slovo od uživatele
    - slova = list slov získaného ze slovníku (ze souboru)
    - global konecHry = bool - True = hra ukončena, protože počítač ve slovníku nenašel slovo, které by mohl použít
    - global pouzite = globální list - slova, která již byla použita
    - global index = pozice zadaného slova ve slovníku
    - n = počet písmen na které se hraje (převzato z flagů, při spuštění)

    Funkce vezme slovo zadané uživatelem a vyhledá ve slovníku slovo, které by mohl použít
    Toto slovo pak zkontroluje, jestli už náhodou nebylo použito
    Pokud takové slovo existuje, napíše do globální proměnné index - pozici slova ve slovníku (číslo)
    Pokud nenalezne slovo nebo nalezne to, které již bylo použito - Ukončí hru a vypíše výsledné skóre na obrazovku
    """

    global index
    global pouzite
    global konecHry
  
    stareSlovo = slova[index]

    for i in range (len(slova)):
        if (slova[i][:n]==slovo[-n:]):
            if (slova[i] not in pouzite):
                index = i;
                pouzite.append(slova[index])
                print(slova[index])
                break;
    if (stareSlovo == slova[index]):
        konecHry=True
    if (konecHry==True):
        print("Hra skoncila. Tvoje skore je: " + (str)(skore));