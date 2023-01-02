from os.path import join, realpath, dirname
from collections import deque

class Ship:
    x=0
    y=0
    direction=deque(['E','S','W','N'])
    
    def __init__(self, path:str) -> None:
        print(path)
        with open(path,'r',encoding='utf-8') as file:
            self.navigation_data = [(line[0],int(line[1:])) for line in file.read().split('\n')]
    
    def __repr__(self) -> str:
        return f"Ship is on coordinates x: {self.x} and y: {self.y} facing {self.direction[0]} manhattan {abs(self.x)+abs(self.y)}"
    
    def rotate(self, direction: str, value: int)->None:
        turn_count = (value//90) * (-1 if direction == 'R' else 1)
        self.direction.rotate(turn_count)
        
    def move(self, direction: str, value: int)->None:
        direction = direction if direction!= 'F' else self.direction[0]
        if direction in ['E','W']:
            self.x = self.x + (value if direction=='E' else -value)
        elif direction in ['N','S']:
            self.y = self.y + (value if direction=='N' else -value)
    
    def navigate(self):
        for command, value in self.navigation_data:
            if command in ['R','L']:
                self.rotate(command, value)
            else:
                self.move(command, value)
        

path_to_file = join(dirname(realpath(__file__)), "ship.txt")
ship=Ship(path_to_file)
print(ship)
# ship.rotate('R',90)
# ship.move('F',10)
ship.navigate()
print(ship)


# soubor = open(join(dirname(realpath(__file__)), "morse.txt"), "r", encoding="utf-8")