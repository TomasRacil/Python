import numpy as np
import pygame

board = np.zeros((80,120))
running = False

col_dead = (10, 10, 40)
col_aboutToDie = (200, 200, 225)
col_alive = (255, 255, 215)

def clickHandler(coords):
    global running
    global board
    #GAME BOARD
    if coords[0] >= 0 and coords[0] <= 1200 and coords[1] >= 50 and coords [1] <= 800:
        if not running: 
            x = int((coords[1] - 50) / 10)
            y = int(coords[0] / 10)

            if board[x, y] == 0:
                board[x, y] = 1
            else:
                board[x, y] = 0

    #START / STOP
    elif coords[0] >= 400 and coords[0] <= 480 and coords[1] >= 0 and coords [1] < 50:
        if running == True:
             running = False
        else:
             running = True

    #CLEAR ALL
    elif coords[0] >= 600 and coords[0] <= 745 and coords[1] >= 0 and coords [1] < 50:
        if not running:
            board = np.zeros((80,120))

def boardUpdate(surface):
    global board
    newBoard = np.zeros((board.shape[0], board.shape[1]))

    for row, column in np.ndindex(board.shape):
        num_alive = np.sum(board[row-1:row+2, column-1:column+2]) - board[row, column]

        if board[row, column] == 1 and num_alive < 2 or num_alive > 3:
            col = col_aboutToDie
        elif (board[row, column] == 1 and 2 <= num_alive <= 3) or (board[row,column] == 0 and num_alive == 3):
            newBoard[row, column] = 1
            col = col_alive

        col = col if board[row, column] == 1 else col_dead

        pygame.draw.rect(surface, col, (column*10, (row*10) + 50, 9, 9))
    
    if running == True: #Hra neběží, nový board se neukládá
        board = newBoard

def getRunning():
    return running