"""
Solution to 7. day of advent of code 2022
https://adventofcode.com/2022/day/7
"""

from os.path import realpath, dirname, join
import json


def build_file_structure(output:list)->dict:
    """_summary_

    Args:
        output (list): _description_

    Returns:
        dict: _description_
    """
    file_structure={}
    while len(output)>0:
        line=output.pop(0)
        if line[0]=='$':
            if line[1]=='cd':
                if line[2]!="..": file_structure[line[2]]=build_file_structure(output)
                    # if line[2] in file_structure:
                    #     file_structure[line[2]].update(build_file_structure(output))
                    # else:
                else: return file_structure
        else:
            if line[0]!='dir':
                file_structure[line[1]]=int(line[0])
    return file_structure

def get_dir_size(file_structure: dict, dir_sizes:list)->int:
    """_summary_

    Args:
        file_structure (dict): _description_
        dir_sizes (list): _description_

    Returns:
        int: _description_
    """
    dir_sum=0
    for key, val in file_structure.items():
        if isinstance(val, int):
            dir_sum+=val
        else:
            temp=get_dir_size(file_structure[key],dir_sizes)
            dir_sizes.append(temp)
            dir_sum+=temp
    return dir_sum


def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
        join(dirname(realpath(__file__)), version+".txt"), "r", encoding="utf_8"
    ) as file:
        output = [line[:-1].split() for line in file]

    file_structure=build_file_structure(output)

    with open(
        join(dirname(realpath(__file__)),version+".json"), 'w', encoding="utf_8"
        ) as file:
        json.dump(file_structure, file)

    dir_sizes=[]
    get_dir_size(file_structure, dir_sizes)
    print(sum([size for size in dir_sizes if size<=100000]))
    print(min([size for size in dir_sizes if (70000000-max(dir_sizes)+size) >= 30000000]))
    
if __name__ == "__main__":
    main("input")
