from tkinter import Tk
from tlacitka import Functions
from tdown import Window


class Editor(Window, Functions):
    """
    Příprava pro mainloop.
    """


if __name__ == "__main__":
    root = Tk()
    root.geometry("1250x720")
    app = Editor(root)
    app.mainloop()
    # objekt Tk uložíme do root, nastavíme velikost okna, třídu Editor uložíme do proměnné app
    # pomocí mainloop řekneme app aby se spustila
