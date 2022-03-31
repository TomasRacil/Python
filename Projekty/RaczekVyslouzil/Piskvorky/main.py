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
    save = []
    # if the file is not empty then put it into an array
    if os.stat("Progress.txt").st_size != 0:
        save = file.read()
        save = [int(n) for n in save.split(" ")]
    play(screen, file, save)


if __name__ == '__main__':
    main()
