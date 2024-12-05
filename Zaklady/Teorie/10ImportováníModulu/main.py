"""
Importování modulů je zcela klíčové v každém programovacím jazyce.
Umožňuje nám využívat mnoha modulů vytvořených komunitou, 
nebo zpřehlednit náš kód rozdělením do jednotlivých modulů.
Výchozí bod aplikace většinou v pythonu nazýváme main a nebo run.
Tento bod pak importuje spouští samotnou aplikace a importuje všechny potřebné moduly 
funkce a nebo třídy.
Běžný standart je uvádět importy v horní části scriptu, ovšem z technického hlediska je možné importovat kdekoliv.
Přehlednost je hlavním důvodem proč se nedoporučuje importovat moduly, kde se nám lbí. 
Navíc se také může stát, že při špatné strategii importů začne docházet ke kruhovým závislostem,
kdy první modul importuje druhý a druhý modul opět první, takový pragram se nespustí.
"""

# v případě že je modul nainstalovaný používáme pro importování použijem výraz import následovaný jménem modulu
import os

# přístup k proměnné modulu os
print(os.__doc__ + "\n")

# pokud chceme z modulu importovat jen některé prvky nebo použijeme výraz from následovaný jednotlivými prvky oddělenými čárkou
from sys import path, platform

print(platform.__doc__ + "\n")

# pokud jde o námi definovaný script je nutné použít výraz from a uvést jeho lokaci
# následovanou názvem importovaného prvku/prvků
from funkce1 import importovanaFunkce1

print(importovanaFunkce1.__doc__ + "\n")

# pokud chceme importovat všechny prvky použijeme  symbol *
from funkce2 import *

print(importovanaFunkce2.__doc__)
print(importovanaFunkce3.__doc__ + "\n")

# importování ze složek vypadá následovně
from slozka.DruhaTrida import DruhaTrida

print(DruhaTrida.__doc__ + "\n")

# tento způsob je poměrně nešikovný a proto používáme speciaální script __init__.py,
# kterým je definován modul a zaznamenává v sobě všechny exportované prvky pro daný modul,
# takže pak stačí iportovat daný modul a máme přístup ke všem prvkům
from prvniModul import *

print(PrvniTrida.__doc__ + "\n")

# Zatím každý import co jsem zde demonstroval používal takzvaného absolutního způsobu importu
# protože tento script sám není součástí modulu. V jeho mateřské složce není vytvořen __init__.py


# Relativní import můžeme vidět například u funkce relativniVolani(),
# která je exportována pomocí __init__.py prvního podmodulu a následně prního modulu
relativniVolani()

# Další relativní import je uveden druhaFunkceVPodmodulu()
druhaFunkceVPodmodulu()

# Pro lepší názornost jsou vytvořené podobné funkce, které nejsou v modulu a proto musí používat relativního importu
from slozka.prvniPodslozka.funkceVPodslozce import absolutniVolani

absolutniVolani()

from slozka.prvniPodslozka.druhaFunkceVPodslozce import druhaFunkceVPodslozce

druhaFunkceVPodslozce()
