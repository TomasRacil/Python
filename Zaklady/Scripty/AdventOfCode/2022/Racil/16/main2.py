"""
Solution to 15. day of advent of code 2022
https://adventofcode.com/2022/day/15
"""

from os.path import realpath, dirname, join
from re import findall

def path_cost(valve_map:dict, valve_map_copy:dict, start: str, current:str, cost:int=0):
    valve_map_copy[current]['tunels'][start]=cost
    for path in valve_map[current]['tunels']:
        if valve_map_copy[path]['tunels'].get(start,100)>cost+1:
            path_cost(valve_map,valve_map_copy, start, path, cost+1)

def calculate_absolute_cost(valve_map:dict, point: str, steps:int, max_steps: int, early_stop:int, visited_items:list=[])->list:
    visited_items.append(point)
    pressure = valve_map[point]['flow_rate']*(max_steps - steps)
    paths=[]
    for cave, val in valve_map[point]['tunels'].items():
        if cave not in visited_items and steps+val+1<early_stop:
            calculated_cost = calculate_absolute_cost(valve_map ,cave, steps+val+1, max_steps, early_stop, visited_items[:])
            processed = [(press+pressure, visited)for press, visited in calculated_cost]
            paths.extend(processed)
    if paths==[]:
        return [(pressure,tuple(visited_items[1:]))]
    return paths

def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
            join(dirname(realpath(__file__)), version + ".txt"), "r", encoding="utf_8"
        ) as file:
            valve_map = {
                line.split()[1]:{
                    'flow_rate': int(findall(r'\d+',line)[0]),
                    'tunels': {path:100 for path in findall('[A-Z]{2}',line.split(';')[1])}
                    } for line in file.read().split('\n')}
        
    valve_map_copy = {key: {k:v if k!='tunels' else {} for k,v in val.items()}for key, val in valve_map.items()}
    
    for key in valve_map:
        path_cost(valve_map,valve_map_copy, key, key)
        
    key_to_drop = [k for k, v in valve_map_copy.items() if v['flow_rate']==0 and k!='AA']
    valve_map_copy = {
        key: {
            'flow_rate':val['flow_rate'],
            'tunels':{k:v for k,v in val['tunels'].items() if k not in key_to_drop+['AA']}}
        for key, val in valve_map_copy.items() if key not in key_to_drop}   
    # print(valve_map_copy)
    all_paths = set()
    for i in range(22,27):
        all_paths.update(set(calculate_absolute_cost(valve_map_copy,'AA',0,26,i,[])))
    print(sorted(all_paths))
    print(len(all_paths))
    best_path=(0,[])
    for path1 in all_paths:
        for path2 in all_paths:
            if len(set(path1[1]) & set(path2[1]))==0:
                # if path1[1]==['JJ','BB','CC']:
                if best_path[0]<path1[0]+path2[0]:
                    best_path = (path1[0]+path2[0],path1[1],path2[1])
                    print(best_path)
                # print(path1[0]+path2[0],path1[1],path2[1])
    print(best_path)
    # print(sorted(posible_paths))
    # posible_combinations = []
    # for val, path in sorted_paths:
    #     posible=[]
    #     for val1,path1 in sorted_paths:
    #         if len(set(path1)&set(path))==0:
    #             posible.append((val1,path1))
    #     try:
    #         # best = max(posible)
    #         posible_combinations.extend([(val+pos[0],(path,pos[1])) for pos in posible])
    #         # posible_combinations.append((val+best[0],(path,best[1])))
    #     except:
    #         pass
    # # print(posible_combinations)
    # print(sorted([(val, visited) for val,visited in posible_combinations  if visited[0][0]=='DD' or visited[0][0]=='JJ']))
if __name__ == "__main__":
    main("input")