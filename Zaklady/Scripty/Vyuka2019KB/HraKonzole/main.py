import time
from playsound import playsound
from random import randint
from datetime import date

from GameEngine import *
from Characters import *

print("Vítejte v náší dobrodružné hře")

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("Dnes je krásný den s datumem ", d1)

uzivatelskeJmeno=None

def hodKostkou(od,do):
   """Hodíme kostkou a vrátí číslo od do """
   ZvukKostka() 
   for i in range(5):        
       print(randint(0,9),end='\r')    ##pouze vzhledový design : "jednoduchý výběr z čísel" random čísla a pak se nějaké zvolí.
       time.sleep(0.25)
   try:
       return (randint(od,do))
   except Exception as e:
       print(f"Neočekávaná vyjímka: \n{e}")
   except NameError:
       print("Rozmezi hodu neni cislo!")


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
            
            elif hod==4:
                print("Dostal si chuť na trénink. Snad si nic neuděláš...\n")
                train(hrac)

            elif hod>4 and hod<6:
                print("Narazil jsi na nepřítele, je to roztomilý bandita")
                ZvukBandita()
                reakceNaNepritele(obtiznostOblasti)

            elif hod==6:
                print("Šťastná ŠESTKA, bohužel ne zde. Z křoví na tebe vylezl drak.")
                ZvukDrak()
                reakceNaNepritele(obtiznostOblasti+1)
            elif hod>6 and hod <=7:
                print("Rychlostí blesku se pohybuješ dál\nStojí tě to pouze 10 energie")
                ZvukRychlost()
                hrac.odectiEnergy(10)

            elif hod==8:
                print("Narazil si na kašnu s živou vodou\nJak moc se napiješ záleží na štěstí: ")
                ZvukVoda()
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
        ZvukSmrt()

    ##Pokracovani programu (Po volbě Odejít) nebo po ukonceni hodu.

else:
    print("Hra ukončena")
      
