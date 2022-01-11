from os import path


def drawToMap(vectors, map):
    """
    for each vector defined bz starting and ending point add +1 to map
    param: list of list of lists [[[x,y],[x,y]],...]
    param: list - 2d map
    """
    for line in vectors:
        x1, x2, y1, y2 = line[0][0], line[1][0], line[0][1], line[1][1]

        xs = range(x1, x2+(-1 if x1 > x2 else 1), -
                   1 if x1 > x2 else 1) if x1 != x2 else []
        ys = range(y1, y2+(-1 if y1 > y2 else 1), -
                   1 if y1 > y2 else 1) if y1 != y2 else []
        if len(xs) == 0:
            xs = [x1 for i in range(len(ys))]
        if len(ys) == 0:
            ys = [y1 for i in range(len(xs))]

        y_x = zip(ys, xs)

        for y, x in y_x:
            map[y][x] += 1


def countCrossings(map):
    """
    count all crosing based on value of each field in map
    return: int - number of crossings
    """
    count = 0
    for line in map:
        for item in line:
            if item > 1:
                count += 1
    return count


with open(path.join(
        path.dirname(path.realpath(__file__)),
        "input.txt"), "r") as inp:
    # creating list of vectors from input file
    vectors = [
        [
            [int(line.split("->")[0].strip().split(",")[0]),
             int(line.split("->")[0].strip().split(",")[1])],
            [int(line.split("->")[1].strip().split(",")[0]),
             int(line.split("->")[1].strip().split(",")[1])]
        ]
        for line in inp]

# filtering only horizontal and vertical vectors
vectorsHorVer = list(
    filter(lambda x: (x[0][1] == x[1][1] or x[0][0] == x[1][0]), vectors))

# creating 2d map of zeroes and solving first task
map = [[0 for x in range(0, 1000)] for y in range(0, 1000)]
drawToMap(vectorsHorVer, map)
print(
    f"1. Pruniky horizontalnich a vertikalnich vektoru: {countCrossings(map)}")

# creating 2d map of zeroes and solving second task
map = [[0 for x in range(0, 1000)] for y in range(0, 1000)]
drawToMap(vectors, map)
print(f"2. Pruniky vsech vektory: {countCrossings(map)}")
