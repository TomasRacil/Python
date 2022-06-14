import pygame

from Game import *

# ----------------------------------------------------------------------------------------------------------------------
# opening a file for progress
# Start a game loop
# ----------------------------------------------------------------------------------------------------------------------
pygame.init()


def main():
    screen = pygame.display.set_mode((800, 480))
    pygame.display.set_caption('Tic-Tac-Toe')
    image = pygame.image.load('Img/icon.png')
    icon = pygame.Surface((image.get_width(), image.get_height()))
    icon.blit(image, (0, 0))
    pygame.display.set_icon(icon)

    # for reading and writing
    file = open("Progress.txt", "r+")
    play(screen, file)


if __name__ == '__main__':
    main()
