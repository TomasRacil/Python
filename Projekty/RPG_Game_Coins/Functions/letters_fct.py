# External import
from colorama import Fore, Style

# Internal import
from Functions.versatile_fct import PressEnter


def DecoratorToColourLetters(func):
    # To colour all letters in light blue colour.

    def wrapper(*args, **kwargs):
        print(Fore.LIGHTBLUE_EX)
        func(*args, **kwargs)
        print(Style.RESET_ALL)
        PressEnter()
    return wrapper


@DecoratorToColourLetters
def Letter_Invitation(playerName):
    print("---------------------------------------------------------------------------------------------------------------\n INVITATION LETTER\n")
    print(f" Greetings, {playerName},\n\n I'm glad this letter found you. Go to the huge old deserted house at the suburbs of our town tomorrow.\n The one next to the Grey forest. You might find me crazy right now and you're telling yourself, there is no")
    print(" way you will go there. Especially not after reading about it in a very shady letter and knowing that it has\n a long history of people going crazy. But here's what I have to say. You are a very curious person and you")
    print(" have only one chance to go and find out what this is all about. It will eat you alive, if you don't. Believe\n me, I used to be just like that.\n")
    print(" The door will open for you at 6 p.m. If you get inside once, you can always come back and continue your\n adventure some other time. If you don't, you won't get a chance to enter the house ever again.\n")
    print(" Think about it carefully.\n\n Good luck.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourLetters
def Note_Mailbox(playerName):
    print("---------------------------------------------------------------------------------------------------------------\n MAILBOX NOTE\n")
    print(f" Dear {playerName},\n\n guess you have a problem getting inside.\n\n I'll give you a hint.\n\n Try ringing the bell.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourLetters
def Letter_Fridge(playerName):
    print("---------------------------------------------------------------------------------------------------------------\n FRIDGE LETTER\n")
    print(f" Dear {playerName},\n\n Welcome to my humble abode.\n\n Now, that you are here, I can finally reveal the purpose of your visit. Or, at least part of it.")
    print(" Strange, as it may sound, I need you to find this house's treasure. You will be looking for ten rare golden\n coins, that are hidden somewhere in the house. Every coin has a different meaning, so remember")
    print(" to be carefull how you deal with them. If you get any ill intentions, I advise you to leave the coins behind,\n forget all of this and never come back. The aftermath of your actions won't keep you")
    print(f" waiting long. But do not worry too much about it, {playerName}, I feel you have a kind heart.\n\n I'm sure there are now even more questions popping out in your head than there were before this letter.")
    print(" I have no doubt you will find answers to all of them, eventually.\n\n Good luck.\n\n PS: Don't forget to prioritize.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourLetters
def Note_Pigeon():   # 659 - 2 - 8 (6 pigeons + 1 mouse + 1 squirrel) - 6
    print("---------------------------------------------------------------------------------------------------------------\n PIGEON NOTE\n")
    print(" House number\n Number of people who lost their head\n Number of animals inhabiting the house\n Number of previous residents")
    print("---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourLetters
def Letter_Book():
    print("---------------------------------------------------------------------------------------------------------------\n BOOK LETTER\n")
    print(" ")
    print("---------------------------------------------------------------------------------------------------------------")