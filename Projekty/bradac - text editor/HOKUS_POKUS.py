from funkce_pro_praci_s_textem import *
from funkcni_casti import *
"""
des. BRADÁČ Tomáš   22-5KB  16.1.2021

Primitivní MarkDown editor
Celé okono pracuje s "Framy", které se rozmisťují pomocí gridového systému (řádek, sloupec)
    V aplikaci mámé okno, ve kterém jsou rozmístěny další rámce
        rámce pro tlačítka, texty
    V levém rámci zpracováváme text zadný uživatelem a převádíme ho do html do pravého rámce 
"""
class Window(Body, Functions):
    """
    Příprava classy pro hlavní loop
    """
    pass


# mainloop
root = Tk()
root.geometry("1280x720")    # WxH
app = Window(root)
app.mainloop()