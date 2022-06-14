import pygame
import sys
from pygame.font import Font
import os

pygame.init()

# ----------------------------------------------------------------------------------------------------------------------
# class menu creates a menu witch works by taking the position of the cursor and then when clicked deciding what text is
# in the specific rectangle and taking action depending on the text
# ----------------------------------------------------------------------------------------------------------------------


class Menus:
    def __init__(self, screen=None, title='Tic-tac-toe', text=None, color=(0, 0, 0), my_font=Font('Road_Rage.otf', 34)):  #constructor
        if text is None:
            text = ['New Game  ', 'Continue ', 'Options ', 'Exit ']
        self.color = color
        self.my_font = my_font
        self.title = title
        self.text = text
        self.x = 0
        self.screen = screen

        def menu(self, file):   #method
        screen = self.screen
        width = screen.get_width()
        height = screen.get_height()

        while True:
            mouse = pygame.mouse.get_pos()
            screen.fill((99, 155, 255))
            pygame.draw.rect(screen, (255, 255, 255), [0, height / 8, width, 54])
            screen.blit(self.my_font.render(self.title, True, self.color),
                        (100, height / 8))
            for i, txt in enumerate(self.text):
                if width / 8 - 60 <= mouse[0] <= width / 8 + len(txt) * 15 and height / 2 - 27 + i * 56 <= mouse[1] <= height / 2 - 27 + i * 56 + 54:
                    self.x = i
                if self.x == i:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     [width / 8 - 60, height / 2 - 27 + i * 56, len(txt) * 21, 54], 0, 5)
                screen.blit(self.my_font.render(txt, True, self.color), (width / 8 - 50, height / 2 - 27 + i * 56))
            pygame.display.update()

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    file.close()
                    pygame.quit()
                    sys.exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        if self.title != 'Tic-tac-toe':
                            return 1
                        else:
                            file.close()
                            pygame.quit()
                            sys.exit()
                    if ev.key == pygame.K_w:
                        if self.x > 0:
                            self.x -= 1
                    if ev.key == pygame.K_s:
                        if self.x < len(self.text)-1:
                            self.x += 1
                    if ev.key == pygame.K_UP:
                        if self.x > 0:
                            self.x -= 1
                    if ev.key == pygame.K_DOWN:
                        if self.x < len(self.text)-1:
                            self.x += 1
                if (ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN) or pygame.mouse.get_pressed() == (True, False, False):
                    for i, txt in enumerate(self.text):
                        if (width / 8 - 60 <= mouse[0] <= width / 8 + len(txt) * 17 and height / 2 - 27 + i * 56 <= mouse[1] <= height / 2 - 27 + i * 56 + 54) or self.x == i:
                            if txt == 'New Game  ':
                                if os.stat("Progress.txt").st_size != 0:
                                    sure = Menus(screen, 'Do you want to start over:', ['Yes  ', 'No  '])
                                    pas = sure.menu(file)
                                    if pas != 0:
                                        return 6
                                else:
                                    new_play = Menus(screen, 'Choose difficulty:', ['Easy  ', 'Normal  ', 'Asian '])
                                    new_play.menu(file)
                                    if new_play != 0:
                                        return 6
                            if txt == 'Continue ':
                                if os.stat("Progress.txt").st_size == 0:
                                    sure = Menus(screen, 'You have to start somewhere :P', ['OK  '])
                                    sure.menu(file)
                                else:
                                    return 5
                            if txt == 'Options ':
                                options = Menus(screen, 'Options:', ['Resolution: Full Screen', 'Resolution: 1280 x 720', 'Resolution: 800 x 480', 'Back  '])
                                options.menu(file)
                            if txt == 'Exit ':
                                file.close()
                                pygame.quit()
                                sys.exit()
                            if txt == 'Yes  ':
                                file.seek(0)
                                file.truncate()
                                new_play = Menus(screen, 'Choose difficulty:', ['Easy  ', 'Normal  ', 'Asian '])
                                new_play.menu(file)
                                if new_play != 0:
                                    return 6
                            if txt == 'No  ':
                                return 0
                            if txt == 'OK  ':
                                return 6
                            if txt == 'Back  ':
                                return 6
                            if txt == 'Easy  ':
                                file.write('1')
                                return 5
                            if txt == 'Normal  ':
                                file.write('2')
                                return 5
                            if txt == 'Asian ':
                                file.write('3')
                                return 5
                            if txt == 'Resolution: Full Screen':
                                self.screen = pygame.display.set_mode((1920, 1080))
                                screen = pygame.display.set_mode((1920, 1080))
                                pygame.display.toggle_fullscreen()
                                width = screen.get_width()
                                height = screen.get_height()
                            if txt == 'Resolution: 1280 x 720':
                                self.screen = pygame.display.set_mode((1280, 720))
                                screen = pygame.display.set_mode((1280, 720))
                                width = screen.get_width()
                                height = screen.get_height()
                            if txt == 'Resolution: 800 x 480':
                                self.screen = pygame.display.set_mode((800, 480))
                                screen = pygame.display.set_mode((800, 480))
                                width = screen.get_width()
                                height = screen.get_height()
