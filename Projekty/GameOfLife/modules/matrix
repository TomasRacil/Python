import numpy as np

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.4, 0.6]).reshape(N, N)

def update(frameNum, img, grid, N, positionX, positionY, polygon, circle, ellipse):
    """
    -----------
    Description
    -----------
    compares and decides life or death of cells in next generation
    -----------
    Parameters
    -----------
    - img: img
    - grid: NxN list with living (ON) and dead (OFF) cells
    - N: size of grid (int)
    - positionX and positionY: list of positions falling under geometry shape
    - polygon, ellipse and circle: distinguish between shapes (True/False values) 
    -----------
    Returns
    -----------
    img with updated dead/alive cells
    """
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neghbor sum
            # using toroidal boundary conditions - x and y wrap around
            # so that the simulaton takes place on a toroidal surface.
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            
            # do we have polygon/circle?
            if polygon or circle or ellipse is True:
                # if vertical position "i" is in list of polygon/circle positions Y
                if i in positionY:
                    # returns tuple with indexes of nums in positionY list, 
                    # example: (array([3, 4, 5, 6, 7, 8], dtype=int64), array([0, 0, 0, 0, 0, 0], dtype=int64))    
                    index_list = np.where(positionY == i)
                    # if horizontal position "j" is in list of polygon positions X
                    # at list position (index) same as the "i" in positions Y  
                    if j in positionX[index_list]:                        
                        # apply Conway's rules
                        if grid[i, j]  == ON:
                            if (total < 2) or (total > 3):
                                newGrid[i, j] = OFF

                        elif total == 3:
                            newGrid[i, j] = ON                
                
                # if not, we are outside of polygon/circle and grid is OFF
                    else: newGrid[i,j] = OFF
                else: newGrid[i, j] = OFF
            
            # if we dont have polygon
            else:
                # apply Conway's rules
                if grid[i, j]  == ON:
                    if (total < 2) or (total > 3):
                        newGrid[i, j] = OFF

                elif total == 3:
                    newGrid[i, j] = ON

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img
