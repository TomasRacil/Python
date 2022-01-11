from collections import deque
from os import path


def lanternFishReproduction(fishes, days):
    '''
    function simulate lantern fish population reproduction
    param: list of int - place in array repressent reproduction redines
    param: int - time to simulate
    return: list of int - state of population after x days
    '''
    groups = deque(fishes)
    day = 1
    while day <= days:
        if groups[0] >= 1:
            groups[7] += groups[0]
        groups.rotate(-1)
        day += 1
    return groups


with open(path.join(
        path.dirname(path.realpath(__file__)),
        "input.txt"), "r") as inp:
    fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # assign fishes to indexes baseed on their reproduction age
    for fish in inp.readline().split(","):
        fishes[int(fish)] += 1

# sum whole population of fishes
print(sum(lanternFishReproduction(fishes, 80)))
