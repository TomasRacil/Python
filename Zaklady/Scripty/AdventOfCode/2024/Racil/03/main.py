"""
Solution to 3. day of advent of code 2024
https://adventofcode.com/2024/day/3
"""

from os.path import realpath, dirname, join
from re import findall


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        operations = findall("(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)", file.read())

        part_1 = [
            int(operation[2]) * int(operation[3])
            for operation in operations
            if operation[3] != "" and operation[2] != ""
        ]
        print(sum(part_1))
        # numbers_to_multiply = findall("mul\((\d+),(\d+)\)", file.read())
        # multiplied = [int(pair[0]) * int(pair[1]) for pair in numbers_to_multiply]
        enabled = True
        multiplication_result = 0
        for operation in operations:
            if operation[1] != "":
                enabled = False
            elif operation[0] != "":
                enabled = True
            elif enabled:
                multiplication_result += int(operation[2]) * int(operation[3])
        print(multiplication_result)


if __name__ == "__main__":
    main()
