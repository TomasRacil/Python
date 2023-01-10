"""
Solution to 15. day of advent of code 2022
https://adventofcode.com/2022/day/15
"""

from os.path import realpath, dirname, join
from collections import deque

class Tetris:
    def __init__(self) -> None:
        self.heigts = [0,0,0,0,0,0,0]
    
    def 
    

class Rock:
    def __init__(self, type: int) -> None:
        if type == 0:
            self.shape = [deque([0, 0, 1, 1, 1, 1, 0])]
        elif type == 1:
            self.shape = [
                deque([0, 0, 0, 1, 0, 0, 0]),
                deque([0, 0, 1, 1, 1, 0, 0]),
                deque([0, 0, 0, 1, 0, 0, 0]),
            ]
        elif type == 2:
            self.shape = [
                deque([0, 0, 0, 0, 1, 0, 0]),
                deque([0, 0, 0, 0, 1, 0, 0]),
                deque([0, 0, 1, 1, 1, 0, 0]),
            ]
        elif type == 3:
            self.shape = [
                deque([0, 0, 1, 0, 0, 0, 0]),
                deque([0, 0, 1, 0, 0, 0, 0]),
                deque([0, 0, 1, 0, 0, 0, 0]),
                deque([0, 0, 1, 0, 0, 0, 0]),
            ]
        elif type == 4:
            self.shape = [deque([0, 0, 1, 1, 0, 0, 0]), deque([0, 0, 1, 1, 0, 0, 0])]

    def __repr__(self) -> str:
        return "\n".join(
            ["".join([str(cislo) for cislo in line]) for line in self.shape]
        )

    def shift(self, dir: str):
        for line in self.shape:
            if line[-1] != 1 and dir == ">":
                line.rotate(1)
            elif line[1] != 1 and dir == "<":
                line.rotate(-1)


def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
        join(dirname(realpath(__file__)), version + ".txt"), "r", encoding="utf_8"
    ) as file:
        shifts = [char for char in file.read()]
    rock=Rock(0)
    print(rock)
    for shift in shifts:
        rock.shift(shift)
        print(rock)


if __name__ == "__main__":
    main("test")
