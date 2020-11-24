"""
Tento script má za úkol předvést standartní způsob psaní prvního scriptů v programu python a také vysvětlit základní syntax.
Je zde uveden ideální způsob ne vše je nutné implementovat do vlastního řešení.
"""

"""
V prních řádcích je vhodné uvést některé základní informace o samotném scriptu. 
V tomto případě je to virtuální prostředí a verze pythonu a další odrážky není nutné vysvětlovat.
"""
#!/usr/bin/env python3
# File name: Program.py
# Description: Basic format for Python scripts
# Author: Tomáš Ráčil
# Date: 19-11-2020


"""
V "hlavičce" se uvádí importy jednotlivých scriptů/knihoven/tříd ve dvou až třech blocích, každý blok by měl být abecedně seřazen. 
Je zde také možné importovat konkrétní prvky knihoven pomocí from a import.
První blok jsou základní knihovny/třidy poskytované v pythonu. 
Do druhého se dávají knihovny/třídy vytvořené jinými uživateli poskytované v rámci standartní distibuce např. pip.
Třetí blok slouží k importu vlastních knihoven/scriptů/třid.
"""

import argparse
import logging
from logging import critical, error, info, warning, debug
import sys

"""
Po importech mohou následovat proměnné sdílené napříč celým scriptem, ale podobně jako v jiných jazycích by jejich využívání mělo být omezeno na minimum.
"""

"""
Následují definice funkcí. 
Jak je možné vidět, narozdíl od mnoha jiných jazyků, python používá odszení pro definování jednotlivých bloků kódu.
U každé funkce by v ideálním případě měl být komentář vysvětlující její fungování.
"""
def parse_arguments():
    """Read arguments from a command line."""
    parser = argparse.ArgumentParser(description='Arguments get parsed via --commands') 
    parser.add_argument('-v', metavar='verbosity', type=int, default=2,
        help='Verbosity of logging: 0 -critical, 1- error, 2 -warning, 3 -info, 4 -debug')

    args = parser.parse_args()
    verbose = {0: logging.CRITICAL, 1: logging.ERROR, 2: logging.WARNING, 3: logging.INFO, 4: logging.DEBUG}
    logging.basicConfig(format='%(message)s', level=verbose[args.v], stream=sys.stdout)
    
    return args
    
    
def main():
    print(args)

"""
Na závěr scriptu použijeme podmínku, která spustí náš script. Tato podmínka porovnává proměnnou __name__, která se vytváří při zavolání scriptu. 
Pokud se jedná o první interpretovaný script, je nastavena na hodnotu __main__. 
Pokud je volána z jiného scriptu je nastavena na její vlastní jméno (jméno scriptu).
Následně je volána funkce pro získání argumentů z příkazové řádky a hlavní funkce.
"""

if __name__ == '__main__':
    args = parse_arguments()
    main()
