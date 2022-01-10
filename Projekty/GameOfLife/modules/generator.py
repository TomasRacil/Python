import math, random
import numpy as np
from shapely.geometry import Point
from shapely.prepared import prep


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
    x, y = np.where((x_[:,np.newaxis] - x0)**2 + (y_ - y0)**2 <= radius**2)
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
    for lat in np.arange(miny, maxy, 1): #spacing set to 1
        for lon in np.arange(minx, maxx, 1):
            points.append(Point((round(lat,4), round(lon,4))))

    # validate if each point falls inside shape using the prepared polygon
    valid_points.extend(filter(prep_polygon.contains, points))
    return valid_points

def generatePolygon( ctrX, ctrY, aveRadius, irregularity, spikeyness, numVerts ) :
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

    irregularity = clip( irregularity, 0,1 ) * 2*math.pi / numVerts
    spikeyness = clip( spikeyness, 0,1 ) * aveRadius

    # generate n angle steps
    angleSteps = []
    lower = (2*math.pi / numVerts) - irregularity
    upper = (2*math.pi / numVerts) + irregularity
    sum = 0
    for i in range(numVerts) :
        tmp = random.uniform(lower, upper)
        angleSteps.append( tmp )
        sum = sum + tmp

    # normalize the steps so that point 0 and point n+1 are the same
    k = sum / (2*math.pi)
    for i in range(numVerts) :
        angleSteps[i] = angleSteps[i] / k

    # now generate the points
    points = []
    angle = random.uniform(0, 2*math.pi)
    for i in range(numVerts) :
        r_i = clip( random.gauss(aveRadius, spikeyness), 0, 2*aveRadius )
        x = ctrX + r_i*math.cos(angle)
        y = ctrY + r_i*math.sin(angle)
        points.append( (int(x),int(y)) )

        angle = angle + angleSteps[i]

    return points

def clip(x, min, max) :
     if( min > max ) :  return x
     elif( x < min ) :  return min
     elif( x > max ) :  return max
     else :             return x
