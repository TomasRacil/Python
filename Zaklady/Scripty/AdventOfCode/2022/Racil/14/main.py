"""
Solution to 14. day of advent of code 2022
https://adventofcode.com/2022/day/14
"""

from os.path import realpath, dirname, join
from itertools import zip_longest

def print_2d(l:list):
    for line in l:
        print(''.join(line))


def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
        join(dirname(realpath(__file__)), version + ".txt"), "r", encoding="utf_8"
    ) as file:
        rock_paths = [
            [
                tuple(int(coord) for coord in pair.split(","))
                for pair in line[:-1].split("->")
            ]
            for line in file
        ]

    flattened = [
        path
        for sublist in [
            [tuple( sorted(list(pair)) for pair in zip(path[idx], path[idx + 1])) for idx in range(len(path) - 1)]
            for path in rock_paths
        ]
        for path in sublist
    ]
    
    ranges=[]
    x_range=[flattened[0][0][0],500]
    y_range=[0,flattened[0][1][-1]]
    for path in flattened:
        xs = list(range(path[0][0],path[0][1]+1))
        ys = list(range(path[1][0],path[1][1]+1))
        if len(xs)==1: xs = xs*len(ys)
        elif len(ys)==1: ys = ys*len(xs)
        for pair in zip(xs,ys):
            ranges.append(pair)
        if max(xs)>x_range[1]: x_range[1]=max(xs)
        if min(xs)<x_range[0]: x_range[0]=min(xs)
        if max(ys)>y_range[1]: y_range[1]=max(ys)
        if min(ys)<y_range[0]: y_range[0]=min(ys)
    
    
    
    y_range[1]+=2
    x_range=[500-y_range[1]-1, 500+y_range[1]+1]
    floor = [(idx, y_range[1]) for idx in range(x_range[0],x_range[1]+1)]
    for pair in floor:
        ranges.append(pair)
    
    print(ranges, x_range,y_range)
    
    map_of_caves=[['#' if (x,y) in ranges else '.' for x in range(x_range[0],x_range[1]+1)] for y in range(y_range[0],y_range[1]+1) ]
    
    
    sand=0
    map_of_caves[0][y_range[1]+1]='+'
    # print_2d(map_of_caves)
    while True:
        sand+=1
        coord=[y_range[1]+1,0]
        if map_of_caves[0][y_range[1]+1]!='+':
            # print(sand-1)
            # print_2d(map_of_caves)
            break
        try:
            while True:
                if map_of_caves[coord[1]+1][coord[0]]=='.':
                    coord[1]+=1
                elif map_of_caves[coord[1]+1][coord[0]-1]=='.':
                    coord[1]+=1
                    coord[0]-=1
                elif map_of_caves[coord[1]+1][coord[0]+1]=='.':
                    coord[1]+=1
                    coord[0]+=1
                else:
                    if [coord[1],coord[0]]==[500-x_range[0],0]:
                        # print(sand)
                        pass
                    else: 
                        map_of_caves[coord[1]][coord[0]]='o'
                        break
            print_2d(map_of_caves)
        except IndexError:
            # map_of_caves[coord[1]][coord[0]]='o'
            # if coord[0]<1:
            #     map_of_caves[coord[1]][coord[0]+1]='o'
            # print_2d(map_of_caves)
            print(sand-1)
            break
if __name__ == "__main__":
    main("input")
