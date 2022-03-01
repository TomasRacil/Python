import time


def invert(graph, ant, color):
    """
    funkce mění barvu v závislosti na vstupní barvě

    Args:
        graph (dict): ?
        ant (turtle): objekt vykreslení
        color (string): barva ... ?
    """
    graph[coordinate(ant)] = color


def coordinate(ant):
    """
    funkce získává aktuální pozici mravence

    Args:
        ant (turtle): objekt vykreslení

    Returns:
        tuple(int,int): (x-ová pozice, y-ová pozice)
    """
    return (round(ant.xcor()), round(ant.ycor()))


def delay():
    """
    Tato funkce slouží jako časový odpočet načtení
    (nemá žádnou reálnou funkci, pouze doplněk do programu)
    """
    print("Nacitam...")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
