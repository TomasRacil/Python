import re

hesla=[re.split(r'\W+',radek.strip()) for radek in open("hesla.txt", "r")]

pocet = 0
for heslo in hesla:
	if heslo[3].count(heslo[2])<=int(heslo[1]) and heslo[3].count(heslo[2])>=int(heslo[0]): pocet+=1

print(pocet)

pocet = 0

for heslo in hesla:
	print(heslo)
	if (heslo[3][int(heslo[0])-1]==heslo[2]) != (heslo[3][int(heslo[1])-1]==heslo[2]): pocet+=1

print(pocet)