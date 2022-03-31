from Domain import *
from Menu import *
from pygame.font import Font
import sys

pygame.init()


def result(screen, domain, my_font, turn, catch, file, array_size, level_number, number_of_levels):
    if catch is not None:
        update_domain(screen, domain, my_font, turn, level_number, number_of_levels)
        pygame.display.update()
        paused = True
        if catch == 0:
            clear_domain(domain, array_size)
            pygame.mouse.set_pos(screen.get_width() / 2, 0)
            paused = False
        elif catch == 1:
            title = 'You have won this level'
            text = ['Next level ', 'Main menu ', 'Exit ']
        elif catch == 2:
            title = 'nah a Draw'
            text = ['Continue ', 'Main menu ', 'Exit ']
        else:
            title = 'You have lost'
            text = ['Start again ', 'Main menu ', 'Exit ']

        width = screen.get_width()
        height = screen.get_height()
        my_font = Font('Road_Rage.otf', 34)
        color = (255, 255, 255)
        x = 0
        original = screen.copy()
        copy = screen.copy()
        while paused:
            mouse = pygame.mouse.get_pos()
            screen.blit(original, (0, 0))
            copy.fill((0, 0, 0))
            copy.set_alpha(210)
            screen.blit(copy, (0, 0))
            pygame.draw.rect(screen, (99, 155, 255), [0, height / 8, width, 54])
            screen.blit(my_font.render(title, True, color), (width / 2 - len(title) * 23, height / 8))
            for i, txt in enumerate(text):
                if width / 8 - 60 <= mouse[0] <= width / 8 + len(txt) * 17 and height / 2 - 27 + i * 56 <= \
                        mouse[1] <= height / 2 - 27 + i * 56 + 54:
                    x = i
                if x == i:
                    pygame.draw.rect(screen, (99, 155, 255),
                                     [width / 8 - 60, height / 2 - 27 + i * 56, len(txt) * 21, 54], 0, 5)
                screen.blit(my_font.render(txt, True, color), (width / 8 - 50, height / 2 - 27 + i * 56))
            pygame.display.update()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    file.close()
                    pygame.quit()
                    sys.exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        screen.blit(original, (0, 0))
                        paused = False
                    if ev.key == pygame.K_w:
                        if x > 0:
                            x -= 1
                    if ev.key == pygame.K_s:
                        if x < len(text) - 1:
                            x += 1
                    if ev.key == pygame.K_UP:
                        if x > 0:
                            x -= 1
                    if ev.key == pygame.K_DOWN:
                        if x < len(text) - 1:
                            x += 1
                if (ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN) or pygame.mouse.get_pressed() == (
                        True, False, False):
                    for i, txt in enumerate(text):
                        if (width / 8 - 60 <= mouse[0] <= width / 8 + len(txt) * 15 and height / 2 - 27 + i * 56 <=
                                mouse[1] <= height / 2 - 27 + i * 56 + 54) or x == i:
                            if txt == 'Next level ':
                                clear_domain(domain, array_size)
                                pygame.mouse.set_pos(screen.get_width() / 2, 0)
                                paused = False
                                return level_number
                            if txt == 'Continue ':
                                clear_domain(domain, array_size)
                                pygame.mouse.set_pos(screen.get_width() / 2, 0)
                                paused = False
                                return level_number
                            if txt == 'Start again ':
                                clear_domain(domain, array_size)
                                pygame.mouse.set_pos(screen.get_width() / 2, 0)
                                paused = False
                                return 1
                            if txt == 'Exit ':
                                file.close()
                                pygame.quit()
                                sys.exit()
    return level_number