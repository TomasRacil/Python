#secret	3AAep9CO2KH7X6cRUaZH6RzUldtxQg
#web app  SQH_PT8jleVf6tjGTHLOZg
#Bot_741 /jméno
#Unob123456789 /heslo

#https://praw.readthedocs.io/en/stable/index.html Knihovna PRAW
#https://docs.python.org/3/library/tkinter.html Knihovna TKINTER

#nový kód je dole!!!!!!!!!

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

def dejMeme():
    target_subreddit = 'memes' #odkud se meme bere                 
    for submission in reddit.subreddit(target_subreddit).new(limit=1): # získání url jednoho obrázku/gifu
        url = submission.url
        print(submission.id) #www.reddit.com/*id*
        if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            webbrowser.open_new(url) # otevře v nastaveném browseru

    print(reddit.read_only) #tohle ani nevím, co dělá

def koment():
    target_subreddit = 'memes' #odkud se meme bere                 
    for submission in reddit.subreddit(target_subreddit).new(limit=1):
        submission.reply("Nice") #TOHLE SE MUSÍ VYNDAT
    

def dejNazev():
    target_subreddit= 'memes'
    reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret, 
                        user_agent=user_agent)

    for submission in reddit.subreddit(target_subreddit).new(limit=2):
        print("-------")
        print("Nazev postu:", submission.title)
        # Output: the submission's title

dejMeme()
koment()
#dejNazev()
