import pygame
import random
from Text import draw_left_small_text, draw_left_big_text, draw_right_big_text

# SHAPE FORMATS
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

type = [S, Z, I, O, J, L, T]
color = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
#index 0-6 for shape.type

class Shape(object):
      rows = 20  # y
      columns = 10  # x

      def __init__(self, column, row, shape):
            self.x = column
            self.y = row
            self.shape = shape
            self.color = color[type.index(shape)]
            self.rotation = 0 #0-3

#rozpoznání Shape z listu "type"
# vstup  = shape v podobě listu
# výstup = shape v podobě pozice a určité rotace shape
def convert_shape_format(shape):
      positions =[]
      format = shape.shape[shape.rotation % len(shape.shape)] #rozpoznání rotace v listu

      for i, line in enumerate(format):
            row =list(line)
            for j, column in enumerate(row):
                  if column == '0':
                        positions.append((shape.x + j, shape.y + i)) #přidání pozice, která byla rozpoznána, jako část Shape
      return positions
      
#check, jestli pohyb je možný - kontrola pozic
# vstup  = shape, grid
# výstup = seřazené pozice podle y_coord jsme získali list pozic, které jsou seřazené po řadách => lepší orientace
#          - porovnání těchto pozic s pozicemi, které jsou přípustné pro pohyb (accepted_positions)
def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)] #přidávání do accepted, pokud je i,j v barvě (0,0,0)
    accepted_positions = [j for sub in accepted_positions for j in sub] #předělání 2 dimenzionálního listu do 1 dimenzionálního  ...  [ [(0,1)] , [(2,3)] ] --> [ (0,1) , (2,3)]
    formatted = convert_shape_format(shape) #pro porovnání pozice Shape s ostatními pozicemi, ji přeformátujeme do podoby [(),()]
 
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1: #kontrolujeme pozice na hraací ploše ... negativní hodnota = poloha mimo plochu => bez pohybu
                return False
 
    return True

#check, jestli shape nedosáhli horní hranice hrací plochy => uživatel prohrál
# vstup  = positions
# výstup = true - konec hry
#          false - hra jde dál
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

#vrátí náhodnou Shape na souřadnicích v gridu == na středu hrací plochy nahoře
def get_shape():
    global type, color
 
    return Shape(3, -3, random.choice(type))

#tisk následující shape vpravo od hrací plochy
# vstup  = shape, vrstva tisku, souřadnice
# výstup = vytisknutá shape na určitých souřadnicích
#          + texty kolem hrací plochy pomocí funkcí z modulu Text
def draw_next_shape(shape, surface, top_left_x, play_width, top_left_y, play_height):

    sx = top_left_x + play_width + 55
    sy = top_left_y + play_height/2 - 95
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*30 + 10, sy + i*30 + 10, 30, 30), 0)
 
    #text
    draw_right_big_text('Next Shape: ', (0,0,0), surface, sx + 5, sy - 30)
    draw_left_big_text('Controls: ', (0,0,0), surface, sy - 30)

    draw_left_small_text('move left - left arrow', (0,0,0), surface, sy)
    draw_left_small_text('move right - right arrow', (0,0,0), surface, sy + 20)
    draw_left_small_text('rotate - up arrow', (0,0,0), surface, sy + 40)
    draw_left_small_text('move down - down arrow', (0,0,0), surface, sy + 60)
    draw_left_small_text('jump down - space', (0,0,0), surface, sy + 80)