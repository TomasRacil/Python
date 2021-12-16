import pygame

color = (30, 30, 60)

pygame.init()
pygame.display.set_caption("Hra života")
surface = pygame.display.set_mode((1200, 800))
    
def updateSurface():
    surface.fill(color)
    pygame.display.update()

def eventHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                print("Left Mouse key was clicked")
                print(pygame.mouse.get_pos())