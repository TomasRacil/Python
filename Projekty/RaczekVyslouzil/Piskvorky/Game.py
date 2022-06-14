from Functions import *
from Results import *


def play(screen, file):
    my_font = Font('Road_Rage.otf', 50)
    menu = Menus(screen)
    menu.menu(file)
    file.seek(0)
    diff = int(file.read())
    array_size = 3
    win_condition = 3
    domain = create_domain(screen, array_size)
    pygame.mouse.set_pos(screen.get_width() / 2, 0)
    while True:
        clock = pygame.time.Clock()
        turn = 1
        level = True
        level_number = 1
        number_of_levels = 5
        while level:
            turn = update_domain(screen, domain, my_font, turn, level_number, number_of_levels, diff)
            catch = draw(domain)
            catch = win(level_number, domain, array_size, win_condition, catch)
            if not catch == 0:
                turn = ai_move(domain, turn, array_size, win_condition, diff)
            else:
                turn += 1
            if catch == 0:
                level_number += 1
            catch = win(level_number, domain, array_size, win_condition, catch)
            level_number, turn, diff = result(screen, domain, my_font, turn, catch, file, 3, level_number, number_of_levels, diff)
            game_input(file)
            pygame.display.update()
            clock.tick(60)
