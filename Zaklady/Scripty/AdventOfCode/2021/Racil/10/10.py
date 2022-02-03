"""
Solution to 10. day of advent of code 2021
https://adventofcode.com/2021/day/10
"""

from os.path import join, dirname, realpath


def count_err_score(lines: list, scoring: dict) -> tuple[int, list]:
    """
    Calculate total error score in all lines.

    Args:
        lines (list): syntax llist of strings
        scoring (dict): mapping erros to number of error points

    Returns:
        tuple[int, list]: tuple containing total score for all errors
                          and list of lines with syntax errors
    """
    corupted_sum, corupted = 0, []
    for idx, line in enumerate(lines):
        opened = []
        for char in line:
            if char in ["(", "[", "{", "<"]:
                opened.append(char)
            elif abs(ord(char) - ord(opened[-1])) > 2:
                corupted_sum += scoring[char]
                corupted.append(idx)
                break
            else:
                opened.pop()
    return (corupted_sum, corupted)


def autocomplete_scores(incomplete_lines: list, scoring: dict) -> list[int]:
    """[summary]

    Args:
        incomplete_lines (list): [description]
        scoring (dict): [description]

    Returns:
        list[int]: [description]
    """
    incomplete_scores = []

    for line in incomplete_lines:
        opened = []
        score = 0
        for char in line:
            if char in ["(", "[", "{", "<"]:
                opened.append(char)
            else:
                opened.pop()
        for char in opened[::-1]:
            score *= 5
            score += scoring[char]
        incomplete_scores.append(score)
    return incomplete_scores


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [line.strip() for line in file]

    err_scoring = {")": 3, "]": 57, "}": 1197, ">": 25137}
    auto_complete_scoring = {"(": 1, "[": 2, "{": 3, "<": 4}
    corupted_sum, corupted = count_err_score(data, err_scoring)
    incomplete_lines = [line for idx, line in enumerate(data) if idx not in corupted]
    incomplete_scores = autocomplete_scores(incomplete_lines, auto_complete_scoring)

    print(corupted_sum)
    print(sorted(incomplete_scores)[int((len(incomplete_scores) - 1) / 2)])


if __name__ == "__main__":
    main()
