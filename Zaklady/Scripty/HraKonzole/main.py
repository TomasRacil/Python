uzivatelskeJmeno=None
age_restriction_partial_fix = True

from random import randint
import time

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
	postava=vyberPostavy()
	soubor = open("konfigurace.txt", "a")
	if ID<10: soubor.write("\n0")
	else: soubor.write("\n")
	soubor.write(str(ID)+";"+uzivatelskeJmeno+";"+postava)
	soubor.close()

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

   # print("Program pokracuje")

    volba=False    
	if(not age_restriction_partial_fix): #Ukončí program, hra vůbec nezačne.
		volba = True
    while not volba:
        volba=input("Zvolte další akci:\nHodit kostkou: 1   \nOdejít: 2\n")
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
                            break
                        elif hod>4:
                            print("Dnes je tvůj šťastný den, úspěšně jsi utekl před banditem, stálo tě to 2 energie.")
                            ##energie=energie-2
                            break
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

