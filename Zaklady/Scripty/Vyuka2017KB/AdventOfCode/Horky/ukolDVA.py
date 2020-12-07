
soubor = open("D:/skola UNOB/Python/Sdileny Repozitar GitHub/Python/Zaklady/Scripty/Vyuka2017KB/AdventOfCode/Horky/hesla.txt", "r")

cisla=[]
pocet=0
poc=0
for radek in soubor:
	cisla.append(radek)
	pocet=pocet+1

print(pocet)

for radek in cisla:
	step_0=radek.split(' ')
	step_00=step_0[1]			#pismeno s dvojteckou
	step_heslo=step_0[2]
	step_1=step_0[0]			#cislo oddelene -
	step_cislo=step_1.split('-')	#[0] a [1] cista cisla
	step_3=[dvojtec.strip(':') for dvojtec in step_00]		
	step_pismeno=step_3[0]
	#print ("cislo: "+ str(step_cislo[0]) +" a " + str(step_cislo[1]))  	#oddeleni cisel od zbytku index [0] a [1]
	#print(step_pismeno) 												#pismeno bez dvojtecky
	#print(step_0[2])													#heslo
	pocitadlo=0
	for letter in step_0[2]:
		if letter==step_pismeno:
			pocitadlo=pocitadlo+1
	print("pocet pismen "+ str(step_pismeno) +" v hesle: "+str(step_0[2]) +" je " + str(pocitadlo))
	if pocitadlo>=int(step_cislo[0]) and pocitadlo<=int(step_cislo[1]):
		poc=poc+1
		print("TRUE"+" je v rozmezi: " + str(step_1)+"\n------------------------------------------\n")
	else: print("FALSE "+"neni v rozmezi: " + str(step_1)+"\n------------------------------------------\n")

print ("spravnych hesel :" + str(poc))

#pocitadlo=0

""" #vytvoreni pocitadlo mimo funkc (zkouska)
for radek in cisla:
	a_string=step_0[2]
	pocitadlo=0
	for letter in step_0[2]:
		if letter==step_pismeno:
			pocitadlo=pocitadlo+1
	print("pocet pismen "+ str(step_pismeno) +" v: "+str(step_0[2]) +" je " + str(pocitadlo))
	if pocitadlo>=int(step_cislo[0]) and pocitadlo<=int(step_cislo[1]):
		poc=poc+1
"""