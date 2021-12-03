from os import path

absolute_path = path.dirname(path.abspath(__file__))

class PassClass:
    def __init__(self, ruleChar, ruleRange, rulePositions, rulePass):
        self.ruleChar = ruleChar
        self.ruleRange = ruleRange
        self.rulePositions = rulePositions
        self.rulePass = rulePass

def solve1(data):
    total = 0

    for line in data:
        if ((line.rulePass.count(line.ruleChar) in line.ruleRange)):
            print("Found valid password = ", line.rulePass, line.ruleRange, line.ruleChar)
            total += 1

    print("Total valid pass count = ", total)

def solve2(data):
    total = 0

    for line in data:
        if ((bool(line.rulePass[line.rulePositions[0]] == line.ruleChar)) ^ (bool(line.rulePass[line.rulePositions[1]] == line.ruleChar))): # XOR
            print(total, "Found valid password = ", line.rulePass, line.rulePositions, line.ruleChar)
            total += 1

    print("Total valid pass count = ", total)



data = []

with open(absolute_path + "/2_input.txt", 'r') as file:
        for line in file:
            dataLine = line.split(' ')

            ruleChar = dataLine[1].split(':')[0]
            ruleRange = range(int(dataLine[0].split('-')[0]), int(dataLine[0].split('-')[1]) + 1)
            rulePositions = (int(dataLine[0].split('-')[0]) - 1, int(dataLine[0].split('-')[1]) - 1)
            rulePass = dataLine[2]

            data.append(PassClass(ruleChar, ruleRange, rulePositions, rulePass))


#solve1(data)
solve2(data)