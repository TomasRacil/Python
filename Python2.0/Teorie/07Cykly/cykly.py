podminka = True

while podminka:
    podminka = input("Pro opakování cyklu zadej r: ") == 'r'

i = 1
while i < 6:
    print(i)
    if i == 4:
        print("přerušení cyklu!")
        break
    i += 1

seznam = ['python', 'go', 'kotlin']
for prvek in seznam:
    print(prvek)

veta = "Procházení řetězce písmeno po písmenu"
for pismeno in veta:
    print(pismeno)

for cislo in range(5, 50, 5):
    print(cislo)

i = 1
while i < 6:
    line = ""
    for cislo in range(6):  # Generuje čísla od 0 do 5
        line += str(cislo) + ", "
    print(line)
    i += 1

for i in range(10):
    if i == 5:
        break
    print(i)