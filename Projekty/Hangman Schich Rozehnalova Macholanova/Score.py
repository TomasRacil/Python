from tkinter import * 
from tkinter import messagebox
import turtle as t  #Knihovna na grafiku
import os

screen = t.getscreen()  #zobrazení turtle okna
global mistake
mistake = 0
global name
name = ""
global user
user =""

def getWord(wrd = ""):
    global word                 #předání slova, které jsme si vygenerovali
    word = wrd

def GetMultiply(mlp):
    global multiply             #potřebujeme dostat úroveň, kterou si uživatel zvolil
    multiply = mlp

def getMistake(mst):
    global mistake              #kolik uživatel udělá chyb na jedno slovo
    mistake = mst

def getName(nm):
    global name                 #aktuálně přihlášený uživatel
    name = nm

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
  

def score_fnce():
    global score
    score = (((len(word) - 1) + mistake) / multiply) + 0.1 #výpočet skóre / úroveň
    score = round(score)
    UserList = []
    ScoreList = []
    pocet = 0
    GamesCount = 0
    GamesCount2 = 1
    GCount = []
    global lead
    x = 0
    aS = 0


    users = open("Uzivatele.txt", "r")
    lines = users.readlines()
    for line in lines:          #pokud je uživatel přihlášený // počítaní skóre pro dotyčného uživatele
        s = line.split(", ")    #split by coma (,) rozdělí na ["username", "password\n"]
        global user
        user = s[0] #vezmeme jen username
        if name == user:
            x = 1
        elif name != user:
            db = open("Uzivatele_saved.txt", "r")
            lines = db.readlines()
            b = 0
            GamesCount = 0
            for line in lines: #pro jeden řádek v řádcích
                if user in line: #pokud je uživatelovo jméno v řádku          
                    txt = line
                    num =[int(i) for i in txt.split() if i.isdigit()] #opravono takhle, kvůli více ciferným číslům       
                    GamesCount += 1 #pocet her ++
                    b += sum(num)
            pocet += 1
            GCount.append(GamesCount)
            UserList.append(user)
            ScoreList.append(b)
    if x == 1:
        db = open("Uzivatele_saved.txt", "r+")   #uložení do nového souboru
        db.write(name+", "+ str(score)+"\n")     #"jméno, skóre"
        lines = db.readlines()
        #aS = 0
        i = 0
        for line in lines: #pro jeden řádek v řádcích
            if name in line: #pokud je uživatelovo jméno v řádku             
                txt = line
                num =[int(i) for i in txt.split() if i.isdigit()] #opravono takhle, kvůli více ciferným číslům
                aS += sum(num)
                GamesCount2 += 1
        aS += score
        db.close()

    #Průměr na 1 hru
    a = 0
    while a < pocet:
        ScoreList[a] = ScoreList[a] / GCount[a]
        a += 1
    UserList.append(name)
    ScoreList.append(aS / GamesCount2)
    #Dva listy sloučíme a srovnáme podle čísel, následně je znovu rozdělíme                             SORT
    zipped_list = zip(UserList, ScoreList)
    sorted_list = sorted(zipped_list, key = lambda t: t[1])                                         #sort podle čísel
    UserList,  ScoreList = zip(*sorted_list)
    with open("zebricek.txt", "xt") as leaderboard: # xt pokud soubor neexistuje, vytvoří se nový, otevřeno jen pro zápis
        a = 0
        while a < (pocet + 1):
            if a <= 4:         #vypíšeme jen prvních 5 uživatelů
                leaderboard.write(str(a+1) + ". " + UserList[a] + ", " + str(ScoreList[a]) + "\n")
            a += 1
        leaderboard.close()
    with open("zebricek.txt", "rt") as leaderboard: #jen pro čtení
        data = leaderboard.read()
        lead = data
        leaderboard.close()
    os.remove("zebricek.txt")   #odstranění souboru

def RetLead():
    return lead