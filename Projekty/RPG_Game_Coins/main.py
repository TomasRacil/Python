# External import
from os import path, remove         # to create a path to a file, to delete a file
from colorama import Fore, Style

# Internal import
from Functions.main_fct import *
from Functions.versatile_fct import Menu, PrintHelp


# Main
if __name__ == "__main__":

    # Local variable
    MainMenuChoice = 0         # variable of the main menu; makes sure the game is in a loop, until it is ended manually

    while((MainMenuChoice < 1) or (MainMenuChoice > 3)):      # loop of the main menu
        print(Fore.YELLOW+ "\n------------------------------------------------------------------------\n C O I N S   t h e   g a m e\n\n MAIN MENU")
        print(Style.RESET_ALL+ "\n  1 ... Start\n  2 ... Help\n  3 ... End game\n")
        MainMenuChoice = Menu(1, 3, 101)       # user chooses his next move in main menu (start, help, end)

        # Start
        match MainMenuChoice:
            case 1:
                choicePlayer = 0        # variable of the players menu; holds the number of player slot that was choosen throughout the game

                while((choicePlayer < 1) or (choicePlayer > 5) and (choicePlayer != 9)):        # loop of the player menu
                    
                    print(Fore.YELLOW+ "\n------------------------------------------------------------------------\n START - Choose a game")
                    print(Style.RESET_ALL)

                    # Menu of players
                    for i in range(1, 6):       # prints out menu of free or occupied spots (1 - 5)
                        filePath = path.join('Saves', ("player" + str(i) + ".txt"))         # creates a path to the supposed files

                        if(path.exists(filePath)):      # prints either "empty" or "player name" depending on the state (exist/does not exist) of the corresponding file
                            print(f"  {i} ... {(open(filePath).readline().strip())}")
                        else:
                            print(f"  {i} ... Empty")
                    print("\n  9 ... Go back\n")
                    choicePlayer = Menu(1, 5, 9)        # user chooses his game spot (1 - 5)

                    filePath = path.join(path.dirname(path.realpath(__file__)),'Saves', ("player" + str(choicePlayer) + ".txt"))      # creates a path to file of the choosen player

                    # Menu of next steps
                    # For empty slots
                    if((choicePlayer > 0) and (choicePlayer < 6) and (choicePlayer != 9) and not (path.exists(filePath))):
                        print(Fore.YELLOW+ f"\n------------------------------------------------------------------------\n START - Game {choicePlayer}")
                        print(Style.RESET_ALL+ "\n  1 ... New game\n\n  9 ... Go back\n")
                        
                        # Start new game
                        if(Menu(1, 1, 9) == 1):       # user chooses to start a new game or go back to player menu
                            MainMenuChoice = NewGame(choicePlayer, filePath)
                        # Go back to player menu
                        else:
                            choicePlayer = 0

                    # Menu of next steps
                    # For already started games
                    elif((choicePlayer > 0) and (choicePlayer < 6) and (choicePlayer != 9) and path.exists(filePath)):
                        choice = 0

                        print(Fore.YELLOW+ f"\n------------------------------------------------------------------------\n START - Game {choicePlayer}")
                        print(Style.RESET_ALL+ "\n  1 ... Load game\n  2 ... New game\n  3 ... Delete game\n\n  9 ... Go back\n")
                        choice = Menu(1, 3, 9)      # user chooses his next step (load, new, delete, exit)

                        match choice:
                        # Load game
                            case 1:
                                MainMenuChoice = LoadGame(choicePlayer, filePath)
                            
                            # Start new game
                            case 2:
                                print(Fore.YELLOW+ f"\n------------------------------------------------------------------------\n  NEW GAME - Game {choicePlayer}")
                                print(Style.RESET_ALL+ "\n  All the progress will be lost.\n  Are you sure you want to proceed?\n\n  1 ... No\n  2 ... Yes\n")

                                # Go back to player menu
                                if(Menu(1, 2, 101) == 1):
                                    choicePlayer = 0
                                
                                # Start new game
                                # Overwrites the old one
                                else:
                                    MainMenuChoice = NewGame(choicePlayer, filePath)

                            # Delete game
                            case 3:
                                print(Fore.YELLOW+ f"\n------------------------------------------------------------------------\n  DELETE GAME - Game {choicePlayer}")
                                print(Style.RESET_ALL+ "\n  All the progress will be lost.\n  Are you sure you want to proceed?\n\n  1 ... No\n  2 ... Yes\n")
                                
                                # Go back to player menu
                                if(Menu(1, 2, 101) == 1):
                                    choicePlayer = 0
                                
                                # Delete game
                                else:
                                    remove(filePath)
                                    choicePlayer = 0
                        
                            # Back to player menu
                            case 9:
                                choicePlayer = 0

                    # Back to main menu
                    else:
                        MainMenuChoice = 0
        
            # Help
            case 2:     # prints function Help()
                PrintHelp()
                print("\n  9 ... Go back\n")
                Menu(9, 9, 9)
                MainMenuChoice = 0         # lets user choose to go back to main menu
        
            # End game
            case 3:         # asks to confirm the choice to end game
                print(Fore.YELLOW+ "\n------------------------------------------------------------------------\n END GAME - Are you sure?")
                print(Style.RESET_ALL+ "\n  1 ... No, continue\n  2 ... Yes, exit\n")

                # Back to main menu
                if(Menu(1, 2, 101) == 1):
                    print("\n")
                    MainMenuChoice = 0
                # Exit
                else:
                    print(Fore.YELLOW+ "\n------------------------------------------------------------------------\n Good bye...\n")
                    print(Style.RESET_ALL)
                    exit()