from tlacitka import *
from tdown import *
from tkinter import *

class Editor(Window, Functions):
    """
    Příprava pro hlavní loop
    """
    pass

root = Tk()
root.geometry("1250x720")
app = Editor(root)
app.mainloop()
#objekt Tk uložíme do root, nastavíme velikost okna, třídu Editor uložíme do proměnné app
#funkci zavoláme pomocí mainloop