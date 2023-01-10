"""
Solution to 2. day of advent of code 2022
https://adventofcode.com/2022/day/2
"""

from os.path import realpath, dirname, join

to_names = {
    'A':'rock',
    'B':'paper',
    'C':'scizor',
    'X':'rock',
    'Y':'paper',
    'Z':'scizor'
}
to_wl = {
    'X':'loss',
    'Y': 'draw',
    'Z': 'win'
}
rule = {
    'rock':{
        'win':'paper',
        'draw':'rock',
        'loss':'scizor'
        },
    'paper':{
        'draw':'paper',
        'loss':'rock',
        'win':'scizor'
        },
    'scizor':{
        'loss':'paper',
        'win':'rock',
        'draw':'scizor'
        },
}
w_score = {
    'loss':0,
    'draw':3,
    'win':6
}
ch_score = {
    'rock':1,
    'paper':2,
    'scizor':3
}


def prepare(data: list[list[str]])-> list[list[str]]:
    """transform from symbols to full names

    Args:
        data (list[list[str]]): input data

    Returns:
        list[list[str]]: preprocesed data
    """
    return [[to_names[round[0]], to_names[round[1]]]for round in data]

def solve_1 (data: list[list[str]])-> int:
    """Calculate sum of scores for whole data

    Args:
        data (list[list[str]]): input data (preprocesed)

    Returns:
        int: score
    """
    return  sum([
        w_score[
            list(rule[round[0]].keys())[
                list(rule[round[0]].values()).index(round[1])
                ]]+
            ch_score[round[1]]
               for round in data]
        )

def solve_2 (data: list[list[str]])-> int:
    """Preproces data to calculate score

    Args:
        data (list[list[str]]): input data

    Returns:
        int: score
    """
    scoring = [[
        to_names[round[0]], 
        rule[to_names[round[0]]][to_wl[round[1]]]] 
               for round in data]
    return solve_1(scoring)

def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [[items for items in rule.split('\n')[0].split()] for rule in file]

    print(f"First part result: {solve_1(prepare(data))}")
    print(f"Second part result: {solve_2(data)}")

if __name__ == "__main__":
    main()
