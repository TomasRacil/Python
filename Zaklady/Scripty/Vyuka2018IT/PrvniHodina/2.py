import random

prijmeni= input("Zadej prijmeni: ")

x_size= int(input("Zadej x pole: "))
y_size= int(input("Zadej y pole: "))

randnums=[[random.randint(-50, 50)for x in range(0,x_size)] for y in range(0,y_size)]

for row in randnums:
    print(row)

s = [[str(e) for e in row] for row in randnums]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print("\n".join(table))


max=randnums[0][0]
min=randnums[0][0]
count=0

for y in randnums:
    for x in y:
        if x < min: min=x
        if x > max: max=x
        if x==len(prijmeni):count+=1

print (f"max= {max}; min= {min}; vyskyty prijmeni= {count}")

