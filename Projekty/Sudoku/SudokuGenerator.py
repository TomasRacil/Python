
import turtle
from random import randint, shuffle
from time import sleep

#Vytvoření prázdného 2D pole

bod = []
for radek in range(0,9):
    bod.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

myPen = turtle.Turtle()
myPen._tracer(0) #rovnou zobrazít celé sudoku
myPen.speed(0) #0 zajistí maximální rychlost vypisování
myPen.color("black")
myPen.hideturtle()
topLeft_x = -150  # Jenom pomocna, pro zobrazení na monitoru
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

def naplnBod(bod):
    #global counter
    for i in range(0, 81):
        rad = i // 9
        slo = i % 9
        if bod[rad][slo] == 0:
            shuffle(numberList)
            for value in numberList:
                if not (value in bod[rad]):
                    pass                        # Zatim pass aby nevyhazoval chybu pri sestaveni nez se funkce dodela

""" Nedodelane funkce vyhazuji error
def resBod(bod):
    global counter   
    

def vymaz(bod, obtiznost):
    
"""

def main():
    obtiznost = 10*int(input("Zadejte obtiznost (1-10): \n"))
    drawbod(bod)
    counter = 1
    sleep(5)
    print("Sudoku bod Ready")
    for slopec in range(0,9):
            print(f"{bod[slopec][0]} {bod[slopec][1]} {bod[slopec][2]} | {bod[slopec][3]} {bod[slopec][4]} {bod[slopec][5]} | {bod[slopec][6]} {bod[slopec][7]} {bod[slopec][8]}")
            if (slopec % 3 == 2):
                print("_____________________")

if __name__ == '__main__':
    main()