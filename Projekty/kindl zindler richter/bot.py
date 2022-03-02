
from tkinter import *
#secret	3AAep9CO2KH7X6cRUaZH6RzUldtxQg
#web app  SQH_PT8jleVf6tjGTHLOZg
#Bot_741 /jméno
#Unob123456789 /heslo

#https://praw.readthedocs.io/en/stable/index.html Knihovna PRAW
#https://docs.python.org/3/library/tkinter.html Knihovna TKINTER

#nový kód je dole!!!!!!!!!

from inspect import Parameter
import praw, urllib
from tkinter import *
import webbrowser

### GUI ###


###logika bota###
client_id = 'SQH_PT8jleVf6tjGTHLOZg'
client_secret = '3AAep9CO2KH7X6cRUaZH6RzUldtxQg'
user_agent = 'Reddit image thing'
username = 'Bot_741',
password = 'Unob123456789',

reddit = praw.Reddit(client_id=client_id, # inicializace klienta pro všechny funkce
            client_secret=client_secret, 
            user_agent=user_agent,
            username=username,
            password=password)
urlList = [] #inicializuje list na ukládání url adres
urlKoment = []

def dejMeme(): #stáhne 100 url adres a vloží je do listu
    target_subreddit = 'memes' #odkud se meme bere                 
    for submission in reddit.subreddit(target_subreddit).new(limit=5): # získání url jednoho obrázku/gifu
        url = submission.url
        urlKoment.append(submission) 
        urlList.append(url) 

    #print(reddit.read_only) #tohle ani nevím, co dělá, ale bylo to tam, tak to mazat raději nebudu       

def MemeZListu(): #funguje!!
    for x in urlList:
        print (x)
    webbrowser.open_new(urlList[2])

dejMeme()
MemeZListu()


def Napis_koment():
    #dejMeme()
    print(urlKoment[2])
    #parametr.reply("Nice")

Napis_koment()
 
    




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

def nsfw():

    global nove_okno
        
    # VYTVOŘENÍ VYSKAKOVACÍHO OKNA
    nove_okno = Toplevel(root)
    nove_okno.geometry("250x250")
    nove_okno.title("NSFW Meme")
    #nove_okno.iconbitmap(r"C:\Users\jacke\py\images\icon2.ico")

    titulek2 = Label(nove_okno,text="Show NSFW Meme",font=("Arial",16))
    titulek2.place(x = 35, y = 30)

    # VYTVOEŘNÍ TLAČÍTKA
    button_koment = Button(nove_okno,text="Comment",width=15,height=2)
    button_koment.place(x=70,y=100)
    button_destroy = Button(nove_okno, text="Close window",command=nove_okno.destroy,width=15,height=2)
    button_destroy.place(x=70,y=150)  
   
# SFW
# PO KLIKNUTI SE OTEVŘE - URL ADRESA
#                       - NOVÉ OKNO
# NOVÉ OKNO - TLAČÍTKA KOMENT A CLOSE
# TLAČÍTKO KOMENT - OKOMTUJE A ZAVŘE OKNO
# TLAČÍTKO CLOSE - ZAVŘE OKNO 


def sfw():

    
    #VYTVOŘENÍ VYSKAKOVACÍHO OKNA
    
    nove_okno2 = Toplevel(root)
    nove_okno2.geometry("250x250")
    nove_okno2.title("SFW Meme")
    #nove_okno2.iconbitmap(r"C:\Users\jacke\py\images\icon3.ico")

    titulek3 = Label(nove_okno2,text="Show SFW Meme",font=("Arial",16))
    titulek3.place(x = 35, y = 30)

    # VYTVOEŘNÍ TLAČÍTKA

    button_koment2 = Button(nove_okno2,text="Comment",width=15,height=2)
    button_koment2.place(x=70,y=100)
    button_destroy2 = Button(nove_okno2, text="Close window",command=nove_okno2.destroy,width=15,height=2)
    button_destroy2.place(x=70,y=150)  


button_sfw = Button(root, text="Image SFW", width=20,height=5, command= sfw )
button_nsfw = Button(root, text="Image NSFW",width=20,height=5,command = nsfw)
button_exit = Button(root, text = "Exit", width=20,height=5,command=root.quit)


button_sfw.place(x = 170, y = 150)
button_nsfw.place(x = 170, y = 250)
button_exit.place(x = 170,y = 350)



                     
root.mainloop()