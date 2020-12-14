import re

print(len(														#tiskneme a zjišťujeme délku řetězce
	[heslo for heslo in [re.split(r'\W+',radek.strip()) 		#upravujme jednotlivé řádky, rozdělujeme na jednotlivé skupiny znaků pomocí regulárního výrazu a vkládáme je do seznamu
	for radek in open("hesla.txt", "r")] 						#procházíme testový soubor vracíme řádky pro další zpracování
	if int(heslo[0])<=heslo[3].count(heslo[2])<=int(heslo[1])]))#podmínka která nechá v seznamu jen platná hesla, heslo[0] a heslo[1] reprezentuje počet písmen povolených v písmenu pomocí metody count pak počítáme počet konkrétních znaků (heslo[2]) v hesle (heslo[3])

#verze vykonávajíc to samé ale pomocí cyklů místo list comprehension
"""
hesla = [re.split(r'\W+',radek.strip()) for radek in open("hesla.txt", "r")]

pocet = 0
for heslo in hesla:
	if int(heslo[0])<=heslo[3].count(heslo[2])<=int(heslo[1]): pocet+=1

print(pocet)
"""

print(len(
	[heslo for heslo in [re.split(r'\W+',radek.strip()) 								#stejné jako v předchozím
	for radek in open("hesla.txt", "r")] 												#stejné jako v předchozím
	if (heslo[3][int(heslo[0])-1]==heslo[2]) != (heslo[3][int(heslo[1])-1]==heslo[2])]))#kontrolujeme jestli znak heslo[3] na indexu uvedeném v heslo[0] a heslo [1] odpovídá znaku heslo[2] nnásledně využíváme nerovnosti pro ověření že je výraz platný jen tehdy je-li pouze jedna odpověď platná

#verze vykonávajíc to samé ale pomocí cyklů místo list comprehension
"""
hesla = [re.split(r'\W+',radek.strip()) for radek in open("hesla.txt", "r")]

pocet = 0

for heslo in hesla:
	if (heslo[3][int(heslo[0])-1]==heslo[2]) != (heslo[3][int(heslo[1])-1]==heslo[2]): pocet+=1

print(pocet)
"""