# External import
from colorama import Fore, Style

# Internal import
from Functions.versatile_fct import PressEnter


def DecoratorToColourKeys(func):
    # To colour all letters in cyan colour.

    def wrapper(*args, **kwargs):
        print(Fore.CYAN)
        func(*args, **kwargs)
        print(Style.RESET_ALL)
        PressEnter()
    return wrapper


@DecoratorToColourKeys
def Key_Table():    # to workroom, dining room
    print("---------------------------------------------------------------------------------------------------------------\n TABLE KEY\n")
    print(" The key's handle looks like an old school writing pen that often needed a refill of ink.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourKeys
def Key_Chest():    # to cellar, attic
    print("---------------------------------------------------------------------------------------------------------------\n CHEST KEY\n")
    print(" The key's handle is completely black and at the end is a sign that looks like zero.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourKeys
def Key_Soap():     # to winter garden, bathroom_2
    print("---------------------------------------------------------------------------------------------------------------\n SOAP KEY\n")
    print(" The key's handle ended with a snowflake.\n\n Or is it a flower?\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourKeys
def Key_Safe():     # to gazebo, workroom
    print("---------------------------------------------------------------------------------------------------------------\n SAFE KEY\n")
    print(" The key's handle looks like a bird cage with a roof.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourKeys
def Key_Swing():    # to childrens room, playground
    print("---------------------------------------------------------------------------------------------------------------\n SWING KEY\n")
    print(" The key's handle is shaped like a teddy bear.\n---------------------------------------------------------------------------------------------------------------")