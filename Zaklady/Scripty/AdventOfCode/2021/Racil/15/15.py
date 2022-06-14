"""
Solution to 15. day of advent of code 2021
https://adventofcode.com/2021/day/15
"""
from os.path import dirname, join, realpath
from tqdm import tqdm


def dijkstra(cave_map_org:list[list[int]])->int:
    """
    Apply dijkstra algorithm on 2d matrix

    Args:
        cave_map (list[list[int]]): matrix containing cost of path

    Returns:
        list[list[int]]: cost of least expensive path
    """
    cave_map = {
        (y, x): [10000000, ()]
        for x in range(len(cave_map_org[0]))
        for y in range(len(cave_map_org))
    }
    cave_map[0, 0] = [0, (0, 0)]
    pbar = tqdm(total=len(cave_map))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    to_be_visited = {(0, 0): 0}
    while True:
        curent = min(to_be_visited, key=to_be_visited.get)
        neighbors = [
            (curent[0] + direction[0], curent[1] + direction[1])
            for direction in directions
            if curent[0] + direction[0] >= 0
            and curent[0] + direction[0] < len(cave_map_org)
            and curent[1] + direction[1] >= 0
            and curent[1] + direction[1] < len(cave_map_org[0])
            and (curent[0] + direction[0], curent[1] + direction[1])
            != cave_map[curent][1]
        ]
        for row, col in neighbors:
            path_len = cave_map[curent][0] + cave_map_org[row][col]
            if cave_map[(row, col)][0] > path_len:
                to_be_visited[(row, col)] = path_len
                cave_map[(row, col)][0] = path_len
                cave_map[(row, col)][1] = curent
        del to_be_visited[curent]
        pbar.update(1)
        if curent == (len(cave_map_org) - 1, len(cave_map_org[0]) - 1):
            break
    pbar.close()

    return cave_map[len(cave_map_org) - 1, len(cave_map_org[0]) - 1][0]


def expand_map(cave_map:list[list[int]], multiplier: int) -> list[list[int]]:
    """
    Chnage matrix size by a factor of a multiplier.

    Args:
        cave_map (list[list[int]]): map to be increased
        multiplier (int): how many times matrix will increase

    Returns:
        list[list[int]]: expanded map
    """
    temp = []
    for row in range(multiplier):
        for line in cave_map:
            temp.append(
                [
                    org + adition if org + adition <= 9 else org + adition - 9
                    for org, adition in zip(
                        line * 5,
                        sum([[col + row] * len(cave_map[0]) for col in range(5)], []),
                    )
                ]
            )

    return [line for line in temp]


def main():
    """main"""

    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf-8"
    ) as file:
        cave_map = [[int(num) for num in line.strip()] for line in file]

    print("Dijkstra applied on 1x1: ", dijkstra(cave_map))

    cave_map=expand_map(cave_map,5)

    print("Dijkstra applied on 5x5: ", dijkstra(cave_map))


if __name__ == "__main__":
    main()
