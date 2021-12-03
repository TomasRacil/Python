text = open("input.txt", "r").readlines()
lines = [x.strip() for x in text]
import re

voc=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eye=["amb","blu","brn","gry","grn","hzl","oth"]
goal, Sum = 0, 0
temp = {}

def rules(record):
    for word in voc:
        if (word not in record): return False
    if not (1920 <= int(record["byr"]) <= 2002): return False
    if not (2010 <= int(record["iyr"]) <= 2020): return False
    if not (2020 <= int(record["eyr"]) <= 2030): return False
    if "cm" in record["hgt"] and not (150 <= int(record["hgt"][:-2]) <= 193): return False
    if "in" in temp["hgt"] and not (59 <= int(temp["hgt"][:-2]) <= 76): return False
    if re.fullmatch(r'#[0-9a-f]{6}', record['hcl']) is None: return False
    if (record["ecl"] not in eye): return False
    if re.fullmatch(r"[0-9]{9}", record['pid']) is None: return False

    return True

for line in lines:
    for i in line.split():
        i=i.split(":")
        temp[i[0]] = i[1]

    if line == "":
        if rules(temp): goal+=1
        temp = {}

print(goal)