import pygame
from Game import clickHandler, boardUpdate, getRunning

pygame.init()
pygame.display.set_caption("Hra života")
surface = pygame.display.set_mode((1200, 800))

col_background = (30, 30, 60)
col_button = (255, 255, 255)

pygame.font.init()
buttonFont = pygame.font.SysFont('Century Gothic', 35)
clearButton = buttonFont.render('Clear All', True, col_button)


def updateSurface():
    if not getRunning():
        startButton = buttonFont.render('Start', True, col_button)
    else:
        startButton = buttonFont.render('Stop', True, col_button)

    surface.fill(col_background)
    surface.blit(startButton, (400, 5))
    surface.blit(clearButton, (600, 5))
    boardUpdate(surface)
    pygame.display.update()


def eventHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                clickHandler(pygame.mouse.get_pos())
