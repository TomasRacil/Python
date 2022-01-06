# External import
from time import sleep      # to prolong an Action
from colorama import Fore, Style

# Internal import
from Functions.versatile_fct import *
from Functions.letters_fct import Letter_Invitation, Note_Mailbox


def Instructions(playerName):
    # Goes through the basic instructions and the beginning of the story.

    print(Fore.YELLOW+     "\n\n------------------------------------------------------------------------\n\n                          Welcome to game\n\n                             C O I N S")
    print(Style.RESET_ALL+ "\n\n You are going to get through the game using a few easy commands that\n can be found in Main menu after choosing an option Help or during\n the game after typing a command -help-.\n")
    print(" You can go back to Main menu after writing a command -exit- and save\n a game using -save-.\n\n Now, try to look at all of the commands.")

    # Enter command -help-
    acts = ["help"]
    ActCompare(acts)

    print((" Congratulations! You made it!\n\n Now, try to get back to the Main menu."))

    # Enter command -exit-
    acts = ["exit"]
    ActCompare(acts)

    print(" You didn't think I would let you quit so soon, did you?\n Consider next part a small film, that can not be skipped\n and where you can not use -exit- and -save-.\n\n Brace yourself, your adventure is beginning...\n")
    PressEnter()

    # Intro to the story
    print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n YOUR HOUSE\n")
    print(Style.RESET_ALL+ " Someone is constantly ringing the doorbell.\n\n DING! DONG! DING! DONG!\n\n You are standing in the main hallway of your house. The front door is just a few steps away from you.\n")
    print(" DING! DONG! DING! DONG!\n\n You were expecting no one and you didn't order anything either.")

    # Enter command -go straight-
    acts = ["go straight"]
    ActCompare(acts)
    
    print(" You walk up to the door and are now right in front of it.")

    # Enter command -open door-
    acts = ["open door"]
    ActCompare(acts)
    
    print(" You are slowly openning the door while carefully looking behind it. Suddenly you smash it open.\n\n You stumble back, your eyes wide open.\n")
    PressEnter()
    print(" There's no one, but", Fore.MAGENTA+ "an envelope.", Style.RESET_ALL+ "It lies on the ground, your name and address nicely written on the top of it.\n\n DING! DONG! DING! DONG!")

    # Enter command -take envelope-
    acts = ["take envelope"]
    ActCompare(acts)
    
    print(" You picked up the envelope and the ringing stopped. It looks rather old and the paper is smooth. You play with it\n in your hands a bit scared to look what's inside.")

	# Enter command -open envelope-
    acts = ["open envelope"]
    ActCompare(acts)
    
    print(" You open the envelope, take out the letter and start reading.\n")
    PressEnter()
    
    Letter_Invitation(playerName)
	
    # Tomorrow
    print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n TOMORROW\n")
    print(Style.RESET_ALL+ " It is ten to six and you are on your way to the old house mentioned in the letter. You stop for a while\n before a crosswalk and tell yourself: Okay, this is the last chance to turn back.")
    print(" If the next person passing is a woman, I will go. If it is a man, I won't.\n")
    PressEnter()
    print("\n So you wait.")
    sleep(2)
    print("\n\n Still waiting...")
    sleep(4)
    print("\n\n After a minute or so, there is a child on the crosswalk and it looks like it could be either.")
    print(" But you remembered your childhood and how much you loved paths of courage,\n tales about scary places and THAT got you going.\n")
    PressEnter()

    # At the house
    print(Fore.YELLOW+     "\n---------------------------------------------------------------------------------------------------------------\n FRONT PORCH\n")
    print(Style.RESET_ALL+ " It's 6 p.m. and you are standing on a front porch of the huge old house not really sure what to do.\n The creaking of planks under your feet combined with the howling of the autumn wind and a ticking")
    print(" of your watch gives you an unsettling feeling. It is gettig darker by every second passed and all you see\n is a rusty", Fore.MAGENTA+ "mailbox", Style.RESET_ALL+ "and a massive main door. However, there's nothing out of ordinary.")

    # Enter command -look at mailbox-
    acts = ["look at mailbox", "open mailbox"]
    ActCompare(acts)

    print(" You look into the mailbox just in case, already feeling stupid for letting someone prank you.\n\n And you can't believe your eyes...\n\n There is", Fore.MAGENTA+ "a note!", Style.RESET_ALL+ "Athough it is barely visible because of the deepenning darkness around you.")
    
    # Enter command -take note-
    acts = ["take note"]
    ActCompare(acts)

    print(" You fish the note out of the mailbox by your hand and start reading.")
    Note_Mailbox(playerName)

    print(" You look up to inspect the door frame and notice a tiny button way above your head behind a small piece\n of a plank that is sticking out from the frame.\n\n It must be", Fore.MAGENTA+ "the doorbell!", Style.RESET_ALL)

    # Enter command -use doorbell-
    acts = ["use doorbell"]
    ActCompare(acts)
    
    print(" You had to get on your tiptoes to reach it. The bell didn't let you wait for itself too long. It sounded\n vintage, almost ancient. After three loud DING-DONGS, the door moved a bit and created a small crack\n in otherwise impregnable wall.")

    # Enter command -open door-
    acts = ["open door"]
    ActCompare(acts)

    print(" You opened the door.")
    
    # Enter command -go straight-
    acts = ["go straight"]
    ActCompare(acts)

    print(Fore.YELLOW+ "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY\n")
    print(Style.RESET_ALL+ " You are standing in the Main hallway, but can't see anything. It's pitch dark inside. Your're not sure,\n what you have packed in your backpack, but maybe you can find there something useful.")
    
    # Enter command -inventory-
    acts = ["inventory"]
    ActCompare(acts)

    # Print inventory
    print(Fore.YELLOW+ "------------------------------------------------------------------------\n INVENTORY\n")
    print(Style.RESET_ALL+ " invitation letter, flashlight, mailbox note")
    print(Fore.YELLOW+ "------------------------------------------------------------------------")
    print(Style.RESET_ALL)

    print(             " Quick tip: You can access your inventory any time during your game\n by simply writing -inventory- and use any item if it suits\n the situation by typing -use [item]-,")
    print(             " You can read any note or letter by typing -read [item]- and look\n at any key by typing -look at [item]-.\n")
    PressEnter()

    # Enter command -use flashlight-
    acts = ["use flashlight"]
    ActCompare(acts)

    print(" Now that you can see better, you look around yourself and notice door on the left and", Fore.MAGENTA+ "fuses", Style.RESET_ALL+ "on the right.")

    # Enter command -use fuses-
    acts = ["use fuses"]
    ActCompare(acts)

    print(" Nothing is happening for a few seconds, but then you almost go blind, when a dim light lits up the house.\n You have no use for your flashlight now, so you put it back in your backpack.")
    print("\n Then you draw on a piece of paper your position in the house creating a simple map.\n\n Look at the map.")

    # Enter command -map-
    acts = ["map"]
    ActCompare(acts)
    
    # Print map
    print(Fore.YELLOW+ "------------------------------------------------------------------------\n MAP\n")
    print(Style.RESET_ALL+ " front porch, main hallway downstairs")
    print(Fore.YELLOW+ "------------------------------------------------------------------------")
    print(Style.RESET_ALL)

    print(             " Quick tip: You can access your map any time during your game by simply\n writing -map- and go back to any place you like\n by typing -go to [place]-.\n")
    PressEnter()

    print(" The introduction has ended.\n Now feel free to expore.")