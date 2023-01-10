"""
Solution to 18. day of advent of code 2022
https://adventofcode.com/2022/day/18
"""

from os.path import realpath, dirname, join
from itertools import zip_longest

def zip_longest_last_value(*args, **kwargs):
    last = (None,) * len(args)
    for x in zip_longest(*args, **kwargs):
        last = tuple(z if z is not None else last[y] for y,z in enumerate(x))
        yield last

def range_not_include(*args, **kwargs):
    if args[0]!=args[1]:
        return list(range(args[0]+1,args[1]))
    else:
        return [args[0]]

def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
        join(dirname(realpath(__file__)), version + ".txt"), "r", encoding="utf_8"
    ) as file:
        droplets = set([tuple(int(coord) for coord in line.split(',')) for line in file.read().split('\n')])
    
    posible_pockets = []
    # posible_pockets = set()
    sum_of_free_sides = 0
    for droplet1 in droplets:
        occupied_sides = 0
        pockets=[]
        for droplet2 in droplets:
            temp = [(one, two) for one,two in zip(droplet1,droplet2) if one!=two]
            if len(temp)==1:
                if abs(temp[0][0]-temp[0][1])==1:
                    occupied_sides+=1
                elif abs(temp[0][0]-temp[0][1])>1:
                    x=range_not_include(*sorted([droplet1[0],droplet2[0]]))
                    y=range_not_include(*sorted([droplet1[1],droplet2[1]]))
                    z=range_not_include(*sorted([droplet1[2],droplet2[2]]))
                    temp_pockets = tuple(zip_longest_last_value(x,y,z)) # generate all posible holes
                    # temp_pockets = tuple(coord[0] if coord[0]==coord[1] else (coord[0]+coord[1])//2 for coord in zip(droplet1,droplet2))
                    if len(set(temp_pockets)&droplets)==0:
                        pockets.extend(temp_pockets)
        # if occupied_sides != 6:
        posible_pockets.extend([pocket for pocket in pockets if pocket not in droplets])
            # posible_pockets.update(pockets)
        sum_of_free_sides+=(6-occupied_sides)
    # print(posible_pockets)
    # res={}
    # for pocket in posible_pockets:
    #     c= posible_pockets.count(pocket)
    #     if c>=6:
    #         res[pocket]= c
    # for key, val in res.items():
    #     print(key,":",val)
    
    non_ideal_pocket = [pocket for pocket in posible_pockets if posible_pockets.count(pocket)<6]
    posible_pockets = set([pocket for pocket in posible_pockets if posible_pockets.count(pocket)>=6])
    
    rounds_without_change = 0
    while True:
        items_to_drop = set()
        for pocket1 in posible_pockets:
            for pocket2 in non_ideal_pocket:
                temp = [(one, two) for one,two in zip(pocket1,pocket2) if one!=two]
                if len(temp)==1:
                    if abs(temp[0][0]-temp[0][1])==1:
                        items_to_drop.add(pocket1)
        posible_pockets = posible_pockets-items_to_drop
                        
        if len(items_to_drop)>0:
            rounds_without_change=0
        else:
            rounds_without_change+=1
        if rounds_without_change==2:
            break
    
    # posible_pockets = posible_pockets-set(droplets)
    print(sum_of_free_sides)
    # print(sorted(list(posible_pockets)))
    
    sum_of_pocket_sides = 0
    for pocket1 in posible_pockets:
        pocket_neigbors=0
        for pocket2 in posible_pockets:
            temp = [(one, two) for one,two in zip(pocket1,pocket2) if one!=two]
            if len(temp)==1:
                if abs(temp[0][0]-temp[0][1])==1:
                    pocket_neigbors+=1
        sum_of_pocket_sides+=(6-pocket_neigbors)
    # print(sum_of_pocket_sides)
    
    print(sum_of_free_sides-sum_of_pocket_sides)
    

if __name__ == "__main__":
    main("input")
