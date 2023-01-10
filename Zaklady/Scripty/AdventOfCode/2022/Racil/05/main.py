"""
Solution to 5. day of advent of code 2022
https://adventofcode.com/2022/day/5
"""

from os.path import realpath, dirname, join
import copy


def print2darray(l: list[list]):
    for line in l:
        print(line)


def reorder(arangment: list[list], orders: list[list], level: int):
    for line in orders:
        arangment[line[2]] += arangment[line[1]][-line[0] :][:: -1 if level == 0 else 1]
        del arangment[line[1]][-line[0] :]
    answer = "".join([stack[-1] for stack in arangment])
    print(answer)


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [section for section in file.read().split("\n\n")]

    arangment_t = [
        [create for create in list(sublist)[::-1] if create != " "]
        for sublist in list(
            zip(
                *[
                    [line[i : i + 1] for i in range(1, len(line), 4)]
                    for line in data[0].split("\n")[:-1]
                ]
            )
        )
    ]

    move_orders = [
        [int(line.split()[1]), int(line.split()[3]) - 1, int(line.split()[5]) - 1]
        for line in data[1].split("\n")
    ]
 
    # print2darray(arangment_t)
    # print2darray(move_orders)

    reorder(copy.deepcopy(arangment_t), move_orders, 0)
    reorder(copy.deepcopy(arangment_t), move_orders, 1)


if __name__ == "__main__":
    main()