# External import
from colorama import Fore, Style


class Cplayer:
    def __init__(self, choicePlayer, filePath):
        # Public
        self.inv = []       # list of items in inventory
        self.map = []       # list of places in map
        self.used = []      # used items from inventory
        self.orderOfCoins = []      # list of the coins in order that they were used
        
        # Private
        self.__player = choicePlayer     # number of player that user chose
        self.__filePath = filePath       # path to the player file

    def NewGame(self):
        # Lets player choose his in-game name and creates lists containing basic
        # items in inventory and places that he has already been to.
        
        print(Fore.YELLOW+ f"\n\n------------------------------------------------------------------------\n NEW GAME - Game {self.__player}\n")
        self.name = input(Fore.MAGENTA+ "  Enter your in-game name: ")
        print(Style.RESET_ALL)

        self.position = "intro"
        self.inv = ["invitation letter", "flashlight","mailbox note"]
        self.map = ["front porch","main hallway downstairs"]

        self.__file = open(self.__filePath, "w")
        
        self.__invStr = "".join([self.__thing + ";" for self.__thing in self.inv])
        self.__mapStr = "".join([self.__place + ";" for self.__place in self.map])
        self.__usedStr = "".join([self.__thing + ";" for self.__thing in self.used])
        self.__orderOfCoinsStr = "".join([self.__coin + ";" for self.__coin in self.orderOfCoins])

        self.__file.write(f"{self.name}\n{self.position}\n{self.__invStr}\n{self.__mapStr}\n{self.__usedStr}\n{self.__orderOfCoinsStr}\n")
        self.__file.close()
        
    def LoadGame(self):
        # Loads the in-game name and the stored inventory and map into corresponding lists.

        self.__file = open(self.__filePath, "r")

        self.name = (self.__file.readline()).strip().rstrip(";")
        self.position = (self.__file.readline()).strip().rstrip(";")
        self.inv = ((self.__file.readline()).strip().rstrip(";")).split(";")
        self.map = ((self.__file.readline()).strip().rstrip(";")).split(";")
        self.used = ((self.__file.readline()).strip().rstrip(";")).split(";")
        self.orderOfCoins = ((self.__file.readline()).strip().rstrip(";")).split(";")