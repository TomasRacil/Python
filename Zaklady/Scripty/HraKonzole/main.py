uzivatelskeJmeno=None
from random import randint
import time

def cteniZeSouboru(soubor="konfigurace.txt"):
    """Funkce pro čtení ze souboru"""
    soubor = open(soubor, "r")    
    return soubor

def zapisDoSouboru(uzivatelskeJmeno):
    """Funkce pro zápis do souboru"""
    soubor = open("konfigurace.txt", "a")
    soubor.write("\n"+uzivatelskeJmeno)
    soubor.close()

def najdiJmeno(uzivatelskeJmeno):
    soubor=cteniZeSouboru()
    for radek in soubor:
        if radek == uzivatelskeJmeno:
            return True
        
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
                    
                else:
                    print("přidávám uživatele")
                
                zapisDoSouboru(uzivatelskeJmeno)

                
            elif int(vek)==17:
                print("Už jen jeden rok")

            else:
                print("Nemůžeš hrát")
                
            zadalVek=True

        except ValueError:
            print("Toto není číslo, zadejte číslo: ")            
                
        except Exception as e:
            print(f"Neočekávaná vyjímka: \n{e}")
            zadalVek=True

   # print("Program pokracuje")

    volba=False    
    while not volba:
        volba=input("Zvolte další akci:\nHodit kostkou: 1   \nOdejít: 2")
        if volba=='1':
            hod=hodKostkou(1,8)
            print("Hodil jsi: " + str(hod))    ##Rozmezí kostky si každý nastavý podle potřeby
            volba=True
            if hod<=2:
                print("Nasadil jsi šnečí tempo o moc jsi se neposunul, nic zvláštního tě nepotkalo")
            elif hod>2 and hod<=5:
                print("Pohybuješ se kupředu")
            elif hod==6:
                print("Šťastná ŠESTKA, bohužel ne zde. Z křoví na tebe vylezl bandita.")
                volba=False
                while not volba:            
                    volba=input("Vyber co uděláš:\n 1 utéct\n 2 bojovat")
                    if volba=='1':
                        volba=True
                        print("Házíš kostkou pro rychlost útěku 1-12")
                        hod=hodKostkou(1,12)
                        if hod<=4:
                            print("Nepodařilo se ti utéct")
                            ##Zivot--
                        elif hod>4:
                            print("Dnes je tvůj šťastný den, úspěšně jsi utekl před banditem, stálo tě to 2 energie.")
                            ##energie=energie-2
                    if volba=='2':
                        volba=True
                        print("Házíš kostkou kolik tě toto rozhodnutí bude stát životu (nejvýše však 3)")
                        hod=hodKostkou(-1,3)
                        if hod<0:
                            print("Fuuha, jak se říká, co tě nezabije to tě posílí. Získáváš jeden život navíc.")
                            ##Zivot++
                        elif hod==0:
                            print("Použil jsi své umění KungFu a úspěšně jsi se vyhnul všem útokům bandity")
                        else:
                            print("Něco tě škráblo ztrácíš : "+hod+"životů")
                            ##Zivoty=Zivoty-hod
                            ##if Zivoty<=0 print("KONEC HRY - ZEMŘEL JSI")
                    else:
                        volba=False
            elif hod>6:
                print("Rychlostí blesku se pohybuješ dál")
                ##energie-2
                        
        elif volba=='2':
            print("Odcházíš...")
            volba=True
        else:
            volba=False
            print("Zadej znovu")
        
        
        

    ##Pokracovani programu (Po volbě Odejít) nebo po ukonceni hodu.
        

else:
    print("Hra ukončena")

