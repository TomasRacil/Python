"""
Solution to 2. day of advent of code 2022
https://adventofcode.com/2024/day/2
"""

from os.path import realpath, dirname, join


def check_diffs(numbers: list[int]) -> bool:
    """Checks if the numbers are sorted (ascending or descending) and the absolute difference between consecutive numbers is between 1 and 3.

    Args:
        numbers (list[int]): numbers to be checked

    Returns:
        bool: retuns True if they fulfill the condition else False
    """
    if not numbers:
        return False
    return all(
        0 > numbers[i] - numbers[i + 1] > -4 for i in range(len(numbers) - 1)
    ) or all(0 < numbers[i] - numbers[i + 1] < 4 for i in range(len(numbers) - 1))


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        levels_list = [
            [int(number) for number in line.split()] for line in file.readlines()
        ]
    # Part 1
    part1 = [levels for levels in levels_list if check_diffs(levels)]
    print(len(part1))

    # Part 2
    part2 = [
        levels
        for levels in levels_list
        if check_diffs(levels)
        or any(
            check_diffs([part for idp, part in enumerate(levels) if idx != idp])
            for idx in range(len(levels))
        )
    ]
    print(len(part2))


if __name__ == "__main__":
    main()
