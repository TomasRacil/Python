"""
Solution to 8. day of advent of code 2022
https://adventofcode.com/2022/day/8
"""

from os.path import realpath, dirname, join

def print2darray(l: list[list]):
    for line in l:
        print(line)

def is_visible(forest:list[list[int]],x:int,y:int)->bool:
    height= forest[y][x]
    try:
        left = max(forest[y][:x])
        right = max(forest[y][x+1:])
        top = max([line[x] for line in forest[:y]])
        bottom = max([line[x] for line in forest[y+1:]])
        if height<=left and height<=right and height<=top and height<=bottom:
            return False
        else: return True;
    except ValueError:
        return True;

def smaller(line:list[int], height:int):
    smaller=[]
    while True:
        try:
            tree = line.pop()
        except IndexError:
            break
        if tree<height: smaller.append(tree)
        else: 
            smaller.append(tree)
            break
    return smaller
        

def scenic_score(forest:list[list[int]],x:int,y:int)->int:
    height= forest[y][x]
    left = len(smaller(forest[y][:x],height))
    right = len(smaller(forest[y][x+1:][::-1], height))
    top = len(smaller([line[x] for line in forest[:y]],height))
    bottom = len(smaller([line[x] for line in forest[y+1:]][::-1], height))
    return(left*right*top*bottom)

def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
        join(dirname(realpath(__file__)), version+".txt"), "r", encoding="utf_8"
    ) as file:
        forest = [[int(tree) for tree in line[:-1]] for line in file]

    print2darray(forest)
    visibility = [[1 if is_visible(forest, x,y) else 0 for x,tree in enumerate(line) ]for y,line in enumerate(forest)]
    # print2darray(visibility)
    # print(sum([sum(line) for line in visibility]))
    scenic_scores = [[scenic_score(forest, x,y) for x,_ in enumerate(line) ]for y,line in enumerate(forest)]
    print(max([max(line) for line in scenic_scores]))
if __name__ == "__main__":
    main("input")
