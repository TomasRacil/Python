soubor=open(r"C:\Users\Tomáš Ráčil\Desktop\Python\Zaklady\Scripty\Vyuka2021KB\01.txt","r",encoding="utf-8")

# text=soubor.read()
# print(text)

# sum_of_numbers=0
# max_of_numbers=0

# # for item in text.split('\n'):
# for item in soubor:
#     # print(item)
#     if item!='\n':
#         sum_of_numbers+=int(item)
#     else:
#         # print(sum_of_numbers)
#         if max_of_numbers<sum_of_numbers: max_of_numbers=sum_of_numbers
#         sum_of_numbers=0

# if max_of_numbers<sum_of_numbers: max_of_numbers=sum_of_numbers
# print(max_of_numbers)

numbers = [
            sum([int(number)for number in numbers.split('\n')]) 
            for numbers in soubor.read().split('\n\n')
            ]

numbers.sort()

print(numbers[-3:])