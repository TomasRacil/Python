"""
Solution to 12. day of advent of code 2022
https://adventofcode.com/2022/day/12
"""

from os.path import realpath, dirname, join
from itertools import zip_longest

def convert_to_list(representation: str, position:int=0,)->list:
    output, temp=[], ''
    while position<len(representation):
        char = representation[position]
        if char==',':
            if temp!='':
                output.append(int(temp))
            temp=''
        elif char =='[':
            sublist, position = convert_to_list(representation, position+1)
            output.append(sublist)
        elif char == ']':
            if temp!='':
                output.append(int(temp))
            return output, position
        else:temp+=char
        position+=1
    return output[0] if len(output)>0 else None

def check_order(packet_pair: tuple)->bool:
    left, right = packet_pair[0], packet_pair[1]
    test = zip_longest(left, right)
    for pair in test:
        try:
            if pair[0]>pair[1]:
                return False
            elif pair[0]<pair[1]:
                return True
        except Exception as _:
            if pair[0] is None and pair[1] is not None:
                return True
            elif pair[0] is not None and pair[1] is None:
                return False
            elif isinstance(pair[0],list) and isinstance(pair[1],list):
                ret = check_order(pair)
                if ret is not None:
                    return ret
            elif isinstance(pair[0],int) and isinstance(pair[1],list):
                ret = check_order(([pair[0]], pair[1][:]))
                if ret is not None:
                    return ret
            elif isinstance(pair[1],int) and isinstance(pair[0],list):
                ret = check_order((pair[0][:], [pair[1]]))
                if ret is not None:
                    return ret
    return None

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if check_order((array[j],pivot)):
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
        join(dirname(realpath(__file__)), version + ".txt"), "r", encoding="utf_8"
    ) as file:
        packet_pairs = [
            tuple(
                convert_to_list(packet)
                for packet in packet_pair.split('\n')
                )
            for packet_pair in file.read().split('\n\n')
            ]
    sum_of_rights = sum([idx+1 for idx,pair in enumerate(packet_pairs) if check_order(pair)])
    print(sum_of_rights)

    packets = [packet for pair in packet_pairs for packet in pair]
    packets.append([[2]])
    packets.append([[6]])

    quickSort(packets, 0, len(packets)-1)
    idx = [idx+1 for idx, packet in enumerate(packets) if packet in [[[2]],[[6]]]]
    print(idx[0]*idx[1])

if __name__ == "__main__":
    main("input")
