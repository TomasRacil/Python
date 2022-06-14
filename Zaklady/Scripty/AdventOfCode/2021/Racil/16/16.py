"""
Solution to 16. day of advent of code 2021
https://adventofcode.com/2021/day/16
"""

import pprint
from os.path import realpath, dirname, join


def prod(lst: list[int]) -> int:
    """
    Multiply all numbers in lst.

    Args:
        lst (list[int]): list of numbers to multiply

    Returns:
        int: product of all numbers in list
    """
    res = 1
    for num in lst:
        res *= num
    return res


def grth(lst: list) -> int:
    """
    Compare first and second number in list.

    Args:
        lst (list): list of numbers

    Returns:
        int: 1 if 1. number > 2. number else 0
    """
    if lst[0] > lst[1]:
        return 1
    else:
        return 0


def smth(lst: list) -> int:
    """
    Compare first and second number in list.

    Args:
        lst (list): list of numbers

    Returns:
        int: 1 if 1. number < 2. number else 0
    """
    if lst[0] < lst[1]:
        return 1
    else:
        return 0


def equl(lst: list) -> int:
    """
    Compare first and second number in list.

    Args:
        lst (list): list of numbers

    Returns:
        int: 1 if 1. number == 2. number else 0
    """
    if lst[0] == lst[1]:
        return 1
    else:
        return 0

operations = {0: sum, 1: prod, 2: min, 3: max, 5: grth, 6: smth, 7: equl}

def get_literal_value(binary: str) -> tuple[int, str]:
    """
    Convert binary into literal value.

    Args:
        binary (str): binary string to be converted

    Returns:
        tuple[int,str]: literal value, rest of binary
    """
    bin_value = ""
    while True:
        bin_value += binary[1:5]
        temp, binary = binary[0], binary[5:]
        if temp == "0":
            break
    return int(bin_value, 2), binary


def identify_packet_structure(binary: str) -> tuple[dict, str]:
    """
    Recursively convert binary string into packet of packets ....

    Args:
        binary (str): string to convert to packets of packets structure

    Returns:
        tuple[dict, str]: dicttionary representing packets, rest of binary string
    """
    packet_structure = {}
    packet_structure["version"], packet_structure["typeId"], binary = (
        int(binary[:3], 2),
        int(binary[3:6], 2),
        binary[6:],
    )
    if packet_structure["typeId"] == 4:
        packet_structure["value"], binary = get_literal_value(binary)
    else:
        packet_structure["operand"] = operations[packet_structure["typeId"]]
        packet_structure["lenghtTypeId"] = int(binary[0])
        if packet_structure["lenghtTypeId"] == 0:
            packet_structure["lenghtValue"], binary, rest = (
                int(binary[1:16], 2),
                binary[16 : 16 + int(binary[1:16], 2)],
                binary[16 + int(binary[1:16], 2) :],
            )
            packet_structure["subpackets"] = []
            while "1" in binary:
                sub_packet, binary = identify_packet_structure(binary)
                packet_structure["subpackets"].append(sub_packet)
            binary = rest

        else:
            packet_structure["lenghtValue"], binary = int(binary[1:12], 2), binary[12:]
            packet_structure["subpackets"] = []
            while len(packet_structure["subpackets"]) < packet_structure["lenghtValue"]:
                sub_packet, binary = identify_packet_structure(binary)
                packet_structure["subpackets"].append(sub_packet)

    return packet_structure, binary


def solve(packet: dict) -> int:
    """
    Recursively solve packets based on operation defined by packets.

    Args:
        packet (dict): packet of packets ...

    Returns:
        int: calculated value of packets
    """
    to_solve = []
    for subpacket in packet["subpackets"]:
        if subpacket["typeId"] == 4:
            to_solve.append(subpacket["value"])
        else:
            to_solve.append(solve(subpacket))
    return packet["operand"](to_solve)

def sum_versions(packet:dict)->int:
    """Recursively sum all versions in packet

    Args:
        packet (dict): packet of packets ....

    Returns:
        int: sum of versions
    """
    version_sum=packet["version"]
    if "subpackets" in packet:
        for subpacket in packet["subpackets"]:
            version_sum+=sum_versions(subpacket)
    return version_sum

def main():
    """
    main
    """
    path = dirname(realpath(__file__))
    with open(
        join(path, "hexadecimal.txt"),
        "r",
        encoding="utf-8",
    ) as file:

        hexa = {
            line.strip().split(" = ")[0]: line.strip().split(" = ")[1] for line in file
        }

    with open(
        join(path, "input.txt"),
        "r",
        encoding="utf-8",
    ) as file:

        binary = "".join([hexa[char] for char in file.readline()])

    to_solve = identify_packet_structure(binary)[0]
    # pprint.pprint(to_solve) # print structure of packets
    print(f"sum of all versions: {sum_versions(to_solve)}")
    print(f"solved packet {solve(to_solve)}")


if __name__ == "__main__":
    main()
