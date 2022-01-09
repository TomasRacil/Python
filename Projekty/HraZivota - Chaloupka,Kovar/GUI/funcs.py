import pygame
from Game import clickHandler, boardUpdate, getRunning

pygame.init()
pygame.display.set_caption("Conway's Game of Life")
surface = pygame.display.set_mode((1200, 800))

col_background = (30, 30, 60)
col_button = (255, 255, 255)

pygame.font.init()
font = pygame.font.SysFont('Century Gothic', 35)


clearButton = font.render('Clear All', True, col_button)
stepButton = font.render('>>', True, col_button)
speedUpButton = font.render('+', True, col_button)
speedDownButton = font.render('-', True, col_button)

speedLbl = font.render('Speed:', True, col_button)
stepLbl = font.render('Step:', True, col_button)

def updateSurface():
    """
    This function fills surface with colors, buttons and updated game board.
	"""
    surface.fill(col_background)

    if not getRunning():
        startButton = font.render('Start', True, col_button)
    else:
        startButton = font.render('Stop', True, col_button)  

    surface.blit(speedLbl, (50, 3))
    surface.blit(speedDownButton, (190, 3))
    surface.blit(speedUpButton, (220, 5))

    surface.blit(startButton, (400, 3))
    surface.blit(clearButton, (650, 3))
    
    surface.blit(stepLbl, (1000, 3))
    surface.blit(stepButton, (1100, 5))

    boardUpdate(surface)
    pygame.display.update()


def eventHandler():
    """
    Event handler function for following events:
        Quit, 
        Mouse Button Down
	"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                clickHandler(pygame.mouse.get_pos(), surface)
