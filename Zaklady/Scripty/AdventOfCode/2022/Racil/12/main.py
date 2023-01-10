"""
Solution to 12. day of advent of code 2022
https://adventofcode.com/2022/day/12
"""

from os.path import realpath, dirname, join
from sys import setrecursionlimit


setrecursionlimit(1750)
vectors = [(-1,0),(1,0),(0,-1),(0,1)]

def calculate_cost(path_map:dict, node:tuple[int,int], cost:int=0):
    """Caculate cost of path to tagret node from every point

    Args:
        path_map (dict): dictionary with node and path cost
        node (tuple[int,int]): target node
        cost (int, optional): cost of path to this node. Defaults to 0.
    """
    path_map[node]['cost']=cost

    paths = [path
            for vector in vectors
            for path in [(node[0]+vector[0],node[1]+vector[1])]
            if path in path_map.keys()
            and path_map[node]['height']-path_map[path]['height'] <=1
            ]

    for path in paths:
        if path_map[path]['cost']>(cost+1):
            calculate_cost(path_map, path, cost+1)


def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
        join(dirname(realpath(__file__)), version + ".txt"), "r", encoding="utf_8"
    ) as file:
        height_map = {
            (y,x):{'cost':162*42, 'height':ord(height)-97}
            for y,row in enumerate(file)
            for x,height in enumerate(row[:-1])
        }
    start = [key for key in height_map if height_map[key]['height']==(ord('S')-97)][0]
    finish = [key for key in height_map if height_map[key]['height']==(ord('E')-97)][0]
    height_map[start]['height']=ord('a')-97
    height_map[finish]['height']=ord('z')-97
    calculate_cost(height_map,finish)
    print(height_map[start]['cost'])
    print(min([val['cost'] for val in height_map.values() if val['height']==0 and val['cost']]))

if __name__ == "__main__":
    main("input")
