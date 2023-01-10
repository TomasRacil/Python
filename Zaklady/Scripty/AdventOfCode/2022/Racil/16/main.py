"""
Solution to 15. day of advent of code 2022
https://adventofcode.com/2022/day/15
"""

from os.path import realpath, dirname, join
from re import findall
from functools import cache

def print_dict(dictionary:dict, level:int=0):
    return '\n'+'\n'.join(["\t"*level+f"{key}:{print_dict(value,level+1) if isinstance(value, dict) else value }" for key, value in dictionary.items()])


def path_cost(valve_map:dict, valve_map_copy:dict, start: str, current:str, cost:int=0):
    valve_map_copy[current]['tunels'][start]=cost
    for path in valve_map[current]['tunels']:
        if valve_map_copy[path]['tunels'].get(start,100)>cost+1:
            path_cost(valve_map,valve_map_copy, start, path, cost+1)

valve_map2={}
max_pressure = 0
@cache
def calculate_absolute_cost(point: str, steps:int, *visited_items:str)->list:
    visited = list(visited_items)
    visited.append(point)
    # print(visited, end='\r')
    pressure = valve_map2[point]['flow_rate']*(steps+15)
    paths=[]
    for key, val in valve_map2[point]['tunels'].items():
        if key not in visited and steps-val-1>0:
            output = [(x[0]+pressure,x[1]) for x in calculate_absolute_cost(key, steps-val-1, *visited)]
            paths.extend((output))
            # if output[0]>max_pressure:
            #     print(output)
                
    if paths==[]:
        return [(pressure,visited[1:])]
    return paths

def calculate_cost_for_each(point:str, steps:int, to_visit:list):
    x = sorted([((steps-path+1)*valve_map2[cave]['flow_rate'], path, cave, valve_map2[cave]['flow_rate']) for cave, path in valve_map2[point]['tunels'].items() if cave in to_visit],reverse=True)
    return x

def calculate_absolute_cost2(point: str, steps:int):
    to_visit = [key for key in valve_map2.keys() if key!='AA']
    costs = calculate_cost_for_each(point,steps, to_visit)
    going_to = [list(costs[0]),list(costs[1])]
    to_visit.remove(going_to[0][2])
    to_visit.remove(going_to[1][2])
    print(26-steps,",",going_to)
    open_valves=[]
    pressure = 0
    while steps>0:
        going_to[0][1]-=1
        going_to[1][1]-=1
        if going_to[0][1]==-1:
            open_valves.append((going_to[0][3],steps-1))
            try:
                first_calculation = calculate_cost_for_each(going_to[0][2],steps, to_visit)
                second_caculation = calculate_cost_for_each(going_to[1][2],steps-going_to[1][1]-1, to_visit)
                if first_calculation[0][0]>second_caculation[0][0]:
                    going_to[0]=list(first_calculation[0])
                else:
                    going_to[0]=list(first_calculation[1])
                to_visit.remove(going_to[0][2])
                print(26-steps,",",going_to)
            except:
                pass
        if going_to[1][1]==-1:
            open_valves.append((going_to[1][3],steps-1))
            try:
                first_calculation = calculate_cost_for_each(going_to[0][2],steps-going_to[0][1]-2, to_visit)
                second_caculation = calculate_cost_for_each(going_to[1][2],steps, to_visit)
                if first_calculation[0][0]>second_caculation[0][0]:
                    going_to[1]=list(second_caculation[1])
                else:
                    going_to[1]=list(second_caculation[0])
                to_visit.remove(going_to[1][2])
                print(26-steps,",",going_to)
            except:
                pass
        if to_visit==[] and going_to[1][1]< -1 and going_to[0][1]< -1:
            print(open_valves)
            break
        # pressure+= sum(open_valves)
        steps-=1
    print(open_valves)
    # while steps>0:
    #     valve_map2
    #     pressure = valve_map2[point]['flow_rate']*steps
    #     pressure = valve_map2[point]['flow_rate']*steps
        
    #     steps-=1
        

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
    # print(valve_map)
    for key in valve_map:
        path_cost(valve_map,valve_map_copy, key, key)
    key_to_drop = [k for k, v in valve_map_copy.items() if v['flow_rate']==0 and k!='AA']
    global valve_map2
    valve_map2 = {
        key: {
            'flow_rate':val['flow_rate'],
            'tunels':{k:v for k,v in val['tunels'].items() if k not in key_to_drop+['AA']}}
        for key, val in valve_map_copy.items() if key not in key_to_drop}
    # print(key_to_drop)
    # print(print_dict(valve_map2))
    
    sorted_paths = sorted(calculate_absolute_cost('AA',11), reverse=True)
    max_val = 0
    posible_combinations = []
    for val, path in sorted_paths:
        posible=[]
        for val1,path1 in sorted_paths:
            if len(set(path1)&set(path))==0:
                posible.append((val1,path1))
        try:
            best = max(posible)
            posible_combinations.append((val+best[0],(path,best[1])))
        except:
            pass
    print(posible_combinations)
    print(sorted([comb for comb in posible_combinations if comb[1][0][0]=='DD' and  comb[1][1][0]=='JJ']))
    # print(sorted_paths)
    # for val1, path1 in sorted_paths:
    #     for val2,path2 in sorted_paths:
    #         for x in range(1,3):
    #             if val1+val2 >max_val and set(path1[:x])&set(path2[:x])=={}:
    #                 max_val=val1+val2
    #                 selected_paths=(path1,path2)
    # print(max_val)
    # [(val,path) for val, path in sorted_paths]
    
    # calculate_absolute_cost2('AA',26)
    # for steps in range(0,26):
    #     paths = calculate_absolute_cost('AA',26)
        
if __name__ == "__main__":
    main("test")
