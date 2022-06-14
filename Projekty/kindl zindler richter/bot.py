
from tkinter import *
import bEnd as bot

 
"""
root vytváří okna
titulek vytvoří titulek okba
button jsou tlačítka na úvodním okně
"""

root = Tk()
root.title("Reddit Bot")
root.geometry("500x500")
root.configure(background='#FF7518')       
""" Slouží k vytvoření okna """

titulek = Label(root,text="Reddit bot",font=("Arial",25))
titulek.configure(background='#FF7518')
titulek.place(x = 165, y = 50)
""" Slouží k vytvoření titulku okna """


def cute_okno():

    
    """
    Tato funkce vytvoří vyskakovací okno ve kterém budou tři tlačítka : stáhnout, koment a close
    
    """

    global nove_okno
        

    nove_okno = Toplevel(root)  # Vytvoření vyskakovacího okna
    nove_okno.geometry("250x250")
    nove_okno.title("Show Cute meme")
   

    titulek2 = Label(nove_okno,text="Show Cute meme",font=("Arial",16)) # Vytvoření titulku okna
    titulek2.place(x = 35, y = 30)

    

    button_koment = Button(nove_okno,text="Comment",width=15,height=2,command=lambda:bot.Napis_koment_Cute()) # Vytvoření tlačítka s funkcí ze soubory bEnd.py
    button_koment.place(x=70,y=100)

    button_stahni = Button(nove_okno,text="Stahnout",width=15,height=2,command=lambda:bot.stahniCute())
    button_stahni.place(x=70,y=150)

    button_destroy = Button(nove_okno, text="Close window",command=nove_okno.destroy,width=15,height=2)
    button_destroy.place(x=70,y=200)  


def meme_okno():

    """
    Funkce je identická funkci cute_okno
    """
    
    nove_okno2 = Toplevel(root)
    nove_okno2.geometry("250x250")
    nove_okno2.title("Meme")
    

    titulek3 = Label(nove_okno2,text="Show Meme",font=("Arial",16))
    titulek3.place(x = 35, y = 30)


    button_koment2 = Button(nove_okno2,text="Comment",width=15,height=2,command=lambda:bot.Napis_koment_Meme())
    button_koment2.place(x=70,y=100)

    button_stahni2 = Button(nove_okno2,text="Stahnout",width=15,height=2,command=lambda:bot.stahniMeme())
    button_stahni2.place(x=70,y=150)

    button_destroy2 = Button(nove_okno2, text="Close window",command=nove_okno2.destroy,width=15,height=2)
    button_destroy2.place(x=70,y=200)  



button_cute = Button(root, text="Cute meme", width=20,height=5, command= lambda:[bot.MemeZListuCute(), cute_okno()] ) #tlačítko spouští funkci z bEnd.py a zároveň otevára nové okno
button_meme = Button(root, text="Meme",width=20,height=5,command = lambda:[bot.MemeZListu(), meme_okno()])
button_exit = Button(root, text = "Exit", width=20,height=5,command=root.quit)

button_cute.place(x = 170, y = 150)
button_meme.place(x = 170, y = 250)
button_exit.place(x = 170,y = 350)



                     
root.mainloop()
