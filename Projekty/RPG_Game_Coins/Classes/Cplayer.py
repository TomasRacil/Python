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

        self.inv = ["invitation letter", "flashlight","mailbox note"]
        self.map = ["front porch","main hallway downstairs"]
        
    def LoadGame(self):
        # Loads the in-game name and the stored inventory and map into corresponding lists.

        self.__file = open(self.__filePath, "r")

        self.name = (self.__file.readline()).strip().rstrip(";")
        self.position = (self.__file.readline()).strip().rstrip(";")
        self.inv = ((self.__file.readline()).strip().rstrip(";")).split(";")
        self.map = ((self.__file.readline()).strip().rstrip(";")).split(";")
        self.used = ((self.__file.readline()).strip().rstrip(";")).split(";")
        self.orderOfCoins = ((self.__file.readline()).strip().rstrip(";")).split(";")