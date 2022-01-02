# External import
from time import sleep      # to prolong an action
from colorama import Fore, Style

# Internal import
from Functions.versatile_fct import *
from Functions.letters_fct import InvitationLetter, MailboxNote


def ActCompare(actDef):
    '''
    This function lets user enter his desired command and compares it with
    a command that he is supposed to enter according to the storymaker.
    The loop of entering repeats itself until the user enters the right command.

    Args:
        actDef(str): action defined by storymaker, to be compared with user imput

    Returns:

    '''
    
    while(True):
        actPl = input(Fore.MAGENTA+"\n I choose action: ")
        print(Style.RESET_ALL)

        if(actPl.lower().find(" the ") != (-1)):
            actPl = actPl.replace("the ", "")
        elif(actPl.lower().find(" a ") != (-1)):
            actPl = actPl.replace("a ", "")
        elif(actPl.lower().find(" an ") != (-1)):
            actPl = actPl.replace("an ", "")

        if(actPl.lower() == actDef):
            break
        else:
            print(Fore.RED+ "\n YOU CAN NOT DO THAT")
            print(Style.RESET_ALL)



def Instructions(playerName, inv, map):
    '''
    Goes through the basic instructions and the beginning of the story.

    Args:
        playerName(str): Name of the player.

    Returns:
        
    '''

    print(Fore.YELLOW+ "\n\n------------------------------------------------------------------------\n\n                          Welcome to game\n\n                             C O I N S")
    print(Style.RESET_ALL+ "\n\n You are going to get through the game using a few easy commands that\n can be found in Main menu after choosing an option Help or during\n the game after typing a command -help-.\n")
    print(" You can go back to Main menu after writing a command -exit-.\n\n Now, try to look at all of the commands.")

    # Enter command -help-
    ActCompare("help")
    PrintHelp()
    PressEnter()

    print((" Congratulations! You made it!\n\n Now, try to get back to the Main menu."))

    # Enter command -exit-
    ActCompare("exit")
    print(" You didn't think I would let you quit so soon, did you?\n Consider next part a small film, that can not be skipped.\n\n Brace yourself, your adventure is beginning...\n")
    PressEnter()

    # Intro to the story
    print(Fore.YELLOW+ "\n---------------------------------------------------------------------------------------------------------------\n YOUR HOUSE\n")
    print(Style.RESET_ALL+ " Someone is constantly ringing the doorbell.\n\n DING! DONG! DING! DONG!\n\n You are standing in the main hallway of your house. The front door is just a few steps away from you.\n")
    print(" DING! DONG! DING! DONG!\n\n You were expecting no one and you didn't order anything either.")

    # Enter command -go straight-
    ActCompare("go straight")
    print(" You walk up to the door and are now right in front of it.")

    # Enter command -open door-
    ActCompare("open door")
    print(" You are slowly openning the door while carefully looking behind it. Suddenly you smash it open.\n\n You stumble back, your eyes wide open.\n")
    PressEnter()
    print(" There's no one, but an envelope. It lies on the ground, your name and address nicely written on the top of it.\n\n DING! DONG! DING! DONG!")

    # Enter command -take envelope-
    ActCompare("take envelope")
    print(" You picked up the envelope and the ringing stopped. It looks rather old and the paper is smooth. You play with it\n in your hands a bit scared to look what's inside.")

	# Enter command -open envelope-
    ActCompare("open envelope")
    print(" You open the envelope, take out the letter and start reading.\n")
    PressEnter()
    
    InvitationLetter(playerName)
	
    # Tomorrow
    print(Fore.YELLOW+ "\n---------------------------------------------------------------------------------------------------------------\n TOMORROW\n")
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
    print(Fore.YELLOW+ "\n---------------------------------------------------------------------------------------------------------------\n FRONT PORCH\n")
    print(Style.RESET_ALL+ " It's 6 p.m. and you are standing on a front porch of the huge old house not really sure what to do.\n The creaking of planks under your feet combined with the howling of the autumn wind and a ticking")
    print(" of your watch gives you an unsettling feeling. It is gettig darker by every second passed and all you see\n is a rusty mailbox and a massive main door. However, there's nothing out of ordinary.")

    # Enter command -look at mailbox-
    ActCompare("look at mailbox")
    print(Fore.YELLOW+ "\n---------------------------------------------------------------------------------------------------------------\n MAILBOX\n")
    print(Style.RESET_ALL+ " You look into the mailbox just in case, already feeling stupid for letting someone prank you.\n\n And you can't believe your eyes...\n\n There is a note! Athough it is barely visible because of the deepenning darkness around you.")
    
    # Enter command -take note-
    ActCompare("take note")
    print(" You fish the note out of the mailbox by your hand and start reading.")
    MailboxNote(playerName)

    print(Fore.YELLOW+ "\n---------------------------------------------------------------------------------------------------------------\n FRONT PORCH\n")
    print(Style.RESET_ALL+ " You look up to inspect the door frame and notice a tiny button way above your head behind a small piece\n of a plank that is sticking out from the frame.\n\n It must be the doorbell!")

    # Enter command -use doorbell-
    ActCompare("use doorbell")
    print(" You had to get on your tiptoes to reach it. The bell didn't let you wait for itself too long. It sounded\n vintage, almost ancient. After three loud DING-DONGS, the door opend and created a small crack\n in otherwise impregnable wall.")

    # Enter command -go straight-
    ActCompare("go straight")

    print(Fore.YELLOW+ "\n---------------------------------------------------------------------------------------------------------------\n MAIN HALLWAY\n")
    print(Style.RESET_ALL+ " You are standing in the Main hallway, but can't see anything. It's pitch dark inside. Your're not sure,\n what you have packed in your backpack, but maybe you can find there something useful.")
    
    # Enter command -inventory-
    ActCompare("inventory")

    # Print inventory
    print(Fore.YELLOW+ "------------------------------------------------------------------------\n INVENTORY\n")
    print(Style.RESET_ALL+ " invitation letter, flashlight, mailbox note")
    print(Fore.YELLOW+ "------------------------------------------------------------------------")
    print(Style.RESET_ALL)

    print(" Quick tip: You can access your inventory any time during your game by simply writing -inventory-\n and use any item if it suits the situation by typing -use [item]-.\n")
    PressEnter()

    # Enter command -use flashlight-
    ActCompare("use flashlight")
    print(" Now that you can see better, you look aroud yourself and notice door on the left and fuses on the right.")

    # Enter command -use fuses-
    ActCompare("use fuses")
    print(" Nothing is happening for a few seconds, but then you almost go blind, when a dim light lits up the house.\n You have no use for your flashlight now, so you put it back in your backpack.")
    print("\n Then you draw on a piece of paper your position in the house creating a simple map.\n\n Look at the map.")

    # Enter command -map-
    ActCompare("map")
    
    # Print map
    print(Fore.YELLOW+ "------------------------------------------------------------------------\n MAP\n")
    print(Style.RESET_ALL+ " front porch, main hallway downstairs")
    print(Fore.YELLOW+ "------------------------------------------------------------------------")
    print(Style.RESET_ALL)

    print(" Quick tip: You can access your map any time during your game by simply writing -map- and go back\n to any place you like by typing -go to [place]-.\n")
    PressEnter()