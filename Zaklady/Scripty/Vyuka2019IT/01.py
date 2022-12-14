"""Ukázka řešení Advent of Code 2022 den 1"""

soubor = open("/home/tomas/GitHub/Python/Zaklady/Scripty/Vyuka2019IT/01.txt","r",encoding="utf-8")

# print(soubor.read().split('\n\n')[0].split('\n'))

list_of_sums = [
    sum([int(number) for number in item.split('\n')])
    for item in soubor.read().split('\n\n')
    ]
list_of_sums.sort()
print(list_of_sums[-3:])

# # sum_of_numbers= 0
# max_sum, max_sum2, max_sum3 = 0,0,0
# list_of_sum=[]

# for line in soubor:
#     if line == '\n':
#         list_of_sum.append(sum_of_numbers)
#         print(sum_of_numbers)
#         sum_of_numbers = 0
#     else:
#         sum_of_numbers+=int(line)
# list_of_sum.append(sum_of_numbers)

# print(sum_of_numbers)
# print(list_of_sum)
# list_of_sum.sort()
# print(list_of_sum[-3:][::-1])

# print(max_sum,max_sum2, max_sum3)
