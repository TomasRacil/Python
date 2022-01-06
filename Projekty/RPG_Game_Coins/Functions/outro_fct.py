# External import
from time import sleep
from colorama import Fore, Style

# Internal import
from Functions.versatile_fct import PressEnter, ArticleCheck, CantDoThat
from Functions.outcomes_fct import *


def ActEnter(acts):
    back = False

    while(back == False):
        actPl = input(Fore.MAGENTA+"\n I choose action: ")
        print(Style.RESET_ALL)
        
        actPl = actPl.lower()
        actPl = ArticleCheck(actPl)

        for actDef in acts:
            if(actDef == actPl):
                back = True
                break
            else:
                CantDoThat()


def Outro(playerName, orderOfCoins):
    storySwitcher = {
        "fridge coin":Outcome_Fridge,
        "vase coin":Outcome_Vase,
        "medicine bottle coin":Outcome_MedicineBottle,
        "safe coin":Outcome_Safe,
        "doll coin":Outcome_Doll,
        "trophy coin":Outcome_Costume,
        "nest coin":Outcome_Nest,
        "sandbox coin":Outcome_Sandbox,
        "rag coin":Outcome_Rag,
        "book coin":Outcome_Book
    }

    print(" Zzz\n")
    sleep(3)
    print(" Zzz\n")
    sleep(3)
    print(" You slowly open your eyes and realize you are...")
    sleep(2)
    print(" At home in your bed!")

    print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n YOUR HOUSE\n")
    print(Style.RESET_ALL+ " You rapidly sit up and feel a pang in your head. You are hundred percent sure you were in the old house\n just a second ago... How is it possible?!")
    print(" Feeling you might be the house's next victim that was driven crazy and need a headshrinker's special care now,\n you look around yourself.")
    PressEnter()
    print(" For a moment you think you have hallucinations. There is a small golden book. You swiftly touch it. Feeling\n the smooth cover of the book, you are surprised it didn't vanish into the thin air, because it is\n")
    print(" the same you remeber from the library.")

    acts = ["open book", "look at book", "read book"]
    ActEnter(acts)
    acts = acts.clear()

    print(f" The book is now titled \"{playerName}\'s beginning\". You open it and start reading...")

    print(Fore.LIGHTBLUE_EX+ f"\n---------------------------------------------------------------------------------------------------------------\n {playerName.upper()}\'S BEGINNING\n")
    print(                   f" Dear {playerName}, good afternoon,\n\n While I can finally tell you something more about the villa,\n I can't tell you who I am. If not already, you will get it eventually. I have no doubt.\n\n As you might have noticed")
    print(" the villa is an old and powerful place. That is precisely why you had to solve a few riddles along the way\n of getting to its heart. If not, the villa could be misused by bad people. However, you have proven")
    print(f" yourself worthy. Since the fist three coins you have inserted into the slot machine were ", Fore.YELLOW+ f"{orderOfCoins[0]}", Fore.LIGHTBLUE_EX+ ",", Fore.YELLOW+ f"\n {orderOfCoins[1]}", Fore.LIGHTBLUE_EX+ "and ", Fore.YELLOW+ f"{orderOfCoins[2]}", Fore.LIGHTBLUE_EX+ ", your life will take quite a turn!")
    PressEnter()

    storySwitcher.get(orderOfCoins[0])()
    storySwitcher.get(orderOfCoins[1])()
    storySwitcher.get(orderOfCoins[2])()

    print(f" The strength and functionality of your new abilities will depend on the order of inserted coins,\n meaning the ", Fore.YELLOW+ f"{orderOfCoins[0]}", Fore.LIGHTBLUE_EX+ f"\'s ability will be the strongest and that\n of a ", Fore.YELLOW+ f"{orderOfCoins[2]}", Fore.LIGHTBLUE_EX+ " will be the weakest.")
    print(" Your choice is final and you can not use the slot machine ever again.")
    print(" And one last thing before I say my final goodbyes. The villa is now yours. You will find a key to it\n glued to the back of the book.\n\n Enjoy your new life and take care.\n\n It was pleasure to get to know you.", Style.RESET_ALL)
    
    print(" You flip through the empty pages to the back of the book and indeed find a key.")

    acts = ["look at key", "take key"]
    ActEnter(acts)
    acts = acts.clear()

    print(" You take the key and look at it. Its handle is pretty long and ends with a small model of the house.\n You have to go try it!\n\n Like right now!")

    acts = ["go to villa", "go to house", "go to old house"]
    ActEnter(acts)
    acts = acts.clear()

    print(" You jump out of the bed, take a jacket and in hurry put the shoes on. As you run down the street, you\n remeber your first trip to the old house and how uncertain and scared you were. Total opposite to now.")
    
    print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n VILLA\n")
    print(Style.RESET_ALL+ " When you finaly run up to the house, your jaw drops open. The villa looks like the house\n at the tapestry in the dining room. It is clean, bright and fixed. You go to the front\n porch and stop in front of the main door.")

    acts = ["use key", "open door"]
    ActEnter(acts)
    acts = acts.clear()

    print(" You put easily the key into the key hole and unlock the door. The door opens without hesistation as if it\n was awaiting your arrival. You enter the house, going swiftly form room to room,")
    print(" you look for signs of destruction. But they are just not there. Everything is neat, beautiful and\n according to your liking. Even the vase you broke is now fixed and well, nourishing its")
    print(" lively and colourful flowers. You go up to the library and notice, there is't any empty frame anymore.\n The seventh frame now bears your portrait.")
    print(" You absentmindedly walk down to the beautiful winter garden and out to the back of the house.\n As you are taking everything that's happend in, you take a deep breath in and out. You smell the grass,")
    print(" the flovers, the forest...\n\n", Fore.YELLOW+ " THIS IS YOUR NEW HOME", Style.RESET_ALL)

    print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n END CREDITS\n")
    print(Style.RESET_ALL+ " Game\t\tDaniela Zavadova\n Story\t\tDaniela Zavadova\n Visual\t\tDaniela Zavadova")