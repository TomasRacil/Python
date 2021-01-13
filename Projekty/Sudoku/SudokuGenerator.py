
import turtle
from random import randint, shuffle
from time import sleep

# Vytvoření prázdného 2D pole
bod = []
for radek in range(0, 9):
    bod.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
cislaSeznam = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0 # počítá počet řešní

myPen = turtle.Turtle()
myPen._tracer(0) # rovnou zobrazít celé sudoku
myPen.speed(0) # zajistí maximální rychlost vypisování
myPen.color("black")
myPen.hideturtle()
topLeft_x = -150 # Jenom pomocna, pro zobrazení na monitoru
topLeft_y = 150

def text(message, x, y, size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x, y)
    myPen.write(message, align="left", font=FONT)

def drawbod(bod):
    intDim = 40 # šířka = délka řádku, slopce
    for rad in range(0, 10):
        if (rad % 3) == 0:# Podmínka zajišťující vykreslení tučné čáry
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


# Funkce kontrolující zaplnění políček
def checkBod(bod):
    for rad in range(0, 9):
        for slo in range(0, 9):
            if bod[rad][slo] == 0:
                return False
    return True

#Tady jsem spojil funkci pro plnění bodu a řešení bodu oproti původnímu projektu do jedné a to pomocí proměnné varianta
def praceBod(bod, varianta):
    global counter
    for i in range(0, 81):
        rad = i // 9 # klasické dělení
        slo = i % 9 # modulo, zbytek po dělení, takže postupně budou hodnoty 1,2,3
        if bod[rad][slo] == 0:
            shuffle(cislaSeznam) # míchá seznam, aby nedocházelo k 1234..
            for value in (cislaSeznam):
                if not (value in bod[rad]): #kontroluje jestli je v radku
                    # kontroluje, zdali jsou hodnoty v jednotlivých sloupcíh, místo výpisu po prvcích jsem zvolil tuhle kontrolu cyklem
                    if not value in (bod[n][slo] for n in range(0, 8)):
                        square = []
                        # kontroluje, v jakém čtverci se pohybujeme, pro kontrolu, jestli číslo již není použito
                        if rad < 3:
                            if slo < 3:
                                square = [bod[i][0:3] for i in range(0, 3)]
                            elif slo < 6:
                                square = [bod[i][3:6] for i in range(0, 3)]
                            else:
                                square = [bod[i][6:9] for i in range(0, 3)]
                        elif rad < 6:
                            if slo < 3:
                                square = [bod[i][0:3] for i in range(3, 6)]
                            elif slo < 6:
                                square = [bod[i][3:6] for i in range(3, 6)]
                            else:
                                square = [bod[i][6:9] for i in range(3, 6)]
                        else:
                            if slo < 3:
                                square = [bod[i][0:3] for i in range(6, 9)]
                            elif slo < 6:
                                square = [bod[i][3:6] for i in range(6, 9)]
                            else:
                                square = [bod[i][6:9] for i in range(6, 9)]
                        if not value in (square[0] + square[1] + square[2]):
                            #Samotné rozdělení variant, pro jednu funkci, která pracuje s bodem
                            if(varianta==1):
                                bod[rad][slo] = value
                                if checkBod(bod):
                                    counter += 1
                                    break
                                else:
                                    if praceBod(bod,varianta):
                                        return True
                            else:
                                bod[rad][slo] = value
                                if checkBod(bod):
                                    return True
                                else:
                                    if praceBod(bod,varianta):
                                        return True
            break
    bod[rad][slo] = 0

#Funkce, která po naplnění začně náhodně mazat hodnoty v políčku a zároveň kontroluje možný počet řešení, tedy, aby byla splněna podmínka
# jednoho řešení
def vymazBod(bod, obtiznost):
    # těžkopádné nastavení obtížnosti, závislé na volbě uživatele
    pokusy=20+obtiznost*10
    while pokusy > 0:
        # vybírám jednotlivá náhodná políčka
        rad = randint(0, 8)
        slo = randint(0, 8)
        while bod[rad][slo] == 0:
            rad = randint(0, 8)
            slo = randint(0, 8)
        backup = bod[rad][slo]
        bod[rad][slo] = 0
        copybod = []
        for r in range(0, 9):
            copybod.append([])
            for c in range(0, 9):
                copybod[r].append(bod[r][c])
        #Zde dochází ke kontrolej jednoho řešení
        praceBod(copybod,1)
        if counter != 1:
            pokusy -= 1
# přidání mainu
def main():
    print("V případě zájmu udělejte prosím výstřižek sudoku")
    obtiznost = int(input("Zadejte obtiznost (1-3): \n"))
    if(obtiznost>3):
        print(f"Zvolili jste spatnou obtiznost")
    elif(obtiznost<1):
        print(f"Zvolili jste spatnou obtiznost")
    #Zde probíhá plnění samotného Sudoku
    praceBod(bod,2)
    vymazBod(bod, obtiznost)
    myPen.getscreen().update()
    # vykreslení samotného sudoku
    drawbod(bod)
    sleep(10)
    print("Sudoku bod Ready")
    for sloupec in range(0,9):
            print(f"{bod[sloupec][0]} {bod[sloupec][1]} {bod[sloupec][2]} | {bod[sloupec][3]} {bod[sloupec][4]} {bod[sloupec][5]} | {bod[sloupec][6]} {bod[sloupec][7]} {bod[sloupec][8]}")
            if (sloupec % 3 == 2):
                print("_____________________")

if __name__ == '__main__':
    main()