import turtle  # dokumentace: https://docs.python.org/3.3/library/turtle.html
from .Helpers import invert, coordinate, delay


def AntModified():
    """
    Varianta funkce ant kdy uživatel zadává nastavení
    """
    ScreenColor, AntFillColor, AntSpeed = settings()

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
    delay()
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


def settings():
    """
    Funkce nastavení - uživatel vybírá barvy a rychlost mravence

    Returns:
        functions: Funkce nastavení barvy obrazovky, barvy mravence a rychlosti mravence
    """
    print(
        """
        Výběr barev:
        [yellow, gold, orange, red, maroon,
        violet, magenta, purple, navy, blue,
        skyblue, cyan, turquoise, lightgreen, green,
        darkgreen, chocolate, brown, black, gray, white]
        """
    )
    ScreenColor = str(input("Zadejte barvu pozadí: "))
    AntFillColor = str(input("Zadejte barvu mravence: "))
    AntSpeed = int(input("Zadejte rychlost [1-10]; nejpomalejší 1, nejrychlejší 10]: "))
    return ScreenColor, AntFillColor, AntSpeed


def Speed(AntSpeed, ant):
    """
    funkce na rychlost animace, vrací hodnoty do funkce ModifiedAnt

    Args:
        AntSpeed (int): rychlost vykrelování
        ant (turtle): objekt vykreslení

    Returns:
        function: Funkce, která inicializuje modifikovaný objekt vykreslení
    """

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
