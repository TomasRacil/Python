"""
Solution to 8. day of advent of code 2022
https://adventofcode.com/2022/day/8
"""

from os.path import realpath, dirname, join

def print2darray(l: list[list]):
    """Print 2d list

    Args:
        l (list[list]): 2d list
    """
    for line in l:
        print(''.join(line))

class Device:
    x=1
    cycle=0
    commands=None
    running_command=None
    sprite = [0,1,2]
    
    def __init__(self, command:list[str]) -> None:
        self.commands = command[::-1]
    
    def do_cycle(self):
        if self.running_command == None:
            com = self.commands.pop()
            try:
                self.running_command=int(com.split()[1])
            except Exception as e:
                pass
        else: 
            self.x+=self.running_command
            self.sprite = [x+self.running_command for x in self.sprite]
            self.running_command=None
        self.cycle+=1

def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
        join(dirname(realpath(__file__)), version+".txt"), "r", encoding="utf_8"
    ) as file:
        commands = [line[:-1] for line in file]

    dev = Device(commands)
    to_sum = []
    # for _ in range(5):
    #     dev.do_cycle()
    #     print(f"{dev.cycle}: {dev.x}")
    while dev.cycle <= 220:
        dev.do_cycle()
        if dev.cycle in [19,59,99,139,179,219]:
            to_sum.append(dev.x*(dev.cycle+1))
    print(sum(to_sum))
    
    dev2 = Device(commands)
    screen = [['.' for x in range(40)]for y in range(6)]
    
    for y,row in enumerate(screen):
        for x,_ in enumerate(row):
            if x in [dev2.x-1,dev2.x,dev2.x+1]:
                screen[y][x]='#'
            dev2.do_cycle()
            # print(''.join(row))
            
    print2darray(screen)
    
if __name__ == "__main__":
    main("input")
