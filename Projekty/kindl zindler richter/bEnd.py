
#secret	3AAep9CO2KH7X6cRUaZH6RzUldtxQg
#web app  SQH_PT8jleVf6tjGTHLOZg
#Bot_741 /jméno
#Unob123456789 /heslo

#https://praw.readthedocs.io/en/stable/index.html Knihovna PRAW
#https://docs.python.org/3/library/tkinter.html Knihovna TKINTER


from inspect import Parameter
from tracemalloc import stop
import praw, urllib
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
        

"""
    dejMeme a dejCute
    -funkce stáhnou 100 url adres a vloží se do listu
    -z toho listu budou tlačítka brát obrázky
"""
def dejMeme(): 
    target_subreddit = 'memes' #odkud se meme bere                 
    for submission in reddit.subreddit(target_subreddit).new(limit=100): # získání url jednoho obrázku/gifu
        url1 = submission.url
        urlList1.append(url1)
        urlKoment1.append(submission) 

def dejCute(): 
    target_subreddit = 'aww' #odkud se meme bere                 
    for submission in reddit.subreddit(target_subreddit).new(limit=100):  # získání url jednoho obrázku/gifu
        url2 = submission.url
        urlList2.append(url2)
        urlKoment2.append(submission)

          
"""
    MemeZListu a MemeZListuCute

    -bere si číslo podle globální proměnné, díky tomu se pokaždé otevře jiný obrázek až do 100
    -po každém kliknutí zvýší globální proměnnou o +1
""" 
def MemeZListu():
    
    global CounterMeme 
    print (urlList1[CounterMeme])
    webbrowser.open_new(urlList1[CounterMeme])
    CounterMeme +=1

def MemeZListuCute(): # tlačítko 2!
    global CounterCute
    print (urlList2[CounterCute])
    webbrowser.open_new(urlList2[CounterCute])
    CounterCute +=1

"""
    stahniMeme a stahniCute
    - stáhnou otevřené obrázky
"""
def stahniMeme():
    
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

"""
    Napis_koment_Meme a Napis_koment_Cute
    - hodí koment pod obrázek
"""

def Napis_koment_Meme():
   urlKoment1[CounterMeme-1].reply("Nice!!")
   

def Napis_koment_Cute():
    urlKoment2[CounterCute-1].reply("Cute!!")
    


#zapnutí funkcí na inicializaci/ naplnění listů
dejMeme()
dejCute()