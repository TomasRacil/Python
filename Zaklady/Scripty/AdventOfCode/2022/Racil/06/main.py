"""
Solution to 6. day of advent of code 2022
https://adventofcode.com/2022/day/6
"""

from os.path import realpath, dirname, join


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = file.read()
    split = [idx+4 for idx,_ in enumerate(data) if len(set(data[idx:idx+4]))==4][0]
    print(split)
    
    split = [idx+14 for idx,_ in enumerate(data) if len(set(data[idx:idx+14]))==14][0]
    print(split)

if __name__ == "__main__":
    main()