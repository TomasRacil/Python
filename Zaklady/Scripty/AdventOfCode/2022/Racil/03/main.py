"""
Solution to 3. day of advent of code 2022
https://adventofcode.com/2022/day/3
"""

from os.path import realpath, dirname, join
from itertools import islice

def priority_sum(input_l: list[chr])->int:
    """Sum prioritie of all characters in input list

    Args:
        input_l (list[chr]): list to sum

    Returns:
        int: sum of priorities
    """
    return sum([(ord(char) - (96 if char.islower() else 38)) for char in input_l])

def chunk(input_l:list, chunk_size:int)->iter:
    """Split list in to same sized chunks

    Args:
        input_l (list): list to split
        chunk_size (int): size of chunk

    Returns:
        iter: iter object of chunks
    """
    arr_range = iter(input_l)
    return iter(lambda: tuple(islice(arr_range, chunk_size)), ())

def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        rucksacs = [line.split('\n')[0] for line in file]

        same_items = [
            list(
                set(rucksac.split('\n')[0][int(len(rucksac)/2):])&
                set(rucksac.split('\n')[0][:int(len(rucksac)/2)])
            )[0]
            for rucksac in rucksacs]

        badges = [
            list(
                set(group[0])&
                set(group[1])&
                set(group[2])
                )[0]
            for group in list(chunk(rucksacs, 3))]

        print(priority_sum(same_items))
        print(priority_sum(badges))


if __name__ == "__main__":
    main()
