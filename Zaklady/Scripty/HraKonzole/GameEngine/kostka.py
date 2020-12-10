from GameEngine import *

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

