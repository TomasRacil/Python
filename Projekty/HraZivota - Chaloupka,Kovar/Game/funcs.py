import numpy as np
import pygame

board = np.zeros((80,120))

col_dead = (10, 10, 40)
col_aboutToDie = (200, 200, 225)
col_alive = (255, 255, 215)

def addPoint(coords):
    board[int((coords[1] - 50)/ 10), int(coords[0] / 10)] = 1

def boardUpdate(surface):
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
    
    #zde bude board = newBoard pro aktualizaci, je možné udělat až po implementaci tlačítek
    
