# External import
from colorama import Fore, Style


def Menu(low, high, plus):
    '''
    Lets user enter his choice of movement in main menu. Controls that
    it is a number and that it is a defined option.

    Args:
        low(int):   The lowest number that the user can choose.
        high(int):  The highest number that the user can choose.
        plus(int):  Additional number the user can choose.

    Returns:
        choice(int): Number that the player chose.
    '''

    # Local variable
    choice = 0      # variable storing the users choice

    while((choice < low) or (choice > high) and (choice != plus)):      # to enter choice again in case of a not valid previous choice
        
        try:
            choice = int(input(Fore.MAGENTA+"  I choose: "))
            print(Style.RESET_ALL)

            # Error when choice is not defined
            if((choice < low) or (choice > high) and (choice != plus)):     # not valid choice
                print(Fore.RED+"\n YOUR CHOICE IS NOT DEFINED")
                print(Style.RESET_ALL)
                choice = 0
            # Choice is defined
            else:       # valid choice
             return choice

        except:     # number is not entered
            print(Fore.RED+"\n USE ONLY NUMBERS")
            print(Style.RESET_ALL)


def PressEnter():   # Lets user press enter to continue. Exists to stop loading loads of text all at once
    input(Fore.MAGENTA+ " Press enter to continue")
    print(Style.RESET_ALL)


def PrintHelp():  # Prints all possible commands or parts of them
    print(Fore.YELLOW+ "------------------------------------------------------------------------\n HELP\n")
    print(Style.RESET_ALL+ "  Crucial commands:  exit, help, inventory, map\n  Moving  commands:  go + /straight/back/left/right/down/up\n  Action  commands:  take/use/look at/open")
    print(Fore.YELLOW+ "------------------------------------------------------------------------")
    print(Style.RESET_ALL)