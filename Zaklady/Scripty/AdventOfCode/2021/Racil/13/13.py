"""
Solution to 13. day of advent of code 2021
https://adventofcode.com/2021/day/13
"""

from os.path import dirname, join, realpath


def fold(
    dots: set[tuple[int, int]], direction: str, place: int
) -> set[tuple[int, int]]:
    """
    Based on folding axis and its location change values of dots and remove same ones.

    Args:
        dots (set[tuple[int,int]]): dots x,y coordinates
        direction (str): folding axis
        place (int): coordinate of axis

    Returns:
        set[tuple[int,int]]: dots on folded paper
    """
    if direction == "y":
        folded_to = {line for line in dots if line[1] < place}
        folded = {
            (line[0], place - 1 - (line[1] - place - 1))
            for line in dots
            if line[1] >= place
        }
    elif direction == "x":
        folded_to = {line for line in dots if line[0] < place}
        folded = {
            (place - 1 - (line[0] - place - 1), line[1])
            for line in dots
            if line[0] >= place
        }
    return folded_to | folded


def to_field(dots: set[tuple[int, int]]) -> list[list[str]]:
    """
    Create 2d matrix based on dots positions. Dots are represented as #

    Args:
        dots (set[tuple[int,int]]): dots x,y coordinates

    Returns:
        list[list[str]]: 2d matrix of trings
    """
    max_x, max_y = 0, 0
    for x_coord, y_coord in dots:
        if x_coord > max_x:
            max_x = x_coord
        if y_coord > max_y:
            max_y = y_coord
    return [
        ["." if not (x, y) in dots else "#" for x in range(max_x + 1)]
        for y in range(max_y + 1)
    ]


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"),
        "r",
        encoding="utf-8",
    ) as file:
        data = file.read().split("\n\n")
    paper = {
        (int(line.strip().split(",")[0]), int(line.strip().split(",")[1]))
        for line in data[0].split("\n")
    }
    fold_inst = [
        (line.split("=")[0][-1], int(line.split("=")[1]))
        for line in data[1].split("\n")
    ]
    first = True
    for direction, place in fold_inst[:]:
        paper = fold(paper, direction, place)
        if first:
            print("Number of dots after first fold: ", len(paper))
            first = False

    for line in to_field(paper):
        print("".join(line))


if __name__ == "__main__":
    main()
