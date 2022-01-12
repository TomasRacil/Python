import turtle as t  #Knihovna na grafiku
import random
from tkinter import * 
from tkinter import messagebox
import os
from time import sleep
import re #regulární výrazy
import Draw as D
import LogReg as L
import Score as S

screen = t.getscreen()  #zobrazení turtle okna

global multiply
multiply = 0
global lead
lead = ""

def main():
    global CharList
    konec = False
    L.home()
    x = 0
    while True:
        x = S.difficulty()            #pokud uživatel zadá špatnou možnost, znovu volí obtížnost
        if x == 1 or x == 2 or x == 3:
            break
    while not konec:
        with open("slovnik.txt", encoding="utf-8") as soubor:
            global word                         #global slouží ke zmeně proměnné, která je globální
            global multiply
            lines = soubor.readlines()
            while x == 1:
                multiply = 1
                word = random.choice(lines)
                if len(word) - 1 <= 5  and not re.search(r"[qxýňďgwť]", word): #and "x" or "q" not in word: 
                    break                       # <1, 5>
            while x == 2:
                multiply = 2
                word = random.choice(lines)
                if (len(word) - 1) >= 6 and (len(word) - 1) <= 8 and not re.search(r"[qxýňďgwť]", word):    # <6, 8>
                    break
            while x == 3:
                multiply = 3
                word = random.choice(lines)
                if re.search(r"[qxýňďgwť]", word) and (len(word) - 1) < 10:
                    break
                elif (len(word) - 1) > 8 and (len(word) -1) < 10:           #<9, x>
                    break
            word = word.lower()  #U vybraného slova se velká písmena změní na malá
            S.GetMultiply(multiply)
            D.getWord(word)
            S.getWord(word)
            print(word)                                                             #Odstranit (Výpis slova do konzole)
            D.fake_main()
            repeat = t.textinput('','Chcete hrát znovu? (a/n): ')
        if repeat == 'a':
            t.reset()
            S.score_fnce()   
        else:              #ukončení a zavření souboru, pokud uživatel zvolí něco jiného než a...
            S.score_fnce()   
            soubor.close()
            t.clear()
            t.setpos(50,60)
            lead = S.RetLead()
            t.write('Žebříček: \n' + str(lead), move=False, align='center', font=('Arial', 18, 'normal'))
            sleep(5)
            konec = True       
    return None


if main() == "main()": 
    main()  #Spustí program

