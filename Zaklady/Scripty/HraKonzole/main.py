import time
from random import randint

uzivatelskeJmeno=None
age_restriction_partial_fix = True

class character():
    """třída ze které vychází postavy"""
    type=1 #1=warrior 2=scout 3=mage 4=banditNPC 5=dragonNPC
    hp=100
    damage=100
    energy=100
    alive=True
    

    def odectiHP(self, kolik):
        if (self.hp-kolik)>0:
            self.hp=self.hp-kolik
        else:
            self.hp=0
            self.alive=False

    def odectiEnergy(self, kolik):
        if (self.energy-kolik)>0:
            self.energy=self.energy-kolik
        else:
            self.energy=0

    def die(self):
        self.alive=False

    def resurrection(self): #musí se po ní zavolat ještě heal - oživit a uzdravit
        self.alive=True

    def card(self):
        print("====================")
        if self.type==1: print("Typ postavy: Warrior")
        if self.type==2: print("Typ postavy: Scout")
        if self.type==3: print("Typ postavy: Mage")
        if self.type==4: print("Typ postavy: Bandita")
        if self.type==5: print("Typ postavy: Drak")
        print(f"Živý: {self.alive}")
        print(f"Zdraví: {self.hp}")
        print(f"Energie: {self.energy}")
        print(f"Dává poškození: {self.damage}\n")


class warrior(character):
    def __init__(self,hp=120,energy=60,damage=90):
        self.type=1
        self.hp=hp
        self.energy=energy
        self.damage=damage

    def heal(self): self.hp=120
    def sleep(self): self.energy=60

class scout(character):
    def __init__(self,hp=50,energy=150,damage=20):
        self.type=2
        self.hp=hp
        self.energy=energy
        self.damage=damage

    def heal(self): self.hp=50
    def sleep(self): self.energy=150

class mage(character):
    def __init__(self,hp=65,energy=100,damage=110):
        self.type=3
        self.hp=hp
        self.energy=energy
        self.damage=damage

    def heal(self): self.hp=65
    def sleep(self): self.energy=100

class banditNPC(character): #za NPC nelze hrát - nemá fce jako heal a sleep
    def __init__(self):
        self.type=4
        self.hp=60
        self.energy=100
        self.damage=50

class dragonNPC(character): #za NPC nelze hrát - nemá fce jako heal a sleep
    def __init__(self):
        self.type=5
        self.hp=200
        self.energy=20
        self.damage=80



def fight(hrac, protivnik):
    """hráč dá svůj damage protivníkovi a protivník dá svůj damage hráči"""
    print("\nBOJUJEŠ!!!\n")
    print("Karta protivníka")
    protivnik.card()
    time.sleep(2)

    hrac.odectiHP(protivnik.damage)
    protivnik.odectiHP(hrac.damage)

    protivnik.odectiEnergy(20)
    hrac.odectiEnergy(20)

    if not hrac.alive and protivnik.alive:
        print("\nProtivník tě silně zasáhl\nCítíš silnou bolest a zatmívá se ti před očima\nKaždá cesta jednou končí...\n")
    if not protivnik.alive and hrac.alive:
        print("\nDáváš silné rány a vidíš, jak protivník slábne\nPoslední ranou jsi ho zasáhl přímo na hrudník a silně krvácí\nTentokrát jsi přežil...\n")
    if hrac.alive and protivnik.alive:
        print("\nSouboj je dlouhý a dynamický, bojuješ jako lev\nProtivník ale také nechce dnes zemřít...")
        print("Oba jste zranění a vyčerpaní, protivník se ti podívá do očí a z posledních sil se dá na útěk\n")
    if not hrac.alive and not protivnik.alive:
        print("\nJe zvláštní ticho\nV prachu a krvi leží dvě postavy\nZdá se, že vaše síly byly vyrovnané...\n")

    print("\nTvoje karta po boji")
    hrac.card()

    print("\n")


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

def zapisDoSouboru(uzivatelskeJmeno):
    """Funkce pro zápis do souboru"""
    ID = zjistiID()
    vyber=vyberPostavy()

    if vyber=="Warrior": postava=1 #zapíše místo slova číslo odpovídající postavě, zakterou hráč hraje - aby pak šla loadnout
    if vyber=="Scout": postava=2
    if vyber=="Mage": postava=3

    soubor = open("konfigurace.txt", "a")
    if ID<10: soubor.write("\n0")
    else: soubor.write("\n")
    soubor.write(str(ID)+";"+uzivatelskeJmeno+";"+str(postava))
    soubor.close()
    return postava

def najdiJmeno(uzivatelskeJmeno):
    """Separuje z řádku jméno a porovná jej"""
    soubor=cteniZeSouboru()
    for radek in soubor:
        radek = radek.split('\n')
        IDjmeno = radek[0]
        jmeno = IDjmeno.split(';')
        if jmeno[1] == uzivatelskeJmeno: return True
    return False

def hodKostkou(od,do):
    """Hodíme kostkou a vrátí číslo od do """
    for i in range(5):        
        print(randint(0,9),end='\r')    ##pouze vzhledový design : "jednoduchý výběr z čísel" random čísla a pak se nějaké zvolí.
        time.sleep(0.25)
    try:
        return (randint(od,do))
    except Exception as e:
        print(f"Neočekávaná vyjímka: \n{e}")
    except NameError:
        print("Rozmezi hodu neni cislo!")


      
def zmenaSmeru():
    """Zmenime smer pohybu"""
    print("\nSMER POHYBU:\n1. doprava - 2. dolu - 3. doleva - 4. nahoru\n")
    zadalSmer = False
    smerPohybu = None
    while not zadalSmer:
        smerPohybu = input("Jakym smerem chcete pokracovat: ")

        try:
           if smerPohybu == '1':
               print ("Pokracujes doprava")
           elif smerPohybu == '2':
               print ("Pokracujes dolu")
           elif smerPohybu == '3':
               print ("Pokracujes doleva")
           elif smerPohybu == '4':
               print ("Pokracujes nahoru")  
               zadalSmer = True        
           else:
               print ("Nepokracujes nikam!")

        except ValueError:
            print("Toto není číslo, zadejte číslo: ")            

        except Exception as e:
            print(f"Neočekávaná vyjímka: \n{e}")
            zadalSmer=True

def ageExploit():
	"""Funkce umožňující hrát s nedostatečným věkem."""
	print("\nMáš štěstí! Herní vývojáři dostatečně neošetřili věkovou restrikci.")
	volba = input("(1)Tvorba nebo výběr postavy.\n(R-{1})Toto je zločin! Ukončit hru.\nTvá volba: ")
	if(volba == "1"):
		user_name = input("Zadej uživatelské jméno: ")
		uzivatelExistuje = najdiJmeno(user_name)
		if uzivatelExistuje:
			print("Postava " + user_name + " načtena.") 
		else:
			print("Přidávám uživatele.")
			zapisDoSouboru(user_name)
	else:
		global age_restriction_partial_fix
		age_restriction_partial_fix = False

def reakceNaNepritele(level=1):
    """fce pro boj - nechá hráče bojovat s protivníkem, kterého určí na vstupu fce"""

    if level==1: protivnik=banditNPC()
    if level==2: protivnik=dragonNPC()
    #TODO doplnit enemy pro další levely

    print("\n[1] utéct\n[2] bojovat")
    volba=input("Vyber co uděláš: ")

    vybral=False

    while not vybral:
        try:
           volba=int(volba)
           if volba==1 or volba==2: vybral=True
        except ValueError:
           print("Toto není číslo, zadejte číslo")
        except Exception as e:
           print(f"Neočekávaná vyjímka: \n{e}")

    if volba==1:
        volba=True
        print("Házíš kostkou pro rychlost útěku 1-12")
        hod=hodKostkou(1,12)
        print("Hodil jsi: " + str(hod))
        if hod<=4:
            print("\nNepodařilo se ti utéct a protivník tě napadl! Ztrácíš 10 životů")
            hrac.odectiHP(10)
        elif hod>4:
            print("\nDnes je tvůj šťastný den, úspěšně jsi utekl před protivníkem, stálo tě to 20 energie.")
            hrac.odectiEnergy(20)
    if volba==2:
        fight(hrac,protivnik)
    else:
        volba=False

def nactiHrace(uzivatelskeJmeno):

    soubor=cteniZeSouboru()
    for radek in soubor:
        radek=radek.split('\n')
        IDjmeno=radek[0]
        jmeno=IDjmeno.split(';')
        if jmeno[1]==uzivatelskeJmeno:
            if jmeno[2]=='1':
                hrac=warrior()
            else:
                if jmeno[2]=='2':
                    hrac=scout()
                else:
                    if jmeno[2]=='3':
                        hrac=mage()                
            try:
                hrac.hp=jmeno[3];                
            except Exception as e:
                print(f"Nepodarilo se nacist ulozene data - HP\n{e}")
            try:
                hrac.damage=jmeno[4];                
            except Exception as e:
                print(f"Nepodarilo se nacist ulozene data - damage\n{e}")
            try:
                hrac.energy=jmeno[5];                
            except Exception as e:
                print(f"Nepodarilo se nacist ulozene data - energy\n{e}")

            break
    return hrac

def saveGame(hrac,uzivatelskeJmeno):
    #TODO saveGame() - naxit IS WORKING on it
    
    soubor = open("konfigurace.txt", "r")
    
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
    
    soubor = open("konfigurace.txt", "w")
    i=0
    for i in range(len(list)):
        soubor.write(list[i]+"\n")

    soubor.close()


    print("Aktualni score ulozeno")

print("Chcete hrát?")

chceHrat=input("Pokud ano zadejte Y: ")
volba=None
hod=None
if chceHrat.lower() == 'y':
    zadalVek=False
    
    while not zadalVek:
        vek=input("Zadejte svůj věk: ")
        
        try:
            if int(vek)>=18:
                print("Hra zacina")                
                uzivatelskeJmeno=input("Zadej své uživatelské jméno: ")
                uzivatelExistuje=najdiJmeno(uzivatelskeJmeno)
                if uzivatelExistuje:
                    print("uzivatel existuje")
                    hrac=nactiHrace(uzivatelskeJmeno)
                    
                else:
                    print("přidávám uživatele")
                    postava=zapisDoSouboru(uzivatelskeJmeno)
                    
                    if postava==1: hrac=warrior()
                    if postava==2: hrac=scout()
                    if postava==3: hrac=mage()

                
            elif int(vek)==17:
                print("Už jen jeden rok")
                ageExploit()

            else:
                print("Nemůžeš hrát")
                ageExploit()
                
            zadalVek=True

        except ValueError:
            print("Toto není číslo, zadejte číslo: ")            
                
        except Exception as e:
            print(f"Neočekávaná vyjímka: \n{e}")
            zadalVek=True

    print("\n======================================================")

    pokracovat=True
    
    while pokracovat and hrac.alive:
        vybral=False
        obtiznostOblasti=1
        
        while not vybral:
            print("\n[1] Hodit kostkou\n[2] Zobrazit kartu\n[3] Odejít")
            volba=input("\nZvolte akci: ")
            try:
                volba=int(volba)
                if volba==1 or volba==2 or volba==3:
                    vybral=True
            except ValueError:
                print("Toto není číslo, zadejte číslo")
            except Exception as e:
                print(f"Neočekávaná vyjímka: \n{e}")

        if volba==1:
            hod=hodKostkou(1,8)
            print("\nHodil jsi: " + str(hod) + "\n")    ##Rozmezí kostky si každý nastaví podle potřeby

            if hod==1:
                print("Nasadil jsi šnečí tempo o moc jsi se neposunul, nic zvláštního tě nepotkalo\nZtrácíš 5 energie")
                hrac.odectiEnergy(5)

            elif hod>=2 and hod<=3:
                print("Pohybuješ se kupředu\nZtrácíš 10 energie")
                hrac.odectiEnergy(10)

            elif hod>3 and hod<6:
                print("Narazil jsi na nepřítele, je to roztomilý bandita")
                reakceNaNepritele(obtiznostOblasti)

            elif hod==6:
                print("Šťastná ŠESTKA, bohužel ne zde. Z křoví na tebe vylezl drak.")
                reakceNaNepritele(obtiznostOblasti+1)
            elif hod>6:
                print("Rychlostí blesku se pohybuješ dál\nStojí tě to pouze 10 energie")
                hrac.odectiEnergy(10)

        if hrac.energy==0:
            print("\nJsi strašně unavený\nUsínáš uprostřed cesty...\nProbouzíš se alespoň trochu odpočatý\n")
            hrac.sleep()
            
        if volba==2:
            print("\nTvoje postava")
            hrac.card()

        elif volba==3:
            print("Odcházíš...")
            saveGame(hrac,uzivatelskeJmeno)
            pokracovat=False

        print("\n======================================================")
        
        
        
    if not hrac.alive:
        print("\n\nZemřel jsi\n\n")

    ##Pokracovani programu (Po volbě Odejít) nebo po ukonceni hodu.
        

else:
    print("Hra ukončena")

