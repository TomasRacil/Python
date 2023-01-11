"""
Solution to 15. day of advent of code 2022
https://adventofcode.com/2022/day/15
"""

from os.path import realpath, dirname, join

def print_2d(l:list):
    for line in l:
        print(line)

class Beacon:
    def __init__(self, coord:tuple) -> None:
        self.x = coord[0]
        self.y = coord[1]
    def __repr__(self) -> str:
        return f"x={self.x}, y={self.y}"
        
class Sensor:
    def __init__(self, data:list[tuple,tuple]) -> None:
        self.x, self.y = data[0]
        self.nearest_beacon = Beacon(data[1])
        self.manhattan_range = abs(self.x-self.nearest_beacon.x) + abs(self.y -self.nearest_beacon.y)
    def __repr__(self) -> str:
        return f"x={self.x}, y={self.y}, range={self.manhattan_range}, beacon={self.nearest_beacon}"

def in_range(sensors: list, y, x)->bool:
    for sensor in sensors:
        if (abs(sensor.x-x)+abs(sensor.y-y))<=sensor.manhattan_range:
            return True
    return False

def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
        join(dirname(realpath(__file__)), version + ".txt"), "r", encoding="utf_8"
    ) as file:
        data = [
            Sensor([tuple(int(section.split('=')[1]) for section in part.split(','))
                    for part in sensor.split(":")]) 
            for sensor in file.read().split('\n')]

    space = 4000001
    # rows=[]
    for radek in range(0,space):
        min_val, max_val=None,None
        ranges=[]
        for sensor in data:
            temp=sensor.manhattan_range-abs(sensor.y-radek)
            if temp>=0:
                t_min_val = sensor.x-temp
                t_max_val = sensor.x+temp
                ranges.append((t_min_val,t_max_val))
        ranges.sort()
        for pair in ranges:
            t_min_val,t_max_val=pair
            if min_val==None:
                min_val, max_val = pair
            else:
                if t_min_val<min_val and t_max_val>=min_val:
                    min_val=t_min_val
                if t_max_val>max_val and t_min_val-1<=max_val:
                    max_val=t_max_val
        if max_val<space or min_val>0:
            print(radek,min_val,max_val)
            # break
        print(radek,end='\r')
    
    
    
if __name__ == "__main__":
    # main("input")
    print(3120101*4000000+2634249)
