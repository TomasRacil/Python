from os import path


def countPositiveChanges(numberList):
    '''
    Function return how many times there is an increase of value
    between two consecutive numbers
    param: list of int
    return: int
    '''
    count = 0
    for i in range(1, len(numberList)):
        if numberList[i-1] < numberList[i]:
            count += 1
    return count


# načtení souboru
with open(path.join(path.dirname(path.realpath(__file__)),
                    "input.txt"), "r") as f:
    numbers = [int(line.strip()) for line in f]

print(f"Počet navýšení o jedna: {countPositiveChanges(numbers)}")

# vytvoření pole obsahující součty tří po sobě jdoucích čísel
slidingWindow = [numbers[i]+numbers[i+1]+numbers[i+2]
                 for i in range(len(numbers)-2)]

print(f"Počet navýšení sliding window: {countPositiveChanges(slidingWindow)}")
