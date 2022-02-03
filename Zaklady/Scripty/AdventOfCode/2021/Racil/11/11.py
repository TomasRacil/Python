"""
Solution to 11. day of advent of code 2021
https://adventofcode.com/2021/day/11
"""

from os.path import join, dirname, realpath


def whos_gonna_flash(
    data: list[list[int]], flashed: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """
    Find items with with value greateer then 9.

    Args:
        data (list[list[int]]): 2D matrix
        flashed (list[tuple[int,int]]): already find items with value > 9

    Returns:
        list[tuple[int,int]]: coordinates of item with value > 9
    """
    going_to_flash = []
    for row, line in enumerate(data):
        for col, octopus in enumerate(line):
            if octopus > 9 and (row, col) not in flashed:
                going_to_flash.append((row, col))
    return going_to_flash


def add_1_around(y_pos: int, x_pos: int, data: list[list[int]]):
    """
    Increase value around position x,y by one.

    Args:
        y_pos (int): y coordinates
        x_pos (int): x coordinates
        data (list[list[int]]): 2D matrix
    """
    directions = [(-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1), (0, 1), (1, 0), (1, 1)]
    for y_change, x_change in directions:
        if not (
            y_pos + y_change >= len(data)
            or y_pos + y_change < 0
            or x_pos + x_change >= len(data[0])
            or x_pos + x_change < 0
        ):
            data[y_pos + y_change][x_pos + x_change] += 1


def add_1_everywhere(data: list[list[int]]):
    """
    Increase value of all item in matrix by one.

    Args:
        data (list[list[int]]): 2D matrix
    """
    for row, line in enumerate(data):
        for col, _ in enumerate(line):
            data[row][col] += 1


def check_sync(data: list[list[int]]) -> bool:
    """
    Check if all values in matrix are the same.

    Args:
        data (list[list[int]]): 2D matrix

    Returns:
        bool: retur true if all items are same else false
    """
    if len(set(sum(data, []))) == 1:
        return True
    else:
        return False


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [[int(octopus) for octopus in line.strip()] for line in file]

    sum_flashes, steps = 0, 0

    while not check_sync(data):
        add_1_everywhere(data)
        flashed, going_to_flash = [], whos_gonna_flash(data, [])

        while len(going_to_flash) > 0:
            for row, col in going_to_flash:
                add_1_around(row, col, data)
                sum_flashes += 1
                flashed.append((row, col))
            flashed.extend(going_to_flash)
            going_to_flash = whos_gonna_flash(data, flashed)

        for row, col in flashed:
            data[row][col] = 0

        steps += 1

    print(sum_flashes)
    print(steps)


if __name__ == "__main__":
    main()
