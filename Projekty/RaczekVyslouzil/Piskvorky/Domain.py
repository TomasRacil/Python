import pygame

pygame.init()


class DomainCell:
    def __init__(self, screen, array_size, x, y):
        self.text = ''
        self.pressed = False
        self.c_width = (((screen.get_width() * 0.8) - 100) / array_size)
        self.c_height = (((screen.get_height() * 0.8) - 100) / array_size)
        self.x = x
        self.y = y
        self.margin = 100
        self.cell_margin = 5
        self.body = pygame.Rect(self.x, self.y, self.c_width, self.c_height)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_margin(self):
        return self.margin

    def get_width(self):
        return self.c_width

    def get_cell_margin(self):
        return self.cell_margin

    def get_body(self):
        return self.body

    def get_text(self):
        return self.text

    def get_pressed(self):
        return self.pressed

    def set_text(self, text):
        self.text = text

    def set_pressed(self, pressed):
        self.pressed = pressed


def create_domain(screen, array_size):
    s_width = (((screen.get_width() * 0.8) - 100) / array_size)
    s_height = (((screen.get_height() * 0.8) - 100) / array_size)
    x = (screen.get_width() - ((screen.get_width() * 0.8) - 100)) / 2
    y = (screen.get_height() - ((screen.get_height() * 0.8) - 100)) / 2
    domain = [[[] for n in range(array_size)] for j in range(array_size)]
    for j in range(array_size):
        for i in range(array_size):
            domain[j][i] = DomainCell(screen, array_size, x, y)
            x += s_width + 5
        x = (screen.get_width() - ((screen.get_width() * 0.8) - 100)) / 2
        y += s_height + 5
    return domain


def clear_domain(domain, array_size):
    for j in range(array_size):
        for i in range(array_size):
            domain[j][i].set_text('')
            domain[j][i].set_pressed(False)


def update_domain(screen, game_domain, my_font, turn, level_number, number_of_levels):
    mouse = pygame.mouse.get_pos()
    screen.fill((99, 155, 255))
    screen.blit(my_font.render(f'{level_number} / {number_of_levels}', True, (255, 255, 255)), (screen.get_width()/2 - 50, 20))
    for j in range(len(game_domain)):
        for i in range(len(game_domain[0])):
            if game_domain[j][i].get_body().collidepoint(mouse) or game_domain[j][i].get_pressed():
                pygame.draw.rect(screen, (255, 255, 255), game_domain[j][i].get_body())
                screen.blit(my_font.render(game_domain[j][i].get_text(), True, (0, 0, 0)),
                            (game_domain[j][i].get_x() + game_domain[j][i].get_width()/3, game_domain[j][i].get_y() + 2))
            else:
                pygame.draw.rect(screen, (255, 255, 255), game_domain[j][i].get_body(), 7)
                screen.blit(my_font.render(game_domain[j][i].get_text(), True, (0, 0, 0)),
                            (game_domain[j][i].get_x() + game_domain[j][i].get_width()/3, game_domain[j][i].get_y() + 2))
            if game_domain[j][i].get_body().collidepoint(mouse) and pygame.mouse.get_pressed() == \
                    (True, False, False) and not game_domain[j][i].get_pressed():
                game_domain[j][i].set_text('X')
                game_domain[j][i].set_pressed(True)
                turn += 1
    return turn
