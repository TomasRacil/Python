from GameEngine import *

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