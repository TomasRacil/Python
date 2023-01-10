from os.path import join, realpath, dirname

soubor = open(join(dirname(realpath(__file__)), "012020.txt"), "r", encoding="utf-8")

def get_numbers_with_particular_sum(numbers, number_count, target_sum):
    for idx1,number1 in enumerate(numbers):
        for idx2,number2 in enumerate(numbers[idx1:]):
            if number_count==3:
                for idx,number3 in enumerate(numbers[idx2:]):
                    if number1+number2+number3==target_sum:
                        return (number1,number2,number3)
            else:
                if number1+number2==target_sum:
                    return (number1, number2)

numbers = [int(cislo) for cislo in soubor]

print(get_numbers_with_particular_sum(numbers, 2, 2020))
print(get_numbers_with_particular_sum(numbers, 3, 2020))

# for idx, radek in enumerate(soubor):
#     if idx==2:
#         print(int(radek))