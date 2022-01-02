# External import
from colorama import Fore, Style

# Internal import
from Functions.versatile_fct import PressEnter


def DecoratorToColourCoins(func):
    # To colour all letters in light red colour.

    def wrapper(*args, **kwargs):
        print(Fore.LIGHTRED_EX)
        func(*args, **kwargs)
        print(Style.RESET_ALL)
        PressEnter()
    return wrapper


@DecoratorToColourCoins
def Coin_Fridge():  # love, kitchen
    print("---------------------------------------------------------------------------------------------------------------\n FRIDGE COIN\n")
    print(" The coin has a heart carved into it.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourCoins
def Coin_Vase():    # family, dining room
    print("---------------------------------------------------------------------------------------------------------------\n VASE COIN\n")
    print(" The coin depicts a branched tree with letters.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourCoins
def Coin_MedicineBottle():  # health
    print("---------------------------------------------------------------------------------------------------------------\n MEDICINE BOTTLE COIN\n")
    print(" The coin has a plus sign carved into it.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourCoins
def Coin_Safe():    # money, workroom
    print("---------------------------------------------------------------------------------------------------------------\n SAFE COIN\n")
    print(" The coin has columns of coins carved into it.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourCoins
def Coin_Doll():    # joy, childrens room
    print("---------------------------------------------------------------------------------------------------------------\n DOLL COIN\n")
    print(" The coin has a smiley face carved into it.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourCoins
def Coin_Trophy():   # success, attic
    print("---------------------------------------------------------------------------------------------------------------\n TROPHY COIN\n")
    print(" The coin depicts a trophy with number one.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourCoins
def Coin_Nest():    # nature, bedroom
    print("---------------------------------------------------------------------------------------------------------------\n NEST COIN\n")
    print(" The coin depicts a leaf and head of some animal.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourCoins
def Coin_Sandbox():    # popularity, playgroung
    print("---------------------------------------------------------------------------------------------------------------\n SANDBOX COIN\n")
    print(" The coin depicts a person wearing a crown and two people hugging him.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourCoins
def Coin_Rag():    # peace, cellar
    print("---------------------------------------------------------------------------------------------------------------\n RAG COIN\n")
    print(" The coin depicts a hand making a V sign.\n---------------------------------------------------------------------------------------------------------------")

@DecoratorToColourCoins
def Coin_Book():    # wisdom, library
    print("---------------------------------------------------------------------------------------------------------------\n BOOK COIN\n")
    print(" The coin has a brain carved into it.\n---------------------------------------------------------------------------------------------------------------")