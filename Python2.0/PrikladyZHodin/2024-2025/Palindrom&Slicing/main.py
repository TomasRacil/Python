slovo = input("Zadej slovo: ")

# je_palindorm = True
# for i in range(len(slovo)//2):
#     if slovo[i]!=slovo[-i-1]:
#         je_palindorm = False
#         break


print("Je palindrom" if slovo == slovo[::-1] else "Neni palindrom")


cisla = [1,2,3,4,5,6,7,8,9,10]

print(cisla)

print(cisla[:3])
print(cisla[-2:])
print(cisla[1::2])
cisla_copy = cisla[::]