
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
        

def dejMeme():
   
    target_subreddit = 'memes' #odkud se meme bere                 
    for submission in reddit.subreddit(target_subreddit).new(limit=100): # získání url jednoho obrázku/gifu
        url1 = submission.url
        urlList1.append(url1)
        urlKoment1.append(submission) 

def dejCute(): 
    """
    Tyto funkce stáhnou 100 url adres a vloží se do listu
    Z listu budou tlačítka brát obrázky
    
    """ 
    target_subreddit = 'aww' #odkud se meme bere                 
    for submission in reddit.subreddit(target_subreddit).new(limit=100):  # získání url jednoho obrázku/gifu
        url2 = submission.url
        urlList2.append(url2)
        urlKoment2.append(submission)
   
          

def MemeZListu():
    
    
    global CounterMeme 
    print (urlList1[CounterMeme])
    webbrowser.open_new(urlList1[CounterMeme])
    CounterMeme +=1

def MemeZListuCute(): 
    """
    Tyto funkce si berou globální proměnou a díky tomu otevřou jiný obrázek až do 100
    Po každém kliknutí zvýší o 1
    
    """
    global CounterCute
    print (urlList2[CounterCute])
    webbrowser.open_new(urlList2[CounterCute])
    CounterCute +=1


def stahniMeme():
    cestaSlozky = os.path.join(os.path.dirname(os.path.realpath(__file__)), "MemeObrazky")
    cisloObr = os.listdir(cestaSlozky)
    cisloSouboru = len(cisloObr)
    cesta = os.path.join(cestaSlozky, f"ObrazekMeme{cisloSouboru + 1}.jpg")
    urllib.request.urlretrieve(urlList1[CounterMeme -1], cesta)
    
def stahniCute():
    cestaSlozky = os.path.join(os.path.dirname(os.path.realpath(__file__)), "CuteObrazky")
    cisloObr = os.listdir(cestaSlozky)
    cisloSouboru = len(cisloObr)
    cesta = os.path.join(cestaSlozky, f"ObrazekCute{cisloSouboru + 1}.jpg")
    urllib.request.urlretrieve(urlList2[CounterCute -1], cesta)



def Napis_koment_Meme():
   urlKoment1[CounterMeme-1].reply("Nice!!")
   

def Napis_koment_Cute():
    """
    Tyto funkce napíši koment pod poslední obrázek
    """
    urlKoment2[CounterCute-1].reply("Cute!!")
    



dejMeme() #zapnutí funkcí na inicializaci/ naplnění listů
dejCute()