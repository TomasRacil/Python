from os import path

# from Ponorka import Ponorka
from PomocneTridy import *

with open(path.join(path.dirname(path.realpath(__file__)), "test.txt"), "r") as soubor:
    ponorka = Ponorka()
    for radek in soubor.readlines():
        ponorka.naviguj(radek)
    print(ponorka.vysledek())

datum = Datum(2024, 12, 4)
print(datum)
