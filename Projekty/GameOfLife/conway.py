import math
import random
import numpy as np
import argparse
from shapely.prepared import prep
from shapely.geometry import Polygon, Point
from matplotlib.patches import Ellipse
import matplotlib.animation as animation
import matplotlib.pyplot as plt


def gen_point_in_circle(radius, x0, y0):

    """
    -----------
    Description
    -----------
    generates coordinates in circle
    -----------
    Parameters
    -----------
    radius of circle, x and y coordinates of center
    -----------
    Returns
    -----------
    list with X coords in list[0] and Y coords in list[1]
    """
    circleX = []
    circleY = []
    x_ = np.arange(x0 - radius - 1, x0 + radius + 1, dtype=int)
    y_ = np.arange(y0 - radius - 1, y0 + radius + 1, dtype=int)
    x, y = np.where((x_[:, np.newaxis] - x0)**2 + (y_ - y0)**2 <= radius**2)
    for x, y in zip(x_[x], y_[y]):
        circleX.append(x)
        circleY.append(y)
    return circleX, circleY


def gen_point_in_polygon(polygon):
    """
    -----------
    Description
    -----------
    Generate spaced points within a shapely Polygon geometry
    -----------
    Parameters
    -----------
    - polygon (shapely.geometry.polygon.Polygon): Polygon geometry
    -----------
    Returns
    -----------
    list of point geometries inside polygon <shapely.geometry.point.Point object at 0x0...>
    """
    valid_points = []
    # determine maximum edges
    minx, miny, maxx, maxy = polygon.bounds

    # create prepared polygon
    prep_polygon = prep(polygon)

    # construct a rectangular mesh
    points = []
    for lat in np.arange(miny, maxy, 1):  # spacing set to 1
        for lon in np.arange(minx, maxx, 1):
            points.append(Point((round(lat, 4), round(lon, 4))))

    # validate if each point falls inside shape using the prepared polygon
    valid_points.extend(filter(prep_polygon.contains, points))
    return valid_points


def generatePolygon(ctrX, ctrY, aveRadius, irregularity, spikeyness, numVerts):
    """
    -----------
    Description
    -----------
    Start with the centre of the polygon at ctrX, ctrY,
    then creates the polygon by sampling points on a circle around the centre.
    Randon noise is added by varying the angular spacing between sequential points,
    and by varying the radial distance of each point from the centre.
    -----------
    Parameters
    -----------
    ctrX, ctrY - coordinates of the "centre" of the polygon
    aveRadius - in px, the average radius of this polygon, this roughly controls how large the polygon is, really only useful for order of magnitude.
    irregularity - [0,1] indicating how much variance there is in the angular spacing of vertices. [0,1] will map to [0, 2pi/numberOfVerts]
    spikeyness - [0,1] indicating how much variance there is in each vertex from the circle of radius aveRadius. [0,1] will map to [0, aveRadius]
    numVerts - self-explanatory
    -----------
    Returns
    -----------
    list of vertices, in CCW order.
    """

    irregularity = clip(irregularity, 0, 1) * 2*math.pi / numVerts
    spikeyness = clip(spikeyness, 0, 1) * aveRadius

    # generate n angle steps
    angleSteps = []
    lower = (2*math.pi / numVerts) - irregularity
    upper = (2*math.pi / numVerts) + irregularity
    sum = 0
    for i in range(numVerts):
        tmp = random.uniform(lower, upper)
        angleSteps.append(tmp)
        sum = sum + tmp

    # normalize the steps so that point 0 and point n+1 are the same
    k = sum / (2*math.pi)
    for i in range(numVerts):
        angleSteps[i] = angleSteps[i] / k

    # now generate the points
    points = []
    angle = random.uniform(0, 2*math.pi)
    for i in range(numVerts):
        r_i = clip(random.gauss(aveRadius, spikeyness), 0, 2*aveRadius)
        x = ctrX + r_i*math.cos(angle)
        y = ctrY + r_i*math.sin(angle)
        points.append((int(x), int(y)))

        angle = angle + angleSteps[i]

    return points


def clip(x, min, max):
    if(min > max):
        return x
    elif(x < min):
        return min
    elif(x > max):
        return max
    else:
        return x


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
            total = int((grid[i, (j-1) % N] + grid[i, (j+1) % N] +
                         grid[(i-1) % N, j] + grid[(i+1) % N, j] +
                         grid[(i-1) % N, (j-1) % N] + grid[(i-1) % N, (j+1) % N] +
                         grid[(i+1) % N, (j-1) % N] + grid[(i+1) % N, (j+1) % N])/255)

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
                        if grid[i, j] == ON:
                            if (total < 2) or (total > 3):
                                newGrid[i, j] = OFF

                        elif total == 3:
                            newGrid[i, j] = ON

                # if not, we are outside of polygon/circle and grid is OFF
                    else:
                        newGrid[i, j] = OFF
                else:
                    newGrid[i, j] = OFF

            # if we dont have polygon
            else:
                # apply Conway's rules
                if grid[i, j] == ON:
                    if (total < 2) or (total > 3):
                        newGrid[i, j] = OFF

                elif total == 3:
                    newGrid[i, j] = ON

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img


def main():
    # parse arguments
    parser = argparse.ArgumentParser(
        description="Runs Conway's Game of Life simulation. See options for controlling the game. Rules will apply to only one shape. With ellipse theres need to define its width and also height.")
    # add arguments
    parser.add_argument('-g', '--grid', dest='N', required=False, default=100,
                        help='define size of grid | example: --grid 20 | default: 100')
    parser.add_argument('-i', '--interval', dest='interval', required=False)
    parser.add_argument('-c', '--circle', dest='radius', required=False,
                        help='define radius of circle, default maximun = grid/2 | example: --circle 20')
    parser.add_argument('-p', '--polygon', dest='verts', required=False,
                        help='define number of vertices in polygon | example: --polygon 20')
    parser.add_argument('-e', '--ellipse', dest='e_param', nargs='+', required=False,
                        help='define width and height values of ellipse | example: --ellipse 10 15')

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
        if radius > N/2:
            radius = N/2

    # set number of verts
    if args.verts and int(args.verts) >= 3:
        verts = int(args.verts)
        polygon = True

    # set animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    if circle is True:
        tmp_list = gen_point_in_circle(radius, N/2, N/2)
        positionX = np.array(tmp_list[0])
        positionY = np.array(tmp_list[1])

    if polygon or ellipse is True:
        # generate random polygon
        if polygon is True:
            poly = generatePolygon(ctrX=N/2, ctrY=N/2, aveRadius=N/3,
                                   irregularity=0.35, spikeyness=0.2, numVerts=verts)
        else:
            ell = Ellipse((N/2, N/2), e_width, e_height,
                          120, ec='b', fill=False)
            poly = ell.get_verts()

        # <shapely.geometry.point.Point object at...>
        geom_pts = gen_point_in_polygon(Polygon(poly))
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
            # copy first coords so that we have closed polygon
            points.append(points[0])
            xs, ys = zip(*points)  # create lists of x and y values

    # declare grid
    grid = np.array([])

    # populate grid with random on/off - more off than on
    grid = randomGrid(N)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, positionX, positionY, polygon, circle, ellipse),
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50)

    if polygon is True:
        plt.plot(xs, ys)
    if circle is True:
        show_circle = plt.Circle((N/2, N/2), radius, ec='b', fill=False)
        ax.add_artist(show_circle)
    if ellipse is True:
        ax.add_patch(ell)

    plt.show()


if __name__ == '__main__':
    main()
