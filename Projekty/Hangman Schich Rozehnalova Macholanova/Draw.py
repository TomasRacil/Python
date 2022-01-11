import turtle as t  #Knihovna na grafiku
import Score as S

screen = t.getscreen()  #zobrazení turtle okna
global mistake
mistake = 0
global name
name = ""
global user
user =""
global multiply
multiply = 0
global lead
lead = ""
global CharList
CharList = []
global count
count = 0
n = -1

def getWord(wrd = ""):
    global word
    word = wrd

def initialize(): #This sets up the background and settings for the game
    global word
    t.speed(0) #This creates the settings
    screen.tracer(0)
    t.hideturtle()
    t.setworldcoordinates(20,20,80,80)

    t.penup() #This draws a gallow
    t.setpos(55,45)
    t.pendown()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(5)

    t.penup()
    t.setpos(35,30)
    t.left(90)
    for i in range(len(word) - 1): #Podtržítka pod písmenama - podle počtu písmen
        t.pendown()
        t.forward(2)    #délka podtžítka pod písmenem
        t.penup()
        t.forward(2)    #délka mezery mezi podtržítky

def drawLetter(word,character):     #Funkce je zavolána, pokud uživatel správně uhodne písmeno. Kraslí písmeno
    global count
    global CharList
    times = [x for x, appearance in enumerate(word) if appearance == character] #vytvoří list když znak se objevuje ve slově 'slovo' --> "o" [3, 5]
    for i in range(len(times)): #nakreslí písmeno podle toho, kde se nachází ve slově (pozice)
        t.penup()
        t.setpos(36 + 4 * (times[i]), 31) # 4* --> rozestupy # 'slovo' --> 'l', (x = 36 + 4*2,y = 31)
        t.write(character, move=True, align='center', font=('Arial', 20, 'normal'))
        if character not in CharList:
            CharList.append(character)
            count += len(times)

def drawBody():  #Funkce je zavolána, pokud uživatel chybně tipne písmeno. Kreslí části tělo oběšence  
    global n
    t.setheading(270)
    t.penup()
    if n == 0: #HLAVA
        t.setpos(45,60)
        t.right(90)
        t.pendown()
        t.circle(3,360,500)
        t.penup()
    elif n == 1: #TORSO
        t.setpos(45,54)
        t.pendown()
        t.forward(8)
        t.penup()
    elif n == 2: #LEVÁ RUKA
        t.setpos(45,51)
        t.right(135)
        t.pendown()
        t.forward(6)
        t.penup()
    elif n == 3: #PRAVÁ RUKA
        t.setpos(45,51)
        t.left(135)
        t.pendown()
        t.forward(6)
        t.penup()
    elif n == 4: #LEVÁ NOHA
        t.setpos(45,46)
        t.right(45)
        t.pendown()
        t.forward(6)
        t.penup()
    elif n == 5: #PRAVÁ NOHA
        t.setpos(45,46)
        t.left(45)
        t.pendown()
        t.forward(6)
        t.penup()

def guess(): #Uživatelský vstup
    global word
    global n
    global mistake
    global count
    character = t.textinput('Tvůj tip','Tipni si písmeno\'') #ptáme se přes 'message box'
    character = character.lower()        #Poku uživatel zadá velké písmeno změní se na malé
    if character in word: #Pokud písmeno je ve slově, nakreslí písmeno
        drawLetter(word,character)
    else: #Pokud písmeno není ve slově, přikreslí se část oběšence
        drawBody()
        n += 1
        mistake += 1
        S.getMistake(mistake)

def fake_main():
    global n
    global count
    global word
    n = 0
    global CharList

    initialize()
    done = False
    count = 0
    while not done:
        if n > 5:
            done = True
            t.penup()
            t.setpos(50,70)
            t.write('Prohra.' + 'Slovo bylo \'' + word + '\'', move=True, align='center', font=('Arial', 10, 'normal'))
            CharList = [""]
        elif count == len(word) - 1: # -> upravuje delku slova o -1 --> na konci řádku je enter
            CharList = [""]          # --> vyprázníme list pro nové slovo   
            done = True
            t.penup()
            t.setpos(50,70)
            t.write('Super! Uhodl jsi slovo \'' + word + '\'. Vyhrál jsi!', move=True, align='center', font=('Arial', 10, 'normal'))
        else:
            guess()
    return None