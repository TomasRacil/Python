"""
Solution to 20. day of advent of code 2021
https://adventofcode.com/2021/day/20
"""

from os import path


def print_image(image: list[list[int]]):
    """
    Print image into the console.

    Args:
        lst (list[list[int]]): [description]
    """
    for row in image:
        print("".join(row).replace("0", ".").replace("1", "#"))


def calculate_bin_value(
    image: list[list[int]], x_coord: int, y_coord: int, char: int
) -> int:
    """
    Create binary number from all pixel in 3x3 matrice.
    Center of this matrix is located on x and y coordinates in the image.

    Args:
        image (list[list[int]]): image to process
        x (int): x coordinate of center of matrix
        y (int): y coordinate of center of matrix
        char (int): value to fill empty positions in matrix

    Returns:
        int: value representing matrix
    """
    directions = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (0, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]
    binary = ""
    for direction in directions:
        if (
            0 <= direction[1] + y_coord
            and direction[1] + y_coord < len(image)
            and 0 <= direction[0] + x_coord
            and direction[0] + x_coord < len(image[0])
        ):
            binary += image[direction[1] + y_coord][direction[0] + x_coord]
        else:
            binary += char
    return int(binary, 2)


def expand_image(image: list[list[int]], char: int) -> list[list[int]]:
    """
    Increase image size horizontaly and verticaly by one.
    New locations are filled wit char

    Args:
        lst (list[list[int]]): original list
        char (str): value to fill empty spaces

    Returns:
        list[list[int]]:new larger list
    """
    radek = [char for _ in range(len(image[0]))]
    return [[char] + row + [char] for row in [radek] + image + [radek]]


def count_ones(image: list[list[int]]) -> int:
    """
    Count all items in image with value of one.

    Args:
        image (list[list[int]]): Image to be counted

    Returns:
        int: Number of ones in image
    """
    val = 0
    for row in image:
        val += row.count("1")
    return val


def enhance_image(
    image: list[list[int]], value_res: list[int], char: int
) -> list[list[int]]:
    """
    Replace items in image based on their binary representation
    and set of rules defined in value_res.

    Args:
        image (list[list[int]]): image to be enhanced
        value_res (list[int]): rules for item replacements
        char (int): value to replace missing spaces

    Returns:
        list[list[int]]: new enhanced image
    """
    image = expand_image(image, char)

    new_image = [[None for col in row] for row in image]
    for idy, row in enumerate(image):
        for idx, _ in enumerate(row):
            val = calculate_bin_value(image, idx, idy, char)
            symbol = value_res[val]
            new_image[idy][idx] = symbol
    return new_image


def main():
    """
    main
    """
    with open(
        path.join(path.dirname(path.realpath(__file__)), "input.txt"),
        "r",
        encoding="utf-8",
    ) as file:
        data = [item for item in file.read().split("\n\n")]
        value_res = ["1" if item == "#" else "0" for item in data[0] if item != "\n"]
        image = [
            ["1" if symbol == "#" else "0" for symbol in line]
            for line in data[1].split("\n")
        ]

    i = 0
    while i < 50:
        image = enhance_image(
            image, value_res, value_res[0] if i % 2 == 0 else value_res[255]
        )
        i += 1
    print(count_ones(image))


if __name__ == "__main__":
    main()
