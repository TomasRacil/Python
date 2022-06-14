"""
Solution to 9. day of advent of code 2021
https://adventofcode.com/2021/day/9
"""

from math import prod
from os.path import realpath, dirname, join


def find_low_points(terrain: list[list[int]]) -> list[tuple[int, int]]:
    """
    Find all low point in the terrain.

    Args:
        terrain (list[list[int]]): 2D map of risk value

    Returns:
        list[tuple[int, int]]: lit of x,y coordinates
    """
    lowpoints = []

    for row, line in enumerate(terrain):
        for col, num in enumerate(line):
            if (
                (row - 1 >= 0 and terrain[row - 1][col] <= num)
                or (col - 1 >= 0 and terrain[row][col - 1] <= num)
                or (row + 1 < len(terrain) and terrain[row + 1][col] <= num)
                or (col + 1 < len(terrain[0]) and terrain[row][col + 1] <= num)
            ):
                continue
            else:
                lowpoints.append((row, col))
    return lowpoints


def find_basins(
    terrain: list[list[int]], lowpoints: list[tuple[int, int]]
) -> list[list[int]]:
    """
    Locate border of the basins and then fill them with their index value.

    Args:
        terrain (list[list[int]]): 2D map of risk value
        lowpoints (list[tuple[int,int]]): low points on map

    Returns:
        list[list[int]]: map of bazins
    """
    basins = [[0 if num == 9 else -1 for num in line] for line in terrain]

    for idx, lowpoint in enumerate(lowpoints):
        basins[lowpoint[0]][lowpoint[1]] = idx + 1

    while -1 in sum(basins, []):
        for row, line in enumerate(basins):
            for col, field in enumerate(line):
                if field == -1:
                    if row - 1 >= 0 and basins[row - 1][col] > 0:
                        basins[row][col] = basins[row - 1][col]
                    if col - 1 >= 0 and basins[row][col - 1] > 0:
                        basins[row][col] = basins[row][col - 1]
                    if row + 1 < len(basins) and basins[row + 1][col] > 0:
                        basins[row][col] = basins[row + 1][col]
                    if col + 1 < len(line) and basins[row][col + 1] > 0:
                        basins[row][col] = basins[row][col + 1]
    return basins


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf-8"
    ) as file:
        data = [[int(cislo) for cislo in line.strip()] for line in file]

    lowpoints = find_low_points(data)
    print(
        "Sum of risk values of all low points: ",
        sum([data[row][col] + 1 for row, col in lowpoints]),
    )

    basins = find_basins(data, lowpoints)

    d_1 = sum(basins, [])
    sizes = [d_1.count(idx + 1) for idx, _ in enumerate(lowpoints)]
    print("Product of three largest basins: ", prod(sorted(sizes, reverse=True)[:3]))


if __name__ == "__main__":
    main()
