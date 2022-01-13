import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse
from shapely.geometry import Polygon
from modules import generator as gen
from modules import matrix

def main():
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation. See options for controlling the game. Rules will apply to only one shape. With ellipse theres need to define its width and also height.")
    # add arguments
    parser.add_argument('-g','--grid', dest='N', required=False, default=100, help='define size of grid | example: --grid 20 | default: 100')
    parser.add_argument('-c','--circle', dest='radius', required=False, help='define radius of circle, default maximun = grid/2 | example: --circle 20')
    parser.add_argument('-p','--polygon', dest='verts', required=False, help='define number of vertices in polygon | example: --polygon 20')
    parser.add_argument('-e','--ellipse', dest='e_param', nargs='+', required=False, help='define width and height values of ellipse | example: --ellipse 10 15')
    
    args = parser.parse_args()
    
    # declare every shape
    polygon = False
    circle = False
    ellipse = False
    positionX = []
    positionY = []

    # ellipse - using args to get list
    if args.e_param:
            e_width = int(args.e_param[0])
            e_height = int(args.e_param[1])
            ellipse = True

    # set grid size
    if args.N and int(args.N) > 8:
        N = int(args.N)

    # set circle radius
    if args.radius and int(args.radius) >= 1:
        radius = int(args.radius)
        circle = True
        if radius > N/2: radius = N/2

    # set number of verts
    if args.verts and int(args.verts) >= 3:
        verts = int(args.verts)
        polygon = True

    if circle is True:
        tmp_list = gen.gen_point_in_circle(radius,N/2,N/2)
        positionX = np.array(tmp_list[0])  
        positionY = np.array(tmp_list[1])

    if polygon or ellipse is True:
        # generate random polygon
        if polygon is True:
            poly = gen.generatePolygon( ctrX=N/2, ctrY=N/2, aveRadius=N/3, irregularity=0.35, spikeyness=0.2, numVerts=verts )
        else: 
            ell = Ellipse((N/2, N/2), e_width, e_height, 120, ec='b', fill = False)
            poly = ell.get_verts()
        
        geom_pts = gen.gen_point_in_polygon(Polygon(poly)) # <shapely.geometry.point.Point object at...>
        # conversion of geometry points to lists
        list_x = []
        list_y = []
        for p in geom_pts:
            list_x.append([int(p.x)])
            list_y.append([int(p.y)])
        positionX = np.array(list_x)  
        positionY = np.array(list_y) 
        # preparing image of polygon
        if polygon is True:
            points = poly[:]
            points.append(points[0]) # copy first coords so that we have closed polygon
            xs, ys = zip(*points) # create lists of x and y values

    # declare grid
    grid = np.array([])

    # populate grid with random on/off - more off than on
    grid = matrix.randomGrid(N)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, matrix.update, fargs=(img, grid, N, positionX, positionY, polygon, circle, ellipse),interval=50)

    if polygon is True:
       plt.plot(xs,ys)
    if circle is True:
        show_circle = plt.Circle((N/2, N/2), radius, ec = 'b', fill = False)
        ax.add_artist(show_circle)
    if ellipse is True:
        ax.add_patch(ell)
    
    plt.show()

if __name__ == '__main__':
    main()
