"""
Solution to 9. day of advent of code 2022
https://adventofcode.com/2022/day/9
"""

from os.path import realpath, dirname, join

def print2darray(l: list[list]):
    """Print 2d list

    Args:
        l (list[list]): 2d list
    """
    for line in l:
        print(line)

# class Tail:
#     x=0
#     y=0
#     history=set()

#     def move_tail(self, x, y):
#         x_dir = x-self.x
#         y_dir = y-self.y
#         if not(abs(x_dir)<=1 and abs(y_dir)<=1):
#             if x_dir == 0 or y_dir == 0:
#                 self.x+= (1 if abs(x_dir)>1 else 0) * (1 if x_dir>0 else -1)
#                 self.y+= (1 if abs(y_dir)>1 else 0) * (1 if y_dir>0 else -1)
#             else:
#                 self.x+=1 if x_dir>0 else -1
#                 self.y+=1 if y_dir>0 else -1
#             self.history.add((self.x,self.y))
   
history=set()
 
class Head:
    x=0
    y=0
    
    next_head = None
    
    def __init__(self,length) -> None:
        if length>0:
            self.next_head = Head(length-1)
    
    def all_positions(self):
        print(self.x,self.y)
        if self.next_head!=None:
            self.next_head.all_positions()
    
    def move(self, moves: list[tuple[str,int]]):
        for move in moves:
            for _ in range(move[1]):
                self.x+=1 if move[0]=='R' else 0
                self.x-=1 if move[0]=='L' else 0
                self.y+=1 if move[0]=='U' else 0
                self.y-=1 if move[0]=='D' else 0
                self.next_head.move_tail(self.x, self.y)
            print(move)
            self.all_positions()
            print("\n")
                

    def move_tail(self, x, y):
        x_dir = x-self.x
        y_dir = y-self.y
        if not(abs(x_dir)<=1 and abs(y_dir)<=1):
            if x_dir == 0 or y_dir == 0:
                self.x+= (1 if abs(x_dir)>1 else 0) * (1 if x_dir>0 else -1)
                self.y+= (1 if abs(y_dir)>1 else 0) * (1 if y_dir>0 else -1)
            else:
                self.x+=1 if x_dir>0 else -1
                self.y+=1 if y_dir>0 else -1
            
            if self.next_head!=None:
                self.next_head.move_tail(self.x, self.y)
            else:
                history.add((self.x,self.y))

                

def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
        join(dirname(realpath(__file__)), version+".txt"), "r", encoding="utf_8"
    ) as file:
        moves = [(line[:-1].split()[0],int(line[:-1].split()[1])) for line in file]
    print(moves)
    h = Head(9)
    h.move(moves)
    print(len(history)+1)
    

if __name__ == "__main__":
    main("input")
