# Import
from os import path
from Classes import *
from Functions import *

# Functions
def Help():
    print("\n\n-----------------------------------------------------------\n HELP\n  Crucial commands:  exit, help, inventory, map\n  Moving  commands:  go + straight/back/left/right/down/up\n  Action  commands:  take/use/look/open\n")

# Global variable
GmainMenuChoice = 0         # variable of the main menu; makes sure the game is in a loop, until it is ended manually

# Main
if __name__ == "__main__":
    # Local variables
    choice = 0

    while((GmainMenuChoice < 1) or (GmainMenuChoice > 3)):      # loop of the main menu
        print("\n-----------------------------\n C O I N S   t h e   g a m e\n\n MAIN MENU - Choose action:\n\n  1 ... Start\n  2 ... Help\n  3 ... End game\n")
        GmainMenuChoice = Menu(1, 3, 101)       # user chooses his next move in main menu (start, help, end)

        # Start
        if(GmainMenuChoice == 1):
            choicePlayer = 0        # variable of the players menu; holds the number of player slot that was choosen throughout the game

            while((choicePlayer < 1) or (choicePlayer > 5) and (choicePlayer != 9)):        # loop of the player menu
                
                print("\n\n-----------------------------\n START - Choose a game\n")

                # Menu of players
                for i in range(1, 6):       # prints out menu of free or occupied spots (1 - 5)
                    filePath = path.join('Saves', ("player" + str(i) + ".txt"))         # creates a path to the supposed files

                    if(path.exists(filePath)):      # prints either "empty" or "player name" depending on the state (exist/does not exist) of the corresponding file
                        print(f"  {i} ... {(open(filePath).readline().strip())}")
                    else:
                        print(f"  {i} ... Empty")
                print("\n  9 ... Back to main menu\n")
                choicePlayer = Menu(1, 5, 9)        # user chooses his game spot (1 - 5)

                filePath = path.join('Saves', ("player" + str(choicePlayer) + ".txt"))      # creates a path to file of the choosen player

                # Menu of next steps
                # For empty slots
                if((choicePlayer > 0) and (choicePlayer < 6) and (choicePlayer != 9) and not (path.exists(filePath))):
                    print(f"\n\n-----------------------------\n START - Game {choicePlayer}?\n\n  1 ... New game\n\n  9 ... Exit\n")
                    
                    # Start new game
                    if(Menu(1, 1, 9) == 1):       # user chooses to start a new game or go back to player menu
                        player = Player(choicePlayer)
                        player.NewGame()
                    # Go back to player menu
                    else:
                        choicePlayer = 0

                # Menu of next steps
                # For already started games
                elif((choicePlayer > 0) and (choicePlayer < 6) and (choicePlayer != 9) and path.exists(filePath)):
                    print(f"\n\n-----------------------------\n START - Game {choicePlayer}\n\n  1 ... Load game\n  2 ... New game\n  3 ... Delete game\n\n  9 ... Exit\n")
                    choice = Menu(1, 3, 9)      # user chooses his next step (load, new, delete, exit)

                    # Load game
                    if(choice == 1):
                        player = Player(choicePlayer)
                        player.LoadGame()
                    
                    # Start new game
                    elif(choice == 2):
                        print(f"\n\n-----------------------------\n  NEW GAME - Game {choicePlayer}\n\n  All the progress will be lost.\n  Are you sure you want to proceed?\n\n  1 ... No\n  2 ... Yes\n")

                        # Go back to player menu
                        if(Menu(1, 2, 101) == 1):
                            choicePlayer = 0
                        
                        # Start new game
                        # Overwrites the old one
                        else:
                            player = Player(choicePlayer)
                            player.NewGame()

                    # Delete game
                    elif(choice == 3):
                        print(f"\n\n-----------------------------\n  DELETE GAME - Game {choicePlayer}\n\n  All the progress will be lost.\n  Are you sure you want to proceed?\n\n  1 ... No\n  2 ... Yes\n")
                        
                        # Go back to player menu
                        if(Menu(1, 2, 101) == 1):
                            choicePlayer = 0
                        
                        # Delete game
                        else:
                            player = Player(choicePlayer)
                            player.DeleteGame()
                    
                    # Back to player menu
                    else:
                        choicePlayer = 0

                # Back to main menu
                else:
                    GmainMenuChoice = 0
       
        # Help
        elif(GmainMenuChoice == 2):     # prints function Help()
            Help()
            print("\n  9 ... Back to main menu\n")
            Menu(9, 9, 9)
            GmainMenuChoice = 0         # lets user choose to go back to main menu
       
        # End game
        elif(GmainMenuChoice == 3):         # asks to confirm the choice to end game
            print("\n\n-----------------------------\n END GAME - Are you sure?\n\n  1 ... No, continue\n  2 ... Yes, exit\n")

            # Back to main menu
            if(Menu(1, 2, 101) == 1):
                print("\n")
                GmainMenuChoice = 0
            # Exit
            else:
                print("\n\n-----------------------------\n Good bye...\n\n")
                exit()