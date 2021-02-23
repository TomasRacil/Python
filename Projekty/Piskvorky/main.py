import tkinter as tk
from Module import *
root = tk.Tk()


"""
Main:
- Vytvoreni pole pro tlacitka
- Nastaveni herniho pole - promenna x promenna (v tomto pripade 5x5), lze libovolne nastavit 
- Nastaveni poctu stejnych - udava kolik O nebo X musi byt za sebou, aby byla uznana vyhra (v tomto pripade 3), lze libovolne nastavit
- Spusteni hlavniho tkinter loopu 
"""
def main():
    Buttons2D=[[],[]]

    velikostPole=6 			
    pocetStejnych=3
    VytvorHerniPole(velikostPole,pocetStejnych)

    root.mainloop()

if __name__ == '__main__':
    main()




