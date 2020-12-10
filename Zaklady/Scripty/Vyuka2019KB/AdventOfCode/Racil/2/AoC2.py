import re

print(len([heslo for heslo in [re.split(r'\W+',radek.strip()) for radek in open("hesla.txt", "r")] 
	if int(heslo[0])<=heslo[3].count(heslo[2])<=int(heslo[1])]))

"""
hesla = [re.split(r'\W+',radek.strip()) for radek in open("hesla.txt", "r")]

pocet = 0
for heslo in hesla:
	if int(heslo[0])<=heslo[3].count(heslo[2])<=int(heslo[1]): pocet+=1

print(pocet)
"""

print(len([heslo for heslo in [re.split(r'\W+',radek.strip()) for radek in open("hesla.txt", "r")] 
	if (heslo[3][int(heslo[0])-1]==heslo[2]) != (heslo[3][int(heslo[1])-1]==heslo[2])]))

"""
hesla = [re.split(r'\W+',radek.strip()) for radek in open("hesla.txt", "r")]

pocet = 0

for heslo in hesla:
	if (heslo[3][int(heslo[0])-1]==heslo[2]) != (heslo[3][int(heslo[1])-1]==heslo[2]): pocet+=1

print(pocet)
"""