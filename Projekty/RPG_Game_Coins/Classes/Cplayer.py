from os import path, remove

class Player:
    def __init__(self, player):
        self.inv = []
        self.map = []
        self._filePath = path.join('Saves', ("player" + str(player) + ".txt"))

    def NewGame(self):
        self.name = input("\n  Enter your in-game name: ")

        self._file = open(self._filePath, "w")
        self._file.write(f"{self.name}\ndiary;letter\nfront poarch;main hall\n")
        
    def LoadGame(self):
        self._file = open(self._filePath, "r")

        self.name = (self._file.readline()).strip().rstrip(";")
        self.inv = ((self._file.readline()).strip().rstrip(";")).split(";")
        self.map = ((self._file.readline()).strip().rstrip(";")).split(";")
            
    def SaveGame(self):
        self._file = open(self._filePath, "w")
        
        self._invStr = "".join([self._predmet + ";" for self._predmet in self.inv])
        self._mapStr = "".join([self._misto + ";" for self._misto in self.map])

        self._file.write(f"{self.name}\n{self._invStr}\n{self._mapStr}\n")
        self._file.close()

    def DeleteGame(self):
        remove(self._filePath)