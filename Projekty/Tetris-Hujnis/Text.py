import pygame


pygame.font.init()

# OBECNÝ KOMENTÁŘ KE VŠEM FUNKCÍM V TOMTO MODULU:
#       - vstupem je zadaný text, velikost textu, vrstva tisku, souřadnice textu
#       - výstupem je vytisknutý text na zadaných souřadnicích


#text uprostřed okna
def draw_central_text(text, size, color, surface, top_left_x, play_width, top_left_y, play_height):

    font = pygame.font.SysFont('arial', size, bold=True, italic=False)
                                #font,velikost,tučné písmo, kurzíva
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), top_left_y + play_height/2 - label.get_height()/2))
    #blit = draw ... nakreslení textu přes pozadí
    #blit(to co chci kreslit, x_coord, y_coord)
                        #souradnici posunu na stred hraci plochy a odectu sirku a vysku textu vydelenou 2ma, protoze text chci primo na stredu


#text vpravo od hrací plochy
def draw_right_big_text(text, color, surface, sx, sy):

    font = pygame.font.SysFont('arial', 30, bold = True)
    label = font.render(text, 1, color)
    surface.blit(label, (sx + 5, sy - 30))


#text vlevo od hrací plochy (velký)
def draw_left_big_text(text, color, surface, sy):

    font = pygame.font.SysFont('arial', 30, bold = True)
    label = font.render(text, 1, color)
    surface.blit(label, (50, sy - 30))
    
#text vlevo od hrací plochy (malý)
def draw_left_small_text(text, color,surface, sy):
    font = pygame.font.SysFont('arial', 15)
    label = font.render(text, 1, color)

    surface.blit(label, (50,sy))
    