from os import path

absolute_path = path.dirname(path.abspath(__file__))

def solve1(data):
    passList = []

    for passData in data:
        temp = {}

        for passEntry in passData.split():
            passKey = passEntry.split(":")[0]
            passValue = passEntry.split(":")[1]

            if (passKey != "cid"):
                temp[passKey] = passValue
        passList.append(temp)

    total = 0
    for key in passList:
        if (len(key) >= 7):
            total += 1

    print("Total valid passList = ", total)

def solve2(data):
    passList = []

    for passData in data:
        temp = {}

        for passEntry in passData.split():
            passKey = passEntry.split(":")[0]
            passValue = passEntry.split(":")[1]

            if (passKey != "cid"):
                temp[passKey] = passValue
        passList.append(temp)

    total = 0

    for p in passList:
        if (len(p) < 7): continue

        ruleBirth = int(p["byr"]) >= 1920 and int(p["byr"]) <= 2002
        ruleIssue = int(p["iyr"]) >= 2010 and int(p["iyr"]) <= 2020
        ruleExpiration = int(p["eyr"]) >= 2020 and int(p["eyr"]) <= 2030

        ruleHeight = False
        if (p["hgt"][-2:] == "in"): ruleHeight = int(p["hgt"][:-2]) >= 59 and int(p["hgt"][:-2]) <= 76
        elif (p["hgt"][-2:] == "cm"): ruleHeight = int(p["hgt"][:-2]) >= 150 and int(p["hgt"][:-2]) <= 193

        ruleHair = p["hcl"][0] == "#" and len(p["hcl"]) == 7
        for character in p["hcl"][1:]:
            if (character not in [range(0,10), 'a', 'b', 'c', 'd', 'e', 'f']): continue

        ruleEye = p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        rulePID = len((p["pid"])) == 9

        if (ruleBirth and ruleIssue and ruleExpiration and ruleHeight and ruleHair and ruleEye and rulePID):
            total += 1

    print("Total valid passList after checking rules = ", total)



data = []

with open(absolute_path + "/4_input.txt", 'r') as file:
    temp = ""
    for line in file:
        if (line.strip()): temp += line.rstrip() + " "
        else: 
            data.append(temp)
            temp = ""

    data.append(temp)

solve1(data)
solve2(data)