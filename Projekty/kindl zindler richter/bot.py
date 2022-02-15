#secret	3AAep9CO2KH7X6cRUaZH6RzUldtxQg
#web app  SQH_PT8jleVf6tjGTHLOZg
#Bot_741 /jméno
#Unob123456789 /heslo

#https://praw.readthedocs.io/en/stable/index.html Knihovna PRAW
#https://docs.python.org/3/library/tkinter.html Knihovna TKINTER

import praw
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

### GUI ###
window = Tk() #připraví okno
window.geometry("1000x500") # nastaví velikost okna X*Y
window.mainloop() #display window


