"""
Solution to 12. day of advent of code 2021
https://adventofcode.com/2021/day/12
"""

from os.path import join, dirname, realpath

def find_paths(map_of_caves: dict, cave: str, max_visits: int):
    """
    Using recursion find all posible paths through cave system.

    Args:
        map_of_caves (dict): map of caves cave: [visits, {posible paths}]
        cave (str): current cave
        max_visits (int): maximum number of visits to one small cave

    Returns:
        int: number of all posible paths from cave
    """
    twice = (
        True
        if max(
            [
                v[0]
                for (k, v) in map_of_caves.items()
                if (k.islower() and k not in ["start", "end"])
            ]
        )
        >= max_visits
        else False
    )
    map_of_caves[cave][0] += 1
    if cave == "end":
        return 1
    elif cave.islower() and map_of_caves[cave][0] > (1 if twice else 2):
        return 0
    else:
        number_of_paths = 0
        for path in map_of_caves[cave][1]:
            number_of_paths += find_paths(
                {cave: [value[0], value[1]] for (cave, value) in map_of_caves.items()},
                path,
                max_visits,
            )
        return number_of_paths


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        paths = {}
        for line in file:
            first_part = line.strip().split("-")[0]
            second_part = line.strip().split("-")[1]
            if first_part not in paths:
                paths[first_part] = [0, set()]
            if second_part not in paths:
                paths[second_part] = [0, set()]
            if first_part != "start":
                paths[second_part][1].add(first_part)
            if second_part != "start":
                paths[first_part][1].add(second_part)

    paths["end"][1].clear()

    for key, value in paths.items():
        print(key, value)

    print()
    print(find_paths(paths, "start", 1))
    print(find_paths(paths, "start", 2))


if __name__ == "__main__":
    main()
