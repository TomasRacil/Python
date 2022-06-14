"""
Solution to 14. day of advent of code 2021
https://adventofcode.com/2021/day/14
"""

from functools import lru_cache
from os.path import dirname, join, realpath

DATA=None

@lru_cache(maxsize=1500)
def solve(polymer:str, depth:int)->dict:
    """
    Recursively do polymerization based on polymer tamplates in DATA.

    Args:
        polymer (dict): polymer to undergo polymerization
        depth (int): number of polymeriyation to be done

    Returns:
        dict: polymerized polymer
    """
    if DATA.get(polymer, None) is None or depth == 0:
        return {
            uniqueChar: polymer.count(uniqueChar) for uniqueChar in set(polymer)
        }
    else:
        exp = DATA.get(polymer) + polymer[-1]
        first_part = solve(exp[:2], depth - 1)
        second_part = solve(exp[1:], depth - 1)
        merged_dic = {
            k: first_part.get(k, 0) + second_part.get(k, 0)
            for k in set(first_part) | set(second_part)
        }
        merged_dic[exp[1]] -= 1
        return merged_dic

def proces(polymer:str,steps:int)->dict:
    """
    Apply multiple solve algorithm on polymer based on steps.

    Args:
        polymer (str): polymer to undergo polymerization
        steps (int): number of polymeriyation to be done

    Returns:
        dict: elements and their count
    """
    sum_of_all = {}
    for pol in polymer:
        temp = solve(pol, steps)
        sum_of_all = {
            k: sum_of_all.get(k, 0) + temp.get(k, 0) for k in set(sum_of_all) | set(temp)
        }
    return sum_of_all

def most_least(elements:dict)->int:
    """
    Return number of most - least common elements.

    Args:
        elements (dict): elements and their count
    """
    most_common = max(elements, key=elements.get)
    least_common = min(elements, key=elements.get)
    return elements[most_common] - elements[least_common]

def main():
    """
    main
    """
    with open(join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf-8") as file:
        polymer = file.readline().strip()
        polymer = [polymer[i : i + 2] for i in range(0, len(polymer) - 1, 1)]
        global DATA
        DATA = {
            line.strip().split(" -> ")[0]: line.strip().split(" -> ")[0][0]
            + line.strip().split(" -> ")[1]
            for line in file
            if line.strip() != ""
        }

    sum_of_all = proces(polymer,10)

    print("After 10 steps: ",most_least(sum_of_all))

    sum_of_all = proces(polymer,40)

    print("After 40 steps: ",most_least(sum_of_all))

if __name__=="__main__":
    main()
