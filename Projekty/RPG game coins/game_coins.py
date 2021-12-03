# Import
import sys
import os

# Classes
class Player:
    def __init__(self, name, numberOfPlayers):
        self.playername = name
        file = open("player" + (numberOfPlayers + 1) + ".txt", "w")
        file.write(f"{self.playername}\ndiary;letter\nfront poarch")
        self.inv = []
        self.map = []


# Functions
def Menu(low, high, plus):
    # Local variables
    choice = 0

    while((choice < low) or (choice > high) and (choice != plus)):
        choice = int(input("\n  I choose: "))

        # Error when choice is not defined
        if((choice < low) or (choice > high) and (choice != plus)):
            print("\n YOUR CHOICE IS NOT DEFINED\n")
            choice = 0
        # Choice is defined
        else:
            return choice

def Exit():
    # Local variable
    choice = 0

    print("\n  9 ... Back to main menu\n")

    while(choice != 9):
        choice = Menu(9, 9, 9)
        print("\n")

        if(choice != 9):
            print("\n YOUR CHOICE IS NOT DEFINED\n")
            choice = 0
    
    return 0

def Help():
    print("\n\n-----------------------------------------------------------\n HELP\n  Crucial commands:  exit, help, inventory, map\n  Moving  commands:  go + straight/back/left/right/down/up\n  Action  commands:  take/use/look/open\n")

# Global variables
GmainMenuChoice = 0

# Main
if __name__ == "__main__":
    # Local variables
    listOfPlayers = []
    numberOfPlayers = 5

    #listOfPlayers = [(line.strip()) for line in (open("list_of_players.txt", "r"))]

    while((GmainMenuChoice < 1) or (GmainMenuChoice > 3)):
        print("\n-----------------------------\n C O I N S   t h e   g a m e\n\n MAIN MENU - Choose action:\n\n  1 ... Start\n  2 ... Help\n  3 ... End game\n")
        GmainMenuChoice = Menu(1, 3, 101)

        # Start
        if(GmainMenuChoice == 1):
            choicePlayer = 0

            while((choicePlayer < 1) or (choicePlayer > 5) and (choicePlayer != 9)):
                print("\n\n-----------------------------\n START - choose a game\n")

                # Menu of players
                for i in range(1, 6):
                    filePath = ("player" + str(i) + ".txt")
                    if(os.path.exists(filePath)):
                        print(f"  {i} ... {(open(filePath).readline())}")
                    else:
                        print(f"  {i} ... Empty")
                print("\n  9 ... Back to main menu\n")
                choicePlayer = Menu(1, 5, 9)
                filePath = ("player" + choicePlayer + ".txt")
                playerName = filePath.readline()

                if((choicePlayer > 0) and (choicePlayer < 6) and (choicePlayer != 9) and os.path.exists(filePath)):
                    print(f"\n\n-----------------------------\n START - Player {playerName}\n\n  1 ... Load game\n  2 ... New game\n  3 ... Delete game\n\n  9 ... Exit\n")
                elif(choicePlayer > 0) and (choicePlayer < 6) and (choicePlayer != 9) and not os.path.exists(filePath):
                    print(f"\n\n-----------------------------\n NEW GAME - Are you sure?\n\n  1 ... Yes, start a new game\n  2 ... No, go back\n")
                    if(Menu(1, 2, 101) == 1):
                        player01 = Player(input("\n  Enter your in-game name: "), numberOfPlayers)
                    else:
                        choicePlayer = 0
                #print(player01.playername)
        # Help
        elif(GmainMenuChoice == 2):
            Help()
            GmainMenuChoice = Exit()
        # End game
        elif(GmainMenuChoice == 3):
            print("\n\n-----------------------------\n END GAME - Are you sure?\n\n  1 ... No, continue\n  2 ... Yes, exit\n")

            # Back to main menu
            if(Menu(1, 2, 101) == 1):
                print("\n")
                GmainMenuChoice = 0
            # Exit
            else:
                print("\n\n-----------------------------\n Good bye...\n\n")
                sys.exit()
        # Error
        else:
            print("\n\nERROR\n\n")
            sys.exit()