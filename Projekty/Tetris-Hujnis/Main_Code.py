import pygame
from Shapes import *
from Text import *
from Grid import *

screen_width = 800      #width = x_coord
screen_height = 700     #height = y_coord
play_width = 300        #300 / 10 = 30 width per block
play_height = 600       #600 / 20 = 20 height per block
block_size = 30
 
top_left_x = (screen_width - play_width) // 2   #šířka okna - šířka hry = top_RIGHT_x ..... //2 = top_left_x .... dvojité lomítko = zaokrouhlení dělení k nejbližšímu celému číslu 15//2 = 7
top_left_y = screen_height - play_height

 #vykreslení okna
def draw_window(surface):
    surface.fill((125,125,125))
    #nadpis Tetris uprostřed okna nad hrací plochou
    font = pygame.font.SysFont('arial', 60, bold=True)
    label = font.render('TETRIS', 1, (0,0,0))
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))
 
    #vykreslení hrací plochy
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* block_size, top_left_y + i * block_size, block_size, block_size), 0)
 
    #okno kolem hrací plochy
    draw_grid(surface, 20, 10, top_left_x, play_width, top_left_y, play_height, block_size)
    pygame.draw.rect(surface, (255, 255, 255), (top_left_x, top_left_y, play_width, play_height), 5)

    #okno kolem Next Shape
    pygame.draw.rect(surface, (255, 255, 255), ((play_width*2) - 10, play_height - 315, (play_width/2) + 50 , (play_height/2) - 120), 5)
    surface.fill((0,0,0), ((play_width*2) - 5, play_height - 310, (play_width/2) + 40 , (play_height/2) - 130))
    # pygame.display.update()

 
def main():
    global grid
 
    locked_positions = {}  
    grid = create_grid(locked_positions)
 
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
 
    while run:
        fall_speed = 0.27
 
        grid = create_grid(locked_positions) #neustále kontrolujeme pozice, jestli se nějaká Shape nepřidala k locked_pos
        fall_time += clock.get_rawtime() #raw.time = čas, který uběhl od posledního clock.tick 
        clock.tick()
 
        # padání Shape
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
 
        #main smyčka s pohybem a ukončením
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
 
            #pohyb
            if event.type == pygame.KEYDOWN:

                #doleva
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                #doprava
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1

                #zrychlení padání
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

                #rotace
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                #skok dolů
                if event.key == pygame.K_SPACE:
                   while valid_space(current_piece, grid):
                       current_piece.y += 1
                   current_piece.y -= 1
                   print(convert_shape_format(current_piece))
 
        shape_pos = convert_shape_format(current_piece) #kontrola Shape, které padá, jestli stále padá, nebo se zastaví a přidá se mezi locked_pos
 
        #přidání Shape do vykreslení gridu
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
 
        #další Shape, při nárazu předchozího
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color # {(x,y):(color,color,color)}
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
 
            full_rows(grid, locked_positions)
 
        draw_window(win)                                                                    #vykreslení okna
        draw_next_shape(next_piece, win, top_left_x, play_width, top_left_y, play_height)   #vykreslení Next Shape
        pygame.display.update()                                                             #update okna
 
        # Check if user lost
        if check_lost(locked_positions):
            run = False
 
    draw_central_text("You Lost", 40, (255,255,255), win, top_left_x, play_width, top_left_y, play_height)
    pygame.display.update()
    pygame.time.delay(2000)
 

def main_menu():
    run = True
    while run:
        win.fill((0,0,0))
        draw_central_text('Press any key to begin.', 60, (255, 255, 255), win, top_left_x, play_width, top_left_y, play_height)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
 
            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()
 
 
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris')
 
main_menu()  # start game