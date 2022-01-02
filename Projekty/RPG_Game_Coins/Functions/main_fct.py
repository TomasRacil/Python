# Internal import
from Classes import *
from intro import Instructions


def NewGame(choicePlayer, filePath):
    '''
    Calls functions needed while starting a new game.

    Args:
        choicePlayer(int):  Number of player that the user chose.
        filePath(str):      The path to the file that is going to store info about player and his progress.

    Returns:
        
    '''

    player = Cplayer(choicePlayer, filePath)    # creates Cplayer instance

    player.NewGame()
    Instructions(player.name, player.inv, player.map)

    room = Croom(player.name, player.inv, player.map, player.used)      # creates Croom instance 

    room.MainHallway_11()

    player.inv = room.inv
    player.map = room.map
    player.used = room.used
    player.SaveGame()

    return 0


def LoadGame(choicePlayer, filePath):
    '''
    Calls functions needed while loading a game.

    Args:
        choicePlayer(int):  Number of player that the user chose.
        filePath(str):      The path to the file that is going to store info about player and his progress.

    Returns:
        
    '''

    player = Cplayer(choicePlayer, filePath)    # creates Cplayer instance
    
    player.LoadGame()

    room = Croom(player.name, player.inv, player.map, player.used)   # creates Croom instance

    room.FrontPorch()

    player.inv = room.inv
    player.map = room.map
    player.used = room.used
    player.SaveGame()

    return 0