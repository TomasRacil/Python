"""
Langtonův mravenec
 -dvourozměrný univerzální Turingův stroj s jednoduchým souborem pravidel, ale komplexním chováním
"""

from modules import Ant
from modules import AntModified


def Chyba():
    """
    funkce pro chybu vstupu
    """
    decision = input("Chyba vstupu! Chcete pokračovat? [y/n]: ")
    if decision == "y":
        return main()
    else:
        return 0


def main():
    """
    Hlavní funkce spouští varianty - s nastavením/bez nastavení
    """

    print('Program "Langtonův mravenec"')

    nastaveni = input("Přejete si vstoupit do nastavení? [y/n] ")

    if nastaveni == "y":
        print("Jste v nastavení.")
        AntModified()

    elif nastaveni == "n":
        print("Pokračujeme s přednastavenými hodnotami!")
        Ant()

    else:
        Chyba()


if __name__ == "__main__":
    main()
