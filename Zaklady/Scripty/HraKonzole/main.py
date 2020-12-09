import time
from random import randint
from datetime import date

from GameEngine import *

print("Vítejte v náší dobrodružné hře")

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("Dnes je krásný den s datumem ", d1)

uzivatelskeJmeno=None

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

    def prictiHP(self, kolik):
        self.hp+=kolik

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
    def sleep(self):  
        hod=hodKostkou(1,8)
        print("\nHodil jsi: " + str(hod) + "\n")   

        if hod==1:
            print("Během spánku jsi byl přepaden. \nNezískal jsi žádnou energii")
               

        elif hod==2:
                print("Sotva jsi zamhouřil oči, okolní rámus tvému spánku rozhodně nedopřál!\nZískáváš 30 energie")
                self.energy=30
        elif hod==3:
            print("V průběhu spánku ses několikrát probudil kvůli nočním můrám !\nZískáváš 60 energie")
            self.energy=60

        elif hod==4 or hod==5:
            print("Po několika hodinách se probouzíš, ale spaní na tvrdé podložce nebylo to pravé!\nZískáváš 90 energie")
            self.energy=90

        elif hod==6:
           print("Bylo ti nabídnuto lůžko v blízkém hostinci, takhle dobře ses už dlouho nevyspal!\nZískáváš 120 energie")
           self.energy=120


class scout(character):
    def __init__(self,hp=50,energy=150,damage=20):
        self.type=2
        self.hp=hp
        self.energy=energy
        self.damage=damage

    def heal(self): self.hp=50
    def sleep(self):  
        hod=hodKostkou(1,8)
        print("\nHodil jsi: " + str(hod) + "\n")   

        if hod==1:
            print("Během spánku jsi byl přepaden. \nNezískal jsi žádnou energii")
               

        elif hod==2:
                print("Sotva jsi zamhouřil oči, okolní rámus tvému spánku rozhodně nedopřál!\nZískáváš 30 energie")
                self.energy=30
        elif hod==3:
            print("V průběhu spánku ses několikrát probudil kvůli nočním můrám !\nZískáváš 60 energie")
            self.energy=60

        elif hod==4 or hod==5:
            print("Po několika hodinách se probouzíš, ale spaní na tvrdé podložce nebylo to pravé!\nZískáváš 90 energie")
            self.energy=90

        elif hod==6:
           print("Bylo ti nabídnuto lůžko v blízkém hostinci, takhle dobře ses už dlouho nevyspal!\nZískáváš 120 energie")
           self.energy=120

class mage(character):
    def __init__(self,hp=65,energy=100,damage=110):
        self.type=3
        self.hp=hp
        self.energy=energy
        self.damage=damage

    def heal(self): self.hp=65
    def sleep(self):  
        hod=hodKostkou(1,8)
        print("\nHodil jsi: " + str(hod) + "\n")   

        if hod==1:
            print("Během spánku jsi byl přepaden. \nNezískal jsi žádnou energii")
               

        elif hod==2:
                print("Sotva jsi zamhouřil oči, okolní rámus tvému spánku rozhodně nedopřál!\nZískáváš 30 energie")
                self.energy=30
        elif hod==3:
            print("V průběhu spánku ses několikrát probudil kvůli nočním můrám !\nZískáváš 60 energie")
            self.energy=60

        elif hod==4 or hod==5:
            print("Po několika hodinách se probouzíš, ale spaní na tvrdé podložce nebylo to pravé!\nZískáváš 90 energie")
            self.energy=90

        elif hod==6:
           print("Bylo ti nabídnuto lůžko v blízkém hostinci, takhle dobře ses už dlouho nevyspal!\nZískáváš 120 energie")
           self.energy=120

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
                hrac.hp=int(jmeno[3]);                
            except Exception as e:
                print(f"Nepodarilo se nacist ulozene data - HP\n{e}")
            try:
                hrac.damage=int(jmeno[4]);                
            except Exception as e:
                print(f"Nepodarilo se nacist ulozene data - damage\n{e}")
            try:
                hrac.energy=int(jmeno[5]);                
            except Exception as e:
                print(f"Nepodarilo se nacist ulozene data - energy\n{e}")

            break
    hrac.card()    
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
    soubor.write(list[0])
    
    for i in range(len(list)):
        if not i==0: soubor.write("\n"+list[i])
    soubor.close()

    print("Aktualni score ulozeno")
    hrac.card()

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

    print("\n=======================================================")

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
            elif hod>6 and hod <=7:
                print("Rychlostí blesku se pohybuješ dál\nStojí tě to pouze 10 energie")
                hrac.odectiEnergy(10)

            elif hod==8:
                print("Narazil si na kašnu s živou vodou\nJak moc se napiješ záleží na štěstí: ")
                hod=hodKostkou(1,6)
                if hod<=2:
                    print("No to si se moc nenapil, pričetlo se ti 10 životů")
                    hrac.prictiHP(10)
                elif hod==3:
                    print("Přiměřeně si se napil, alespoň zbyde i na ostatní, pričetlo se ti 20 životů")
                    hrac.prictiHP(20)
                elif hod>=4:
                    print("Teda nemusel si vypít všechno, pričetlo se ti 30 životů")
                    hrac.prictiHP(30)

        if hrac.energy==0:
            print("\nJsi strašně unavený\nUsínáš uprostřed cesty...\nProbouzíš se alespoň trochu odpočatý\n")
            hrac.sleep()
            
        if volba==2:
            print("\nTvoje postava")
            hrac.card()

        elif volba==3:
            print("Odcházíš...")
            try:
                saveGame(hrac,uzivatelskeJmeno)
            except Exception as e:
                print(f"Neočekávaná vyjímka: Hra neulozena, kontaktujte Naxit\n{e}")
            pokracovat=False

        print("\n======================================================")
        
        
        
    if not hrac.alive:
        print("\n\nZemřel jsi\n\n")

    ##Pokracovani programu (Po volbě Odejít) nebo po ukonceni hodu.

else:
    print("Hra ukončena")
      
