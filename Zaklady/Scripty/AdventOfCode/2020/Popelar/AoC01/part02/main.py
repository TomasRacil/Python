lines = open("input.txt", "r").readlines()
numbers = {int(line.strip()) for line in lines}

for number1 in numbers:
    number11 = 2020-number1

    for number2 in numbers:
        number21 = number11-number2

        for number3 in numbers:
            if number21==number3: goal = number1*number2*number3

print(goal)