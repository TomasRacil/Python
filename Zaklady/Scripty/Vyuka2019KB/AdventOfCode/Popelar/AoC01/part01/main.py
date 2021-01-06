lines = open("input.txt", "r").readlines()
goal=1

for number in lines:
    number1 = 2020-int(number)

    for number2 in lines:
        if number1==int(number2): goal*=number1

print(goal)