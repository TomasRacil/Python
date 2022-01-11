from os import path


def median(list):
    """
    idenify median value in the list
    param: list of int
    return: float - median of list
    """
    n = len(list)
    list.sort()

    if n % 2 == 0:
        median1 = list[n//2]
        median2 = list[n//2 - 1]
        return (median1 + median2)/2
    else:
        return list[n//2]


def countFuel1(depths, target):
    """
    calculate sum of fuel consumption to get to target
    from initital depth
    param: list of int - depths
    param: int - target value
    return: int - fuel consumption
    """
    fuel = 0
    for depth in depths:
        fuel += abs(depth-target)
    return fuel


def countFuel2(depths, target):
    """
    calculate sum of fuel consumption to get to target
    from initital depth (increasing cost)
    param: list of int - depths
    param: int - target value
    return: int - fuel consumption
    """
    fuel = 0
    for depth in depths:
        fuel += (abs(depth-target)*(1+abs(depth-target)))/2
    return int(fuel)


with open(path.join(
        path.dirname(path.realpath(__file__)),
        "input.txt"), "r") as file:
    depths = [int(depth) for depth in file.readline().split(",")]


median = int(median(depths))
print(f"1: {countFuel1(depths, median)}")
average = int(sum(depths)/len(depths))
print(f"2: {countFuel2(depths, average)}")
