
import turtle
from random import randint, shuffle
from time import sleep

#Vytvoření prázdného 2D pole

bod = []
for radek in range(0,9):
    bod.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

myPen = turtle.Turtle()
myPen._tracer(0) #rovnou zobrazít celé sudoku
myPen.speed(0) #0 zajistí maximální rychlost vypisování
myPen.color("black")
myPen.hideturtle()
topLeft_x = -150#Jenom pomocna, pro zobrazení na monitoru
topLeft_y = 150


def text(message, x, y, size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x, y)
    myPen.write(message, align="left", font=FONT)

def drawbod(bod):
    intDim = 40 # šířka = délka řádku, slopce
    for rad in range(0, 10):
        if (rad % 3) == 0:#Podmínka zajišťující vykreslení tučné čáry
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        myPen.goto(topLeft_x, topLeft_y - rad * intDim)# začínající souřadnice odkud bude kreslit
        myPen.pendown()
        myPen.goto(topLeft_x + 9 * intDim, topLeft_y - rad * intDim)# Finální souřadnice, kam až kreslí
    for slo in range(0, 10):
        if (slo % 3) == 0:# Podmínka zajišťující vykreslení tučné čáry
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        myPen.goto(topLeft_x + slo * intDim, topLeft_y) # Souřadnice startu
        myPen.pendown()
        myPen.goto(topLeft_x + slo * intDim, topLeft_y - 9 * intDim) # Souřadnice konce

    for rad in range(0, 9):
        for slo in range(0, 9):
            if bod[rad][slo] != 0:
                text(bod[rad][slo], topLeft_x + slo * intDim + 9, topLeft_y - rad * intDim - intDim + 8, 20)
