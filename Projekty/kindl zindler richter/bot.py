
   

#secret	3AAep9CO2KH7X6cRUaZH6RzUldtxQg
#web app  SQH_PT8jleVf6tjGTHLOZg
#Bot_741 /jméno
#Unob123456789 /heslo

#https://praw.readthedocs.io/en/stable/index.html Knihovna PRAW
#https://docs.python.org/3/library/tkinter.html Knihovna TKINTER

#prohrabat ty importy, něco už tam nepoužíváme!!

from inspect import Parameter
from tracemalloc import stop
import praw, urllib
from tkinter import *
import webbrowser, random
import os

###logika bota###
client_id = 'SQH_PT8jleVf6tjGTHLOZg'
client_secret = '3AAep9CO2KH7X6cRUaZH6RzUldtxQg'
user_agent = 'Reddit image thing'
username = 'Bot_741',
password = 'Unob123456789',

cisloObr = 0 #hej raději ani mazat nebudu... 
CounterMeme = 0 #počítačka na MEME
CounterCute = 0 #počítačka na CUTE

reddit = praw.Reddit(client_id=client_id, # inicializace klienta pro všechny funkce
            client_secret=client_secret, 
            user_agent=user_agent,
            username=username,
            password=password)

urlList1 = [] #inicializuje list na ukládání url adres
urlList2 = []
urlKoment1 = [] #list na komentáře
urlKoment2 = []
cisla = [] #list čísel


Cislo = random.randint(0,99)
        

def dejMeme(): #stáhne 100 url adres a vloží je do listu inicializace pro první tlačítko, zavolá se po spuštění
    target_subreddit = 'memes' #odkud se meme bere                 
    for submission in reddit.subreddit(target_subreddit).new(limit=100): # získání url jednoho obrázku/gifu
        url1 = submission.url
        urlList1.append(url1)
        urlKoment1.append(submission) 

def dejCute(): #inicializace pro druhé tlačítko.
    target_subreddit = 'aww' #odkud se meme bere                 
    for submission in reddit.subreddit(target_subreddit).new(limit=100):
        url2 = submission.url
        urlList2.append(url2)
        urlKoment2.append(submission)

    #print(reddit.read_only) #tohle ani nevím, co dělá, ale bylo to tam, tak to mazat raději nebudu       

def MemeZListu():
    """""
    hlavní funkce která se otevře po stisku tlačítka 2.
    bere si číslo podle globální proměnné, díky tomu se pokaždé otevře jiný obrázek až do 100
    po každém kliknutí zvýší globální proměnnou o +1
    """ 
    global CounterMeme 
    print (urlList1[CounterMeme])
    webbrowser.open_new(urlList1[CounterMeme])
    CounterMeme +=1

def MemeZListuCute(): # tlačítko 2!
    global CounterCute
    print (urlList2[CounterCute])
    webbrowser.open_new(urlList2[CounterCute])
    CounterCute +=1


def stahniMeme():
    """
    To stahování si musí vyřešit sám Zindler já kur*a ani nevím jak to funguje!!!
    a btw musíš to nějak sladit, aby to fungovalo s těmi Countery.
    """
    cestaSlozky = os.path.abspath('Projekty/kindl zindler richter/MemeObrazky')
    cisloObr = os.listdir(cestaSlozky)
    cisloSouboru = len(cisloObr) 
    cesta = os.path.join(cestaSlozky, f"ObrazekMeme{cisloSouboru + 1}.jpg")
    urllib.request.urlretrieve(urlList1[CounterMeme -1], cesta)
    
def stahniCute():
    cestaSlozky = os.path.abspath('Projekty/kindl zindler richter/CuteObrazky')
    cisloObr = os.listdir(cestaSlozky)
    cisloSouboru = len(cisloObr)
    cesta = os.path.join(cestaSlozky, f"ObrazekCute{cisloSouboru + 1}.jpg")
    urllib.request.urlretrieve(urlList2[CounterCute -1], cesta)

def Napis_koment_Meme():
   urlKoment1[CounterMeme-1].reply("Nice!!")
   

def Napis_koment_Cute():
    urlKoment2[CounterCute-1].reply("Cute!!")
    


#zapnutí funkcí na inicializaci/ naplnění listů
dejMeme()
dejCute()


 
    




#VYTVOŘENÍ OKNA

root = Tk()
root.title("Reddit Bot")
root.geometry("500x500")
#root.iconbitmap(r"C:\Users\jacke\py\images\icon1.ico")
root.configure(background='#FF7518')       


titulek = Label(root,text="Reddit bot",font=("Arial",25))
titulek.configure(background='#FF7518')
titulek.place(x = 165, y = 50)



# NSFW
# PO KLIKNUTI SE OTEVŘE - URL ADRESA
#                       - NOVÉ OKNO
# NOVÉ OKNO - TLAČÍTKA KOMENT A CLOSE
# TLAČÍTKO KOMENT - OKOMTUJE A ZAVŘE OKNO
# TLAČÍTKO CLOSE - ZAVŘE OKNO

def cute_okno():

    global nove_okno
        
    # VYTVOŘENÍ VYSKAKOVACÍHO OKNA
    nove_okno = Toplevel(root)
    nove_okno.geometry("250x250")
    nove_okno.title("Show Cute meme")
    #nove_okno.iconbitmap(r"C:\Users\jacke\py\images\icon2.ico")

    titulek2 = Label(nove_okno,text="Show Cute meme",font=("Arial",16))
    titulek2.place(x = 35, y = 30)

    # VYTVOEŘNÍ TLAČÍTKA
    button_koment = Button(nove_okno,text="Comment",width=15,height=2,command=lambda:Napis_koment_Cute())
    button_koment.place(x=70,y=100)

    button_stahni = Button(nove_okno,text="Stahnout",width=15,height=2,command=lambda:[stahniCute(),nove_okno.destroy()])
    button_stahni.place(x=70,y=150)

    button_destroy = Button(nove_okno, text="Close window",command=nove_okno.destroy,width=15,height=2)
    button_destroy.place(x=70,y=200)  
   
# SFW
# PO KLIKNUTI SE OTEVŘE - URL ADRESA
#                       - NOVÉ OKNO
# NOVÉ OKNO - TLAČÍTKA KOMENT A CLOSE
# TLAČÍTKO KOMENT - OKOMTUJE A ZAVŘE OKNO
# TLAČÍTKO CLOSE - ZAVŘE OKNO 


def meme_okno():

    
    #VYTVOŘENÍ VYSKAKOVACÍHO OKNA
    
    nove_okno2 = Toplevel(root)
    nove_okno2.geometry("250x250")
    nove_okno2.title("Meme")
    #nove_okno2.iconbitmap(r"C:\Users\jacke\py\images\icon3.ico")

    titulek3 = Label(nove_okno2,text="Show Meme",font=("Arial",16))
    titulek3.place(x = 35, y = 30)

    # VYTVOEŘNÍ TLAČÍTKA

    button_koment2 = Button(nove_okno2,text="Comment",width=15,height=2,command=lambda:Napis_koment_Meme())
    button_koment2.place(x=70,y=100)
    button_stahni2 = Button(nove_okno2,text="Stahnout",width=15,height=2,command=lambda:[stahniMeme(),nove_okno2.destroy()])
    button_stahni2.place(x=70,y=150)
    button_destroy2 = Button(nove_okno2, text="Close window",command=nove_okno2.destroy,width=15,height=2)
    button_destroy2.place(x=70,y=200)  


button_cute = Button(root, text="Cute meme", width=20,height=5, command= lambda:[MemeZListuCute(), cute_okno()] )
button_meme = Button(root, text="Meme",width=20,height=5,command = lambda:[MemeZListu(), meme_okno()])
button_exit = Button(root, text = "Exit", width=20,height=5,command=root.quit)


button_cute.place(x = 170, y = 150)
button_meme.place(x = 170, y = 250)
button_exit.place(x = 170,y = 350)



                     
root.mainloop()
