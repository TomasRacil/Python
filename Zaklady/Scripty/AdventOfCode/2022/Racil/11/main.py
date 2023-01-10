"""
Solution to 11. day of advent of code 2022
https://adventofcode.com/2022/day/11
"""

from os.path import realpath, dirname, join
from functools import reduce

op = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}


class Monkey:
    """Mokey class"""

    operation = None
    test = None
    inpections = 0

    def operation_builder(self, operation:str):
        """Build operation from string

        Args:
            operation (str): _description_

        Returns:
            _type_: _description_
        """
        operation = operation.split(" ")[1:]
        return lambda item: op[operation[1]](
            item if operation[0] == "old" else int(operation[0]),
            item if operation[2] == "old" else int(operation[2]),
        )

    def test_builder(self, test, if_true, if_false):
        """Build test from string

        Args:
            test (_type_): _description_
            if_true (_type_): _description_
            if_false (_type_): _description_

        Returns:
            _type_: _description_
        """
        return lambda x: if_true if x % test == 0 else if_false

    def __init__(self, attr: list[str]) -> None:
        self.items = [int(item) for item in attr[1].split(":")[1].split(",")]
        self.operation = self.operation_builder(attr[2].split("=")[1])
        self.test = self.test_builder(
            int(attr[3].split(":")[1].split(" ")[-1]),
            int(attr[4][-1]),
            int(attr[5][-1]),
        )

    def __repr__(self) -> str:
        return f"inspections: {self.inpections}"


def solve(monkeys: list[Monkey], divider: int, version: int):
    """Solve task based on version witch between first and second solution

    Args:
        monkeys (list[Monkey]): _description_
        divider (int): _description_
        version (int): _description_

    Returns:
        _type_: _description_
    """
    for r in range(20 if version == 1 else 10000):
        for monkey in monkeys:
            for item in monkey.items:
                worry_level = (
                    monkey.operation(item) % divider // (3 if version == 1 else 1)
                )
                monkeys[monkey.test(worry_level)].items.append(worry_level)
                monkey.inpections += 1
            monkey.items.clear()
        print(r, end="\r")
    inspections = [monkey.inpections for monkey in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]


def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
        join(dirname(realpath(__file__)), version + ".txt"), "r", encoding="utf_8"
    ) as file:
        monkeys = [monkey.split("\n") for monkey in file.read().split("\n\n")]

    divider = reduce(
        (lambda x, y: x * y),
        [int(monkey[3].split(":")[1].split(" ")[-1]) for monkey in monkeys],
    )

    print(solve([Monkey(monkey) for monkey in monkeys], divider, 1))
    print(solve([Monkey(monkey) for monkey in monkeys], divider, 2))


if __name__ == "__main__":
    main("input")
