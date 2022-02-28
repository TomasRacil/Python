"""
Langtonův mravenec
   -dvourozměrný univerzální Turingův stroj s jednoduchým souborem pravidel, ale komplexním chováním
"""

import turtle  # dokumentace: https://docs.python.org/3.3/library/turtle.html
import time

print('Program "Langtonův mravenec"')

# Hlavní funkce spouští varianty - s nastavením/bez nastavení
def main():
    nastaveni = input("Přejete si vstoupit do nastavení? [y/n] ")
    if nastaveni == "y":
        print("Jste v nastavení.")
        AntModified()
    elif nastaveni == "n":
        print("Pokračujeme s přednastavenými hodnotami!")
        delay()
        Ant()
    else:
        Chyba()


# Funkce nastavení - uživatel vybírá barvy a rychlost mravence
def settings():
    """
    Hlavní funkce mravence:
    -načte plátno, barvu pozadí a velikost
    - vytvoří grafického mravence, určí tvar a velikost a rychlost
    - přiřadí souřadnice pro mravence -> funkce coordinate

    Pravidla:
    - pokud mravenec ještě danou pozici nenavštívil a nebo je pozice bílá, změní se barva na černou,
     mravenec se otočí doprava a posune se
    - pokud je pozice černá, mravenec změní barvu na bílou, otočí se doleva a udělá krok dopředu

    - mravenec začíná dělat dálnici cca po 11000 cyklech, jinak program běží do nekonečna
    """
    print(
        """Výběr barev:
        [yellow, gold, orange, red, maroon,
        violet, magenta, purple, navy, blue,
        skyblue, cyan, turquoise, lightgreen, green,
        darkgreen, chocolate, brown, black, gray, white]\n"""
    )
    ScreenColor = str(input("Zadejte barvu pozadí: "))
    AntFillColor = str(input("Zadejte barvu mravence: "))
    AntSpeed = int(input("Zadejte rychlost [1-10]; nejpomalejší 1, nejrychlejší 10]: "))
    return ScreenColor, AntFillColor, AntSpeed


def Ant():
    window = turtle.Screen()
    window.bgcolor("white")
    window.screensize(2000, 2000)
    maps = {}  # slovník pro uložení souřadnice a barvy

    ant = turtle
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(10)
    ant.tracer(2, 0)
    # pro zrychlení ruší VSync - plátno se neobnovuje s frekvencí obrazovky
    # -> parametry: (počet přeskočených obnov, zpoždění)
    pos = coordinate(ant)

    for _ in range(12000):
        step = 10
        if pos not in maps or maps[pos] == "white":
            ant.fillcolor("black")
            ant.stamp()
            invert(maps, ant, "black")
            ant.right(90)
            ant.forward(step)
            pos = coordinate(ant)

        elif maps[pos] == "black":
            ant.fillcolor("white")
            invert(maps, ant, "white")
            ant.stamp()
            ant.left(90)
            ant.forward(step)
            pos = coordinate(ant)

    turtle.done()  # nezavírá plátno po dokončení cyklů


# Varianta funkce ant kdy uživatel zadává nastavení
def AntModified():
    ScreenColor, AntFillColor, AntSpeed = settings()
    delay()
    window = turtle.Screen()
    window.bgcolor(ScreenColor)
    window.screensize(2000, 2000)
    maps = {}

    ant = turtle
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(AntSpeed)
    Speed(AntSpeed, ant)
    pos = coordinate(ant)

    for _ in range(12000):
        step = 10
        if pos not in maps or maps[pos] == "white":
            ant.fillcolor(AntFillColor)
            ant.stamp()
            invert(maps, ant, "black")
            ant.right(90)
            ant.forward(step)
            pos = coordinate(ant)

        elif maps[pos] == "black":
            ant.fillcolor("white")
            invert(maps, ant, "white")
            ant.stamp()
            ant.left(90)
            ant.forward(step)
            pos = coordinate(ant)

    turtle.done()


# funkce mění barvu v závislosti na vstupní barvě
def invert(graph, ant, color):
    graph[coordinate(ant)] = color


# funkce získává aktuální pozici mravence
def coordinate(ant):
    return (round(ant.xcor()), round(ant.ycor()))


# časový odpočet načtení (nemá žádnou reálnou funkci, pouze doplněk)
def delay():
    print("Nacitam...")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)


# funkce na rychlost animace, vrací hodnoty do funkce ModifiedAnt
def Speed(AntSpeed, ant):
    if AntSpeed == 1:
        return ant.speed(1), ant.delay(50)
    elif AntSpeed == 2:
        return (ant.speed(1),)
    elif AntSpeed == 3:
        return ant.speed(2)
    elif AntSpeed == 4:
        return ant.speed(3)
    elif AntSpeed == 5:
        return ant.speed(4)
    elif AntSpeed == 6:
        return ant.speed(6)
    elif AntSpeed == 7:
        return ant.speed(10)
    elif AntSpeed == 8:
        return ant.speed(10), ant.tracer(2, 0)
    elif AntSpeed == 9:
        return ant.speed(10), ant.tracer(8, 0)
    elif AntSpeed == 10:
        return ant.speed(10), ant.tracer(60, 0)
    else:
        print("Zadali jste neznámou hodnotu!")
        return AntModified()


# funkce pro chybu vstupu
def Chyba():
    decision = input("Chyba vstupu! Chcete pokračovat? [y/n]: ")
    if decision == "y":
        return main()
    else:
        return 0


if __name__ == "__main__":
    main()
