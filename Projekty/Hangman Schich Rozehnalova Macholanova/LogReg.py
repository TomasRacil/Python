from tkinter import * 
from tkinter import messagebox
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

def register():
    db = open("Uzivatele.txt", "r")
    Username = t.textinput("","Vytvoř jmeno: ")
    Password = t.textinput("","Vytvoř heslo: ")
    Password_copy = t.textinput("","Potvrď heslo: ")
    d = []
    f = []
    for i in db:
        a, b = i.split(", ") #rozdělíme i podle čárky Username, Password
        b = b.strip()
        d.append(a)     #do d přidám a (username)
        f.append(b)     #do f přirám b (password)
    data = dict(zip(d, f))  #dict == dictionary (key, value)

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
            S.getName(name)
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
        data = dict(zip(d, f))      #konvertuji dva listy do jednoho

        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        messagebox.showinfo("Úspěch!","Úspěšné přihlášení")
                        name = Username
                        S.getName(name)
                    else:
                         messagebox.showerror("Chyba", "Heslo nebo jméno není správné")
                         access()
                except:
                    messagebox.showerror("Chyba","Chybné heslo jména")
                    access()
            else:
                messagebox.showerror("Chyba","Jmeno nebo heslo neexistuje")
                access()
        except:
            messagebox.showerror("Chyba","Jmeno nebo heslo neexistuje")
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