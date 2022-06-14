"""
Suboptimal solution to 8. day of advent of code 2021
https://adventofcode.com/2021/day/8
"""

from os.path import dirname, realpath, join


def to_numbers(pattern:list[set[str]], numbers:list[str])->int:
    """
    Convert numbers to their real value based on the pattern.

    Args:
        pattern (list[set[str]]): pattern representing all numbers
        numbers (list[str]): output nubmbers

    Returns:
        int: value of numbers
    """
    mapping = {"a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": ""}
    mapping["a"] = list(pattern[1] - pattern[0])[0]
    for num in pattern:
        if mapping["a"] in num:
            num.remove(mapping["a"])
    for seg in ["a", "b", "c", "d", "e", "f", "g"]:
        count = 0
        for num in pattern:
            if seg in num:
                count += 1
        if count == 9:
            mapping["f"] = seg
            break
    for num in pattern:
        if mapping["f"] in num:
            num.remove(mapping["f"])
    mapping["c"] = list(pattern[1])[0]
    for num in pattern:
        if mapping["c"] in num:
            num.remove(mapping["c"])
    pattern = pattern[2:]
    mapping["d"] = list(pattern[0] & min(pattern[1:], key=len))[0]
    for num in pattern:
        if mapping["d"] in num:
            num.remove(mapping["d"])
    mapping["b"] = list(pattern[0])[0]
    for num in pattern:
        if mapping["b"] in num:
            num.remove(mapping["b"])
    pattern = pattern[1:]
    mapping["g"] = list(min(pattern, key=len))[0]
    for num in pattern:
        if mapping["g"] in num:
            num.remove(mapping["g"])
    mapping["e"] = list(max(pattern, key=len))[0]
    map_num = [
        {
            mapping["a"],
            mapping["b"],
            mapping["c"],
            mapping["e"],
            mapping["f"],
            mapping["g"],
        },  # 0
        {mapping["c"], mapping["f"]},  # 1
        {mapping["a"], mapping["c"], mapping["e"], mapping["d"], mapping["g"]},  # 2
        {mapping["a"], mapping["c"], mapping["d"], mapping["f"], mapping["g"]},  # 3
        {mapping["b"], mapping["c"], mapping["d"], mapping["f"]},  # 4
        {mapping["a"], mapping["b"], mapping["d"], mapping["f"], mapping["g"]},  # 5
        {
            mapping["a"],
            mapping["b"],
            mapping["d"],
            mapping["e"],
            mapping["f"],
            mapping["g"],
        },  # 6
        {mapping["a"], mapping["c"], mapping["f"]},  # 7
        {
            mapping["a"],
            mapping["b"],
            mapping["c"],
            mapping["d"],
            mapping["e"],
            mapping["f"],
            mapping["g"],
        },  # 8
        {
            mapping["a"],
            mapping["b"],
            mapping["c"],
            mapping["d"],
            mapping["f"],
            mapping["g"],
        },  # 9
    ]
    ret_number = 0
    for number in numbers:
        number_to_set = set([char for char in number])
        for idx, m_number in enumerate(map_num):
            if number_to_set == m_number:
                ret_number *= 10
                ret_number += idx
    return ret_number


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf-8"
    ) as file:
        data = [line.strip().split("|") for line in file]
        outputs = [line[1].split() for line in data]
        patterns = [
            [{char for char in num} for num in sorted(line[0].split(), key=len)]
            for line in data
        ]

    number_of_1478 = 0
    for output in outputs:
        for com in output:
            if len(com) in [2, 3, 4, 7]:
                number_of_1478 += 1
    print("Number of ones fours sevens and eights: ",number_of_1478)

    sum_of_outputs = 0
    for output, pattern in zip(outputs, patterns):
        sum_of_outputs += to_numbers(pattern, output)
    print("Sum of all numbers: ",sum_of_outputs)


if __name__ == "__main__":
    main()
