import urllib.request
import praw
import webbrowser
import os

reddit = praw.Reddit(
    client_id="SQH_PT8jleVf6tjGTHLOZg", #The client ID is the 14-character string listed just under “personal use script” for the desired developed application
    client_secret="3AAep9CO2KH7X6cRUaZH6RzUldtxQg", #The client secret is at least a 27-character string listed adjacent to secret for the application.
    user_agent="Test_BOT",
    username="Bot_741",
    password="Unob123456789",
)

cislo = 1

def dejMeme():
    target_subreddit = 'memes' #odkud se meme bere                 
    for submission in reddit.subreddit(target_subreddit).new(limit=1):
        global url1
        url1 = submission.url
        print(submission.id) #www.reddit.com/*id*
        if url1.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            webbrowser.open_new(url1) # otevře v nastaveném browseru
            #submission.reply("Nice") #TOHLE SE MUSÍ VYNDAT
            return url1

def dejNSFW():
    target_subreddit = 'nsfw' #odkud se meme bere                 
    for submission in reddit.subreddit(target_subreddit).new(limit=1):
        global url2
        url2 = submission.url
        print(submission.id) #www.reddit.com/*id*
        if url2.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            webbrowser.open_new(url2) # otevře v nastaveném browseru
            #submission.reply("Nice") #TOHLE SE MUSÍ VYNDAT
            return url2

def stahniMeme():
    cestaSlozky = os.path.abspath('Projekty/kindl zindler richter/MemeObrazky')
    cislo = os.listdir(cestaSlozky)
    cisloSouboru = len(cislo) 
    cesta = os.path.join(cestaSlozky, f"ObrazekMeme{cisloSouboru + 1}.jpg")
    urllib.request.urlretrieve(url1, cesta)
    

def stahniNSFW():
    cestaSlozky = os.path.abspath('Projekty/kindl zindler richter/NSFWObrazky')
    cislo = os.listdir(cestaSlozky)
    cisloSouboru = len(cislo)
    cesta = os.path.join(cestaSlozky, f"ObrazekNSFW{cisloSouboru + 1}.jpg")
    urllib.request.urlretrieve(url2, cesta)
    

dejMeme()
dejNSFW()
stahniMeme()
stahniNSFW()