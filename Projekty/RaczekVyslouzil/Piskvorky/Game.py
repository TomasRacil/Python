from Functions import *
from Results import *


def play(screen, file, save):
    my_font = Font('Road_Rage.otf', 50)
    menu = Menus(screen)
    menu.menu(file)
    domain = create_domain(screen, 3)
    pygame.mouse.set_pos(screen.get_width() / 2, 0)
    while True:
        clock = pygame.time.Clock()
        turn = 1
        level = True
        level_number = 1
        number_of_levels = 5
        while level:
            turn = update_domain(screen, domain, my_font, turn, level_number, number_of_levels)
            catch = draw(domain)
            catch = win(level_number, domain, 3, 3, catch)
            if not catch == 0:
                turn = ai_move(domain, turn, 3, 3)
            else:
                turn += 1
            if catch == 0:
                level_number += 1
            catch = win(level_number, domain, 3, 3, catch)

            level_number = result(screen, domain, my_font, turn, catch, file, 3, level_number, number_of_levels)
            game_input(file)
            print(clock.get_fps())
            pygame.display.update()
            clock.tick(60)
