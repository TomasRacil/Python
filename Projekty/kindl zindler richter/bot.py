#secret	3AAep9CO2KH7X6cRUaZH6RzUldtxQg
#web app  SQH_PT8jleVf6tjGTHLOZg
#Bot_741 /jméno
#Unob123456789 /heslo

#https://praw.readthedocs.io/en/stable/index.html Knihovna PRAW
#https://docs.python.org/3/library/tkinter.html Knihovna TKINTER

#nový kód je dole!!!!!!!!!

import praw, urllib
from tkinter import *

reddit = praw.Reddit(
    client_id="SQH_PT8jleVf6tjGTHLOZg", #The client ID is the 14-character string listed just under “personal use script” for the desired developed application
    client_secret="3AAep9CO2KH7X6cRUaZH6RzUldtxQg", #The client secret is at least a 27-character string listed adjacent to secret for the application.
    user_agent="Test_BOT",
    username="Bot_741",
    password="Unob123456789",
    
)
#print(reddit.user.me()) #To verify that you are authenticated as the correct user

print(reddit.read_only)
#funkce bota: Show_meme == stáhne jedno meme z nějakého subreditu a otevře ho jako pozadí pop-up okna potom ho zase smaže.

### GUI ###
window = Tk() #připraví okno
window.title ('MEME BOT') #název okna


window_width = 1000 # nastaví velikost okna X
window_height = 500 # nastaví velikost okna Y
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#offset okna, aby bylo ve středu obrazovky + jeho velikost(první dva řádky výška=500 šířka 1000)
#ikona okna ale to neumím přidat... obrázek tu je...
#window.iconbitmap("icon_reddit.ico") #sem musíš najít cestu


client_id = 'SQH_PT8jleVf6tjGTHLOZg'
client_secret = '3AAep9CO2KH7X6cRUaZH6RzUldtxQg'
user_agent = 'Reddit image thing'

target_subreddit = 'memes'

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret, 
                     user_agent=user_agent)
                     
for submission in reddit.subreddit(target_subreddit).new(limit=5):
    url = submission.url
    if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
        webbrowser.open_new(url)


