from Funkce import *
from tkinter import *

def main():
    window = Tk()
    window.update()
    window.title("Password Vault")
    cursor= sqlinitialize()
    cursor.execute("SELECT * FROM masterpassword")
    if cursor.fetchall():
        loginScreen(window)
    else:
        firstTimeScreen(window)
    window.mainloop()
___main___ = main()


