
soubor = open("D:/skola UNOB/Python/adventofcode/hesla.txt", "r")
pocitadlo=0
cisla=[]
pocet=0
poc=0
nova=0
for radek in soubor:
	cisla.append(radek)
	pocet=pocet+1

print(pocet)
novehesla=0
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
	#print(step_heslo)													#heslo
	
	if (step_heslo[int(step_cislo[0])-1] == step_pismeno) or (step_heslo[int(step_cislo[1])-1] == step_pismeno):
		nova=nova+1
	if(step_heslo[int(step_cislo[0])-1] == step_pismeno) and (step_heslo[int(step_cislo[1])-1] == step_pismeno):
		nova=nova-1


	pocitadlo=0
	for letter in step_heslo:
		if letter==step_pismeno:
			pocitadlo=pocitadlo+1
	print("pocet pismen "+ str(step_pismeno) +" v hesle: "+str(step_0[2]) +" je " + str(pocitadlo))
	if pocitadlo>=int(step_cislo[0]) and pocitadlo<=int(step_cislo[1]):
		poc=poc+1
		print("TRUE"+" je v rozmezi: " + str(step_1)+"\n------------------------------------------\n")
	else: print("FALSE "+"neni v rozmezi: " + str(step_1)+"\n------------------------------------------\n")

	
print("Nove hesla podle indexu : "+str(nova))







#print ("spravnych hesel :" + str(poc))

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
"""
print("\n\n-----------Nove zadani:----------\n")
novehesla=0
pocitadlo=0
HESlo=step_0[2]
index1=int(step_cislo[0])
index2=int(step_cislo[1])

for c in range(0, len(HESlo)):
    if HESlo[c] == step_pismeno:
    	if (c+1)==index1 :
    		pocitadlo=pocitadlo+1
    		break
    	elif (c+1)== index2:
    		pocitadlo=pocitadlo+1
    		break
    	print("Pismeno: "+step_pismeno+" je na pozici " + str(c)+ " takze " + str(index1) + " nebo: "+str(index2)+" je spravny")
    	print("Jedna se o heslo: "+HESlo+"\n\n\n")
print(pocitadlo)
#for letter in HESlo:
#	if letter ==step_pismeno and ((HESlo.find(letter)+1)==index1 or (HESlo.find(letter)+1)==index2):
#		novehesla=novehesla+1
#		print("index pismena: "+ letter + " je " + str(HESlo.find(letter)+1))

#print(pocitadlo)
#print("v hesle: " + str(HESlo) + "je : " + str(pocitadlo) + "pismen: " + str(step_pismeno) + "na indexu: " + str(index1) + " nebo "+str(index2))
"""
