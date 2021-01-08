
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

def kontrolBod(bod):
    for rad in range(0, 9):
        for slo in range(0, 9):
            if bod[rad][slo] == 0:
                return False
    return True

def naplnBod(bod):
    global counter
    for i in range(0, 81):
        rad = i // 9 #i děleno 9 - 1/9 = 0 rad
        slo = i % 9 #i modulo 9 - 1 mod 9 = 1
        if bod[rad][slo] == 0:
            shuffle(numberList)
            for value in numberList:
                if not (value in bod[rad]):
                    # Check that this value has not already be used on this sloumn
                    if not value in (
                            bod[0][slo], bod[1][slo], bod[2][slo], bod[3][slo], bod[4][slo], bod[5][slo], bod[6][slo],
                            bod[7][slo], bod[8][slo]):
                        # Identify which of the 9 squares we are working on
                        square = []
                        if rad < 3:
                            if slo < 3:square = [bod[i][0:3] for i in range(0, 3)]
                            elif slo < 6:square = [bod[i][3:6] for i in range(0, 3)]
                            else:square = [bod[i][6:9] for i in range(0, 3)]
                        elif rad < 6:
                            if slo < 3:square = [bod[i][0:3] for i in range(3, 6)]
                            elif slo < 6:square = [bod[i][3:6] for i in range(3, 6)]
                            else:square = [bod[i][6:9] for i in range(3, 6)]
                        else:
                            if slo < 3:square = [bod[i][0:3] for i in range(6, 9)]
                            elif slo < 6:square = [bod[i][3:6] for i in range(6, 9)]
                            else:square = [bod[i][6:9] for i in range(6, 9)]
                        # Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                            bod[rad][slo] = value
                            if kontrolBod(bod):return True
                            else:
                                if naplnBod(bod):return True
                break
        bod[rad][slo] = 0


def resBod(bod):
    global counter

def vymaz(bod, obtiznost):


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