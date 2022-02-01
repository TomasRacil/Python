import pygame

#vytvoření hrací plochy - backgroundu, na které reagují padající Shapes
def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
    #list pro každou řadu(row) v gridu barvy(0,0,0) ... 10 čtverců v řadě(column), 20 řad 
 
    #locked_positions = čtverce, které nejsou černé = už spadlé Shapes
    # => přidání těchto souřadnic, jiné barvy, do gridu
    for i in range(len(grid)): # == 20, == y_coord
        for j in range(len(grid[i])): # == 10, == x_coord
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid

#nakreslení mřížované hrací plochy pro lepší přehlednost během hry
def draw_grid(surface, row, col, top_left_x, play_width, top_left_y, play_height, block_size):
    surface_x = top_left_x
    surface_y = top_left_y 
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (surface_x, surface_y+ i*block_size), (surface_x + play_width, surface_y + i * block_size))  # horizontal
        for j in range(col):
            pygame.draw.line(surface, (128,128,128), (surface_x + j * block_size, surface_y), (surface_x + j * block_size, surface_y + play_height))  # vertical
 
#smazání zaplněné řady, posunutí o řádek níž
def full_rows(grid, locked):
    full_rows = 0
    for i in range(len(grid)-1,-1,-1):      #smyčka probíhá od spodu gridu
        row = grid[i]
        if (0, 0, 0) not in row:            #pokud color (0,0,0) není v gridu
            full_rows += 1
            
            current_row_index = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    
    if full_rows > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:  #pro každý key, v listu locked, založené na y hodnotě [(x,y)]        [(0,1), (0,0)] --> [(0,0), (0,1)] ==> všechny pozice, které jsou na stejné y_coord dostaneme za sebou
            x, y = key   #souradnice key --- key = tuple => více pozicí
            if y < current_row_index:  #je y menší než momentální index řady (row)? --- všechno menší než index i (tedy na obrazovce nad touto pozicí) se posune dolů
                newKey = (x, y + full_rows) #+ full_rows ... pokud mažeme více řad zároveň, pak posouváme o tolik řad, kolik jsme smazali
                locked[newKey] = locked.pop(key) #nová pozice locked bude mí stejné barvy, jako předchozí, co se musela posunout

#při del locked[] smažeme celou danou řadu z gridu, proto musíme zároveň jednu přičíst nahoru