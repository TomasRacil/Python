import turtle
from random import randint, shuffle
from time import sleep
bod = []
for radek in range(0, 9):
    bod.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

myPen = turtle.Turtle()
myPen._tracer(0) # rovnou zobrazít celé sudoku
myPen.speed(0) # zajistí maximální rychlost vypisování
myPen.color("black")
myPen.hideturtle()
topLeft_x = -150
topLeft_y = 150

def text(message, x, y, size):
    """Nastavení textu - funkce se volá během vykreslení
    Args:
        messsage --- list k vykreslení
        x --- x souradnice pro vykreslení
        y --- y souradnice pro vykreslení
        size --- velikost samotného písma

    Returns:
        vypsaný text
    """
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x, y)
    myPen.write(message, align="left", font=FONT)

def drawbod(bod):
    """Vykresluje celé sudoku a v závěru volá funkci text, která do vykresleného pole doplní jednnotlivá čísla
        Args:
            bod --- list, dvourozměrné pole
        Returns:
            Turtle - graficky znázorněné sudoku
        """
    intDim = 40 # šířka = délka řádku, slopce
    for rad in range(0, 10):
        if (rad % 3) == 0:
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        """Začínající souřadnice odkud bude kreslit"""
        myPen.goto(topLeft_x, topLeft_y - rad * intDim)
        myPen.pendown()
        """Finální souřadnice, kam až kreslí"""
        myPen.goto(topLeft_x + 9 * intDim, topLeft_y - rad * intDim)
    for slo in range(0, 10):
        if (slo % 3) == 0:
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        """Souřadnice startu"""
        myPen.goto(topLeft_x + slo * intDim, topLeft_y)
        myPen.pendown()
        myPen.goto(topLeft_x + slo * intDim, topLeft_y - 9 * intDim) # Souřadnice konce

    for rad in range(0, 9):
        for slo in range(0, 9):
            if bod[rad][slo] != 0:
                text(bod[rad][slo], topLeft_x + slo * intDim + 9, topLeft_y - rad * intDim - intDim + 8, 20)
    myPen.getscreen().update()
    sleep(10)