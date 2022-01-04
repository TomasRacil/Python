import turtle as t  #Knihovna na grafiku
import random
from tkinter import * 
from tkinter import messagebox
import os

screen = t.getscreen()  #zobrazení turtle okna
global mistake
mistake = 0
global name
name = ""
global user
user =""
global multiply
multiply = 0

#To do:
#Malé/velké písmena - ze slova si všechny znaky přeneseme na malé, stejně tak vstup uživatele -> VYŘEŠENO
#Chyba: slovo je o jeden neznámý znak delší, než má být -> VYŘEŠENO
#Chyba: I/O operation on closed file -> VYŘEŠENO
#Udělat def na zadavani (registrace/přihlášení) uzivatele (Podle jména, ?Heslo?) -> VYŘEŠENO
#->sledování skóre uživatele
#->výpis skóre uživatelů, pokud se uživatel rohodne ukončit hru
#Obtížnost slova - podle počtu znaků, podle znaků (X...)
#->Obtížnosti - lehká, střední, těžká - lehká -> počet bodů bude stejný jako počet písmen. Střední -> počet písmen * 2. Těžká -> počet písmen * 3 -> VYŘEŠENO
#->Pokud uživatel uhodne špatně znak -1 bod... //skóre nemůže jít do mínusu -> VYŘEŠENO
#--

#https://stackoverflow.com/questions/23893978/keeping-high-scores-in-a-text-file
#přepsání souboru kvůli skóre, které se bude měnit - nový txt soubor, kde se bude ukládat jen jmeno a skóre, při ukončení programu (Uzivatele_saved.txt)
#z tohoto souboru budeme i zobrazovat žebříček hráčů...
#https://www.kite.com/python/answers/how-to-replace-a-string-within-a-file-in-python



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
    times = [x for x, appearance in enumerate(word) if appearance == character] #Creates list of when 'character' appears in 'word'
    for i in range(len(times)): #Draws character based on when it appears in 'word'
        t.penup()
        t.setpos(36 + 4*(times[i]),31)
        t.write(character, move=True, align='center', font=('Arial', 20, 'normal'))
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
    character = t.textinput('Tvůj tip','Tipni si písmeno\'') #ptáme se přes 'message box'
    character = character.lower()        #Poku uživatel zadá velké písmeno změní se na malé
    if character in word: #Pokud písmeno je ve slově, nakreslí písmeno
        drawLetter(word,character)
    else: #Pokud písmeno není ve slově, přikreslí se část oběšence
        drawBody()
        n += 1
        mistake += 1



def register():
    db = open("Uzivatele.txt", "r")
    Username = t.textinput("","Vytvoř jmeno: ")
    Password = t.textinput("","Vytvoř heslo: ")
    Password_copy = t.textinput("","Potvrď heslo: ")
    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    global name  

    if Password != Password_copy:
        messagebox.showerror("Chyba", "Hesla se neshodují")
        register()
    else:
        if len(Password)<=2:
            messagebox.showerror("Chyba", "Heslo je příliš krátké")
            register()
        elif Username in d:
            messagebox.showerror("Chyba", "Jmeno již existuje")
            register()
        else:
            db = open("Uzivatele.txt", "a")
            db.write(Username+", "+Password+"\n")
            name = Username
            messagebox.showinfo("Úspěch!", "Úspěšná registrace")

def access():
    db = open("Uzivatele.txt", "r")
    Username = t.textinput("","Zadej svoje jmeno: ")
    Password = t.textinput("","Zadej svoje heslo: ")

    global name         #potřebujeme změnit proměnnou

    if not len(Username or Password) < 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        messagebox.showinfo("Úspěch!","Úspěšné přihlášení")
                        name = Username
                    else:
                         messagebox.showerror("Chyba", "Heslo nebo jméno není správné")
                         access()
                except:
                    messagebox.showerror("Chyba","Chybné heslo jména")
                    access()
            else:
                messagebox.showerror("Chyba","Jmeno nebo helso neexistuje")
                access()
        except:
            messagebox.showerror("Chyba","Jmeno nebo helso neexistuje")
            access()
    else:
        messagebox.showerror("Chyba","Zadej hodnotu: ")
        access()

def home(option=None):      #Funkce je zavolána hned při startu programu //Assign the value None to a variable
    option = t.textinput("","Login | Signup: ")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        messagebox.showwarning("Chyba", "Zadej jednu z možností")
        home()

def difficulty(option=None):
    option = t.textinput("Obtížnost", "Lehká/Střední/Těžká (1/2/3)")
    if option == '1':
        messagebox.showinfo("", "Lehká obtížnost")
        return 1
    elif(option == '2'):
        messagebox.showinfo("", "Střední obtížnost")
        return 2
    elif(option == '3'):
        messagebox.showinfo("", "Těžká obtížnost")
        return 3
    else:
        messagebox.showwarning("Chyba", "Zadej jednu z možností")
        difficulty()
  

def score_fnce():
    global score
    score = (((len(word) - 1) + mistake) / multiply) + 0.1 #výpočet skóre / úroveň
    score = round(score)

    users = open("Uzivatele.txt", "r")
    lines = users.readlines()
    for line in lines:          #pokud je uživatel přihlášený // počítaní skóre pro dotyčného uživatele
        s = line.split(", ")    #split by coma (,) rozdělí na ["username", "password\n"]
        global user
        user = s[0] #vezmeme jen username
        print(user) #odstranit
        print(s) #odstranit
        if name == user:
            x = 1
        elif name != user:
            db = open("Uzivatele_saved.txt", "r")
            lines = db.readlines()
            b = 0
            for line in lines: #pro jeden řádek v řádcích
                if user in line: #pokud je uživatelovo jméno v řádku             
                    txt = line
                    num =[int(i) for i in txt.split() if i.isdigit()] #opravono takhle, kvůli více ciferným číslům
                    #pocet her ++
                    print(str(num))                 #odstranit
                    b += sum(num)

    if x == 1:
        db = open("Uzivatele_saved.txt", "r+")   #uložení do nového souboru
        db.write(name+", "+ str(score)+"\n")     #"jméno, skóre"
        lines = db.readlines()
        a = 0
        i = 0
        for line in lines: #pro jeden řádek v řádcích
            if name in line: #pokud je uživatelovo jméno v řádku             
                txt = line
                num =[int(i) for i in txt.split() if i.isdigit()] #opravono takhle, kvůli více ciferným číslům
                #pocet her ++
                print(str(num))                 #odstranit
                a += sum(num)
        a += score
        messagebox.showwarning("Info ", score)      #odstranit
        messagebox.showwarning("Celkem ", a)        #odstranit
        db.close()

    with open("zebricek.txt", "xt") as leaderboard: # xt pokud soubor neexistuje, vytvoří se nový, otevřeno jen pro zápis
        leaderboard.write(name + ", " + str(a) + "\n")
        leaderboard.write(user + ", " + str(b) + "\n")      #-->Vypsat všechny uživatele
        leaderboard.close()
    with open("zebricek.txt", "rt") as leaderboard: #jen pro čtení
        data = leaderboard.read()
        leaderboard.close()
        #sort
    print(data)
    #messagebox.showinfo("Celkem ", data)   
    os.remove("zebricek.txt")   #odstranění souboru


def fake_main():
    global n
    global count
    global word
    n = 0
    count = 0
    initialize()
    done = False
    while not done:
        if n > 5:
            done = True
            t.penup()
            t.setpos(50,70)
            t.write('Prohra.' + 'Slovo bylo \'' + word + '\'', move=True, align='center', font=('Arial', 10, 'normal'))
        elif count > len(word) - 2: # -> upravuje delku slova o -2
            done = True
            t.penup()
            t.setpos(50,70)
            t.write('Super! Uhodl jsi slovo \'' + word + '\'. Vyhrál jsi!', move=True, align='center', font=('Arial', 10, 'normal'))
        else:
            guess()
    return None

def main():
    konec = False
    home()
    x = difficulty()
    while not konec:
        with open("slovnik.txt", encoding="utf-8") as soubor:
            global word                         #global slouží ke zmeně proměnné, která je globální
            global multiply
            lines = soubor.readlines()
            while x == 1:
                multiply = 1
                word = random.choice(lines)
                if len(word) - 1 <= 5: #and "x" or "q" not in word: 
                    break                       # <1, 5>
                else:
                    continue
            while x == 2:
                multiply = 2
                word = random.choice(lines)
                pismena = ["q", "x", "ý", "ň", "ď", "g", "w", "ť"]          #odstanit
                if (len(word) - 1) >= 6 and (len(word) - 1) <= 8:              # <6, 8>
                    #and "x" or "q" not in word: <- když to přidám do podmínky ingnoruje mi to zadaný interval
                    #todo: podmínka aby mi to nepralo některá písmenka
                    #to slovo se bude řešit v další úrovni, tedy v další úrovni povolíme slova, kde se tyto znaky nacházejí i když jsou menší než podmínka  
                    break
                else:
                    continue
            while x == 3:
                multiply = 3
                word = random.choice(lines)
                if (len(word) - 1) > 8 or (len(word) - 1) < 8 and "x" in word:                             #<9, x>
                    break
                else:
                    continue
            word = word.lower()                         #U vybraného slova se velká písmena změní na malá
            print(word)                                 #Odstranit
            fake_main()
            repeat = t.textinput('','Chcete hrát znovu? (a/n): ')
        if repeat == 'a':
            t.reset()
            score_fnce()    
        else:              #ukončení a zavření souboru, pokud uživatel zvolí n, nebo něco jiného...
            score_fnce()   
            soubor.close()
            konec = True           
    return None



main()  #Spustí program




