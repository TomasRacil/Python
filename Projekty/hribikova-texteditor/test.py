from tkinter import *
from json.tool import main
from tlacitka import *
from tdown import *


class Editor(Window, Functions):
    """
    Příprava pro mainloop.
    """

    pass


if __name__ == "_main_":
    main()

root = Tk()
root.geometry("1250x720")
app = Editor(root)
app.mainloop()
# objekt Tk uložíme do root, nastavíme velikost okna, třídu Editor uložíme do proměnné app
# pomocí mainloop řekneme app aby se spustila
