"""
Solution to 1. day of advent of code 2024
https://adventofcode.com/2024/day/1
"""

from os.path import realpath, dirname, join


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "test.txt"), "r", encoding="utf_8"
    ) as file:
        lists = [
            sorted(l)
            for l in zip(
                *[
                    (int(number) for number in line.split())
                    for line in file.read().split("\n")
                ]
            )
        ]
    distances = [abs(item - lists[0][idx]) for idx, item in enumerate(lists[1])]
    print(sum(distances))
    simmilarity_scores = [lists[1].count(number) * number for number in lists[0]]
    print(sum(simmilarity_scores))


if __name__ == "__main__":
    main()
