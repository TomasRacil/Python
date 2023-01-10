"""
Solution to 1. day of advent of code 2022
https://adventofcode.com/2022/day/1
"""

from os.path import realpath, dirname, join

def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "test.txt"), "r", encoding="utf_8"
    ) as file:
        data = [sum([int(cal)for  cal in elf.split('\n')]) for elf in file.read().split("\n\n")]
    data.sort(reverse=True)
    print(data[0])
    print(sum(data[0:3]))


if __name__ == "__main__":
    main()
