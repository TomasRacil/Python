"""
Solution to 4. day of advent of code 2022
https://adventofcode.com/2022/day/4
"""

from os.path import realpath, dirname, join

def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        cleanig_areas = [
            [
                list(range(int(elf.split('-')[0]), int(elf.split('-')[1])+1))
                          for elf in line.split('\n')[0].split(',')
                          ]
                         for line in file
                         ]
    print(cleanig_areas)
    overlaps = [group for group in cleanig_areas if (set(group[0]).issubset(group[1]) or set(group[1]).issubset(group[0]))]
    print(len(overlaps))
    overlaps2 = [group for group in cleanig_areas if set(group[0])&set(group[1])]
    print(len(overlaps2))

if __name__ == "__main__":
    main()
