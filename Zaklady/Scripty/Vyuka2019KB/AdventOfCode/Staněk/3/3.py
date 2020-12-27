from os import path

absolute_path = path.dirname(path.abspath(__file__))

def solve1(data):
    coordX = 0
    coordY = 0
    totalTrees = 0

    for line in range(len(data)):
        if (coordY <= (len(data))):
            if (data[coordY][coordX % len(data[coordY])] == '#'):
                totalTrees += 1
            coordX += 3
            coordY += 1

        else: break

    print("Total trees encountered = ", totalTrees)

def solve2(data):
    multiplyTrees = 1
    slopeTypes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]

    for slope in slopeTypes:
        coordX = 0
        coordY = 0
        totalTrees = 0

        for line in range(len(data)):
            if (coordY <= (len(data))):
                if (data[coordY][coordX % len(data[coordY])] == '#'):
                    totalTrees += 1
                coordX += slope[1]
                coordY += slope[0]

            else: break

        multiplyTrees *= totalTrees
        print("Total trees encountered in", slope, " = ", totalTrees)
    
    print("Total trees multiplied = ", multiplyTrees)



data = []

with open(absolute_path + "/3_input.txt", 'r') as file:
    for line in file:
        data.append(line.rstrip())

solve1(data)
solve2(data)