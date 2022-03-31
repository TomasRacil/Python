import pygame
import random
import sys

pygame.init()


def game_input(file):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            file.close()
            pygame.quit()
            sys.exit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                file.close()
                pygame.quit()
                sys.exit()


def ai_move(game_array, turn, array_size, win_condition):
    if turn % 2 == 0:
        x1 = -1
        y1 = -1
        num = 0
        position = -1
        win_condition = win_condition - 1
        # bot play 1
        if turn == 2:
            if game_array[1][1].get_text() == 'X':
                x1 = random.randint(0, 1) * 2
                y1 = random.randint(0, 1) * 2
            else:
                x1 = 1
                y1 = 1
        else:
            for y in range(array_size):
                for x in range(array_size):
                    if game_array[y][x].get_text() == 'X':
                        num += 1
                    if game_array[y][x].get_text() == '':
                        position = x
                    if num == win_condition and not position == -1:
                        x1 = position
                        y1 = y
                num = 0
                position = -1
            for x in range(array_size):
                for y in range(array_size):
                    if game_array[y][x].get_text() == 'X':
                        num += 1
                    if game_array[y][x].get_text() == '':
                        position = y
                    if num == win_condition and not position == -1:
                        x1 = x
                        y1 = position
                num = 0
                position = -1
            for p in range(array_size):
                if game_array[p][p].get_text() == 'X':
                    num += 1
                if game_array[p][p].get_text() == '':
                    position = p
                if num == win_condition and not position == -1:
                    x1 = position
                    y1 = position
            num = 0
            position = -1
            for p in range(array_size):
                if game_array[p][2 - p].get_text() == 'X':
                    num += 1
                if game_array[p][2 - p].get_text() == '':
                    position = p
                if num == win_condition and not position == -1:
                    x1 = 2 - position
                    y1 = position
            num = 0
            position = -1
            for y in range(array_size):
                for x in range(array_size):
                    if game_array[y][x].get_text() == 'O':
                        num += 1
                    if game_array[y][x].get_text() == '':
                        position = x
                    if num == win_condition and not position == -1:
                        x1 = position
                        y1 = y
                num = 0
                position = -1
            for x in range(array_size):
                for y in range(array_size):
                    if game_array[y][x].get_text() == 'O':
                        num += 1
                    if game_array[y][x].get_text() == '':
                        position = y
                    if num == win_condition and not position == -1:
                        x1 = x
                        y1 = position
                num = 0
                position = -1
            for p in range(array_size):
                if game_array[p][p].get_text() == 'O':
                    num += 1
                if game_array[p][p].get_text() == '':
                    position = p
                if num == win_condition and not position == -1:
                    x1 = position
                    y1 = position
            num = 0
            position = -1
            for p in range(array_size):
                if game_array[p][2 - p].get_text() == 'O':
                    num += 1
                if game_array[p][2 - p].get_text() == '':
                    position = p
                if num == win_condition and not position == -1:
                    x1 = 2 - position
                    y1 = position
            if x1 == -1 and y1 == -1 and draw(game_array) != 2:
                while True:
                    x1 = random.randint(0, 2)
                    y1 = random.randint(0, 2)
                    if game_array[y1][x1].get_text() == '':
                        break
        game_array[y1][x1].set_text('O')
        game_array[y1][x1].set_pressed(True)
        turn += 1
    return turn


def win(level_number, game_array, array_size, win_condition, catch):
    number_of_x = 0
    number_of_o = 0

    for i in range(array_size):
        for j in range(array_size):
            if game_array[i][j].get_text() == '':
                number_of_x = 0
                number_of_o = 0
            if game_array[i][j].get_text() == 'O':
                number_of_x = 0
                number_of_o += 1
            if game_array[i][j].get_text() == 'X':
                number_of_x += 1
                number_of_o = 0
            if number_of_x == win_condition:
                if level_number % 5 == 0:
                    return 1
                else:
                    return 0
            if number_of_o == win_condition:
                return 3
            if j == array_size - 1:
                number_of_x = 0
                number_of_o = 0

    for i in range(array_size):
        for j in range(array_size):
            if game_array[j][i].get_text() == '':
                number_of_x = 0
                number_of_o = 0
            if game_array[j][i].get_text() == 'O':
                number_of_x = 0
                number_of_o += 1
            if game_array[j][i].get_text() == 'X':
                number_of_x += 1
                number_of_o = 0
            if number_of_x == win_condition:
                if level_number % 5 == 0:
                    return 1
                else:
                    return 0
            if number_of_o == win_condition:
                return 3
            if j == array_size - 1:
                number_of_x = 0
                number_of_o = 0

    for i in range(array_size):
        if game_array[i][i].get_text() == '':
            number_of_x = 0
            number_of_o = 0
        if game_array[i][i].get_text() == 'O':
            number_of_x = 0
            number_of_o += 1
        if game_array[i][i].get_text() == 'X':
            number_of_x += 1
            number_of_o = 0
        if number_of_x == win_condition:
            if level_number % 5 == 0:
                return 1
            else:
                return 0
        if number_of_o == win_condition:
            return 3
        if i == array_size - 1:
            number_of_x = 0
            number_of_o = 0

    for k in range(array_size):
        j = 0
        for i in range(array_size - k):
            if game_array[i][j + k].get_text() == '':
                number_of_x = 0
                number_of_o = 0
            if game_array[i][j + k].get_text() == 'O':
                number_of_o += 1
                number_of_x = 0
            if game_array[i][j + k].get_text() == 'X':
                number_of_x += 1
                number_of_o = 0
            if number_of_x == win_condition:
                if level_number % 5 == 0:
                    return 1
                else:
                    return 0
            if number_of_o == win_condition:
                return 3
            if i == array_size - k - 1:
                number_of_x = 0
                number_of_o = 0
            j += 1

    for k in range(array_size):
        j = 0
        for i in range(array_size - k):
            if game_array[i + k][j].get_text() == '':
                number_of_x = 0
                number_of_o = 0
            if game_array[i + k][j].get_text() == 'O':
                number_of_o += 1
                number_of_x = 0
            if game_array[i + k][j].get_text() == 'X':
                number_of_x += 1
                number_of_o = 0
            if number_of_x == win_condition:
                if level_number % 5 == 0:
                    return 1
                else:
                    return 0
            if number_of_o == win_condition:
                return 3
            if i == array_size - k - 1:
                number_of_x = 0
                number_of_o = 0
            j += 1

    for k in range(array_size):
        j = array_size - 1
        for i in range(array_size - k):
            if game_array[i + k][j].get_text() == '':
                number_of_x = 0
                number_of_o = 0
            if game_array[i + k][j].get_text() == 'O':
                number_of_o += 1
                number_of_x = 0
            if game_array[i + k][j].get_text() == 'X':
                number_of_x += 1
                number_of_o = 0
            if number_of_x == win_condition:
                if level_number % 5 == 0:
                    return 1
                else:
                    return 0
            if number_of_o == win_condition:
                return 3
            if i == array_size - k - 1:
                number_of_x = 0
                number_of_o = 0
            j -= 1

    for k in range(array_size):
        j = array_size - 1
        for i in range(array_size - k):
            if game_array[i][j - k].get_text() == '':
                number_of_x = 0
                number_of_o = 0
            if game_array[i][j - k].get_text() == 'O':
                number_of_o += 1
                number_of_x = 0
            if game_array[i][j - k].get_text() == 'X':
                number_of_x += 1
                number_of_o = 0
            if number_of_x == win_condition:
                if level_number % 5 == 0:
                    return 1
                else:
                    return 0
            if number_of_o == win_condition:
                return 3
            if i == array_size - k - 1:
                number_of_x = 0
                number_of_o = 0
            j -= 1
    return catch


def draw(domain):
    full = 0
    for y in range(len(domain)):
        for x in range(len(domain[0])):
            if not domain[y][x].get_text() == '':
                full += 1
            if full == 9:
                return 2

