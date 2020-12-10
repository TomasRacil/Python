from GameEngine import *

""" funkce/tridy pro konfiguraci pri vyberu postavy """

def vyberPostavy():
    """Funkce pro vyber postavy/tridy a pripsani ji k novemu uzivateli"""
    postavy=["Warrior", "Scout", "Mage"]
    print("Pro zvoleni postavy zmacknete prislusne cislo\n")
    i=1
    vybral=False
    for postava in postavy:
        print(f"{i}. {postava}")
        i+=1
    while not vybral:
        volba=input('\n')

        try:
            if int(volba)>0 or int(volba)<i:
                print(f"Vybral sis postavu: {postavy[int(volba)-1]}")
                vybral=True
            elif int(volba)>=i:
                print("Prilis velke cislo. Znovu!")
        except Exception as e:
            print(f"Chyba: {e}\nZnovu!")
    
    return postavy[int(volba)-1]


def cteniZeSouboru (soubor="Data\konfigurace.txt"):
    """Funkce pro čtení ze souboru"""
    soubor = open(soubor, "r")
    return soubor
    

def zjistiID():
    """Funkce pro přidání jedinečného ID k novému uživatelskému jménu"""
    soubor = cteniZeSouboru()
    listRadku = soubor.readlines()
    soubor.close()
    pocet = listRadku[-1].split(';')
    return (int(pocet[0])+1)


def najdiJmeno(uzivatelskeJmeno):
    """Separuje z řádku jméno a porovná jej"""
    soubor=cteniZeSouboru()
    for radek in soubor:
        radek = radek.split('\n')
        IDjmeno = radek[0]
        jmeno = IDjmeno.split(';')
        if jmeno[1] == uzivatelskeJmeno: return True
    return False

def zapisDoSouboru(uzivatelskeJmeno):
    """Funkce pro zápis do souboru"""
    ID = zjistiID()
    vyber=vyberPostavy()

    if vyber=="Warrior": postava=1 #zapíše místo slova číslo odpovídající postavě, zakterou hráč hraje - aby pak šla loadnout
    if vyber=="Scout": postava=2
    if vyber=="Mage": postava=3

    soubor = open("Data\konfigurace.txt", "a")
    if ID<10: soubor.write("\n0")
    else: soubor.write("\n")
    soubor.write(str(ID)+";"+uzivatelskeJmeno+";"+str(postava))
    soubor.close()
    return postava

def saveGame(hrac,uzivatelskeJmeno):
    #TODO saveGame() - naxit IS WORKING on it    
    soubor = open("Data\konfigurace.txt", "r")
    
    i=0
    for line in soubor:
        line = line.split('\n')
        i+=1    
    soubor.seek(0)
    list=[{} for c in range(i)]
    i=0 
    for radek in soubor:
        radek = radek.split('\n')
        list[i]=radek[0]
        jmeno = list[i].split(';')
        if jmeno[1] == uzivatelskeJmeno:
            prepsanyRadek=jmeno[0]+";"+jmeno[1]+";"+jmeno[2]+";"+str(hrac.hp)+";"+str(hrac.damage)+";"+str(hrac.energy)  
            list[i]=prepsanyRadek
        i+=1      
    soubor.close()
    
    soubor = open("Data\konfigurace.txt", "w")
    soubor.write(list[0])
    
    for i in range(len(list)):
        if not i==0: soubor.write("\n"+list[i])
    soubor.close()

    print("Aktualni score ulozeno")