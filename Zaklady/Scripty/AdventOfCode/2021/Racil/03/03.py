from os import path
from copy import deepcopy


def getMostCommon(listOfItems):
    '''
    param: list
    return: most common item
    '''
    return max(set(listOfItems), key=listOfItems.count)


def getErasable(col, identifer):
    '''
    identify binaries to be erased based on the passed identifier
    param: list of values
    param: identifier
    return: list (int) -indexes to be erased
    '''
    toErase = []
    for idx, item in enumerate(col):
        if item == identifer:
            toErase.append(idx)
    return toErase


def erase(cols, toErase):
    '''
    erase items from list based on list of indexesed passed
    param: list of lists - to be modified
    param: list (int) -indexes to be erased    
    '''
    for idx, _ in enumerate(cols):
        for index in sorted(toErase, reverse=True):
            del cols[idx][index]


with open(path.join(path.dirname(path.realpath(__file__)),
                    "input.txt"), "r") as f:
    # convert data to 2d field
    binaries = [[bin for bin in line.strip()] for line in f]

# switch rows for cols
cols = [[row[col] for row in binaries] for col in range(len(binaries[0]))]
# create string from most common items
gamma = ''.join([getMostCommon(col) for col in cols])
# get lest coomon bz inverting most commons
epsilon = ''.join(['0' if char == '1' else '1' for char in gamma])
# change from binary to int
gamma_n, epsilon_n = int(gamma, 2), int(epsilon, 2)

print("1:")
print(f"gamma: {gamma_n}\nepsilon: {epsilon_n}\ng*e: {gamma_n*epsilon_n}")

# deep copy of lists
cols_m, cols_l = deepcopy(cols), deepcopy(cols)

# most common
for col in cols_m:
    mostCommon = getMostCommon(col)
    erase(cols_m, getErasable(col, mostCommon))
    if len(cols_m[0]) == 1:
        break

# least common
for col in cols_l:
    leastCommon = '1' if getMostCommon(col) == '0' else '0'
    erase(cols_l, getErasable(col, leastCommon))
    if len(cols_l[0]) == 1:
        break

# converting results to int
o2g = int(''.join(col[0] for col in cols_m), 2)
co2s = int(''.join(col[0] for col in cols_l), 2)

print("\n2:")
print(f"o2g: {o2g}\nco2s: {co2s}\no2g*co2s: {o2g*co2s}")
