# Internal import
from Classes import *
from Functions.intro_fct import Instructions
from Functions.outro_fct import Outro


def NewGame(choicePlayer, filePath):
    '''
    Calls functions needed while starting a new game.

    Args:
        choicePlayer(int):  Number of player that the user chose.
        filePath(str):      The path to the file that is going to store info about player and his progress.

    Returns:
        0
        
    '''

    player = Cplayer(choicePlayer, filePath)    # creates Cplayer instance

    player.NewGame()
    Instructions(player.name)

    room = Croom(player.name, player.inv, player.map, player.used, filePath)      # creates Croom instance
    room.SaveFct()
    room.MainHallway_11()

    return 0


def LoadGame(choicePlayer, filePath):
    '''
    Calls functions needed while loading a game.

    Args:
        choicePlayer(int):  Number of player that the user chose.
        filePath(str):      The path to the file that is going to store info about player and his progress.

    Returns:
        0
        
    '''

    player = Cplayer(choicePlayer, filePath)    # creates Cplayer instance
    
    player.LoadGame()

    if(player.position == "intro"):       # game was started, but intro was not played till the end
        Instructions(player.name)

        room = Croom(player.name, player.inv, player.map, player.used, filePath)      # creates Croom instance
        room.SaveFct()
        room.MainHallway_11()

    elif(player.position == "outro"):     # game has been played to the end, only the ending story will be replayed
        Outro(player.name, player.orderOfCoins)
    else:
        room = Croom(player.name, player.inv, player.map, player.used, filePath)   # creates Croom instance
        room.FrontPorch()

    return 0