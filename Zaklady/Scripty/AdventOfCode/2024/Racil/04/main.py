"""
Solution to 4. day of advent of code 2024
https://adventofcode.com/2024/day/4
"""

from os.path import realpath, dirname, join
from re import findall, match
import numpy as np


def find_1(lines: list[list[str]], pattern: str) -> int:
    processed_lines = ["".join(line) for line in lines]
    return sum(len(findall(pattern, line)) for line in processed_lines) + sum(
        len(findall(pattern, line[::-1])) for line in processed_lines
    )


def find_2(matricies: list[list[list]], pattern: str) -> int:
    return sum(
        [
            (
                1
                if (
                    (diag1 := "".join(matrix.diagonal())) == pattern
                    or diag1[::-1] == pattern
                )
                and (
                    (diag2 := "".join(np.diag(np.fliplr(matrix)))) == pattern
                    or diag2[::-1] == pattern
                )
                else 0
            )
            for matrix in matricies
        ]
    )


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        lines = np.array([[char for char in line.strip()] for line in file.readlines()])
        columns = np.transpose(lines)
        diagonals = [
            lines[::-1, :].diagonal(i)
            for i in range(-lines.shape[0] + 1, lines.shape[1])
        ]
        diagonals.extend(
            lines.diagonal(i) for i in range(lines.shape[1] - 1, -lines.shape[0], -1)
        )
        print(
            find_1([n.tolist() for n in lines], "XMAS")
            + find_1([n.tolist() for n in columns], "XMAS")
            + find_1([n.tolist() for n in diagonals], "XMAS")
        )
        rows, cols = lines.shape
        matricies = [
            lines[i : i + 3, j : j + 3]
            for i in range(rows - 2)
            for j in range(cols - 2)
        ]
        print(find_2(matricies, "MAS"))


if __name__ == "__main__":
    main()
