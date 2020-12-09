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


def cteniZeSouboru (soubor="konfigurace.txt"):
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