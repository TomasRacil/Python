# External import
from colorama import Fore, Style

# Internal import
from Functions.versatile_fct import PressEnter


def DecoratorToColourOutcomes(func):
    # Colours outcomes in blue colour

    def wrapper(*args, **kwargs):
        print(Fore.BLUE)
        func(*args, **kwargs)
        print(Style.RESET_ALL)
        PressEnter()
    return wrapper


# Functions printing outcomes
@DecoratorToColourOutcomes
def Outcome_Fridge():
    print(" LOVE\n")
    print(" Fridge coin with its heart symbolizes love. You will know, what dish people love the most and you will be\n able to cook it just right for them. This food will spread love and surpress people's hatred.")

@DecoratorToColourOutcomes
def Outcome_Vase():
    print(" FAMILY\n")
    print(" Vase coin with its family tree symbolizes family. From now on, you will be able to see and talk to your\n deceased family members. You can find them at places they liked the most.")

@DecoratorToColourOutcomes
def Outcome_MedicineBottle():
    print(" HEALTH\n")
    print(" Health coin with its golden red cross symbolizes health. You won't be affected by any illness or disease.\n In addition to that, people spending time at your presence will be cured of their illness or at least,\n their symptoms will be eased.")

@DecoratorToColourOutcomes
def Outcome_Safe():
    print(" WEALTH\n")
    print(" Safe coin with its piles of coins symbolizes wealth. You will have one wish for something tangible per day.\n The safe in the villa's workroom will provide you that. The code stays the same.")

@DecoratorToColourOutcomes
def Outcome_Doll():
    print(" JOY\n")
    print(" Doll coin with its smiley face symbolizes joy. You will be able to feel, what makes people happy and give\n them exactly that through a balloon art. You will be great at cheering people up.")

@DecoratorToColourOutcomes
def Outcome_Costume():
    print(" FREEDOM\n")
    print(" Costume coin with its dove symbolizes freedom. There will be no place, that you won't be able to visit.\n All you have to do is to think about that place and go through the terrace door. You have to\n go through the same door that you have come out of while returning.")

@DecoratorToColourOutcomes
def Outcome_Nest():
    print(" NATURE\n")
    print(" Nest coin with its fauna and flora symbolizes nature. You will become an animal and a plant whisperer. You\n will understand nature better than anyone and it will understand you. It will thrive under\n your care.")

@DecoratorToColourOutcomes
def Outcome_Sandbox():
    print(" POWER\n")
    print(" Sandbox coin with its silhouettes symbolizes power. You will be very popular wherever you go. You will have\n a gift of great social and persuasive skills that can help you build a better future.")

@DecoratorToColourOutcomes
def Outcome_Rag():
    print(" PEACE\n")
    print(" Rag coin with its V-sign symbolizes peace. You will be great at soothing fear and calming people down,\n because of your perfect empathy. Your life will be very peaceful and undisrupted.")

@DecoratorToColourOutcomes
def Outcome_Book():
    print(" WISDOM\n")
    print(" Book coin with its brain symbolizes wisdom. You won't have suddenly all the knolegde of the world, but it\n will be fairly easy for you to obtain it. All you have to do is to read a book about any topic,\n you'd like to learn.")