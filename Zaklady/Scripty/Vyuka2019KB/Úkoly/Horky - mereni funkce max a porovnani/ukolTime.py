import random		#kvuli randint(od,do)
import time			#kvuli zjisteni jak dlouho je projekt spusten

def SeradAvratMax(ZvolList):
	'''Serazeni listu a vraceni posledniho-tedy nejvetsiho cisla'''
	ZvolList.sort()
	return ZvolList[-1]


def NajdiMax(ZvolList):
	'''Nalezeni maxima v listu pomoci cyklu'''
	maximum=ZvolList[0]
	for x in ZvolList:
		if x > maximum:
			maximum=x 
     
	return maximum

def NajdiMin(ZvolList):
	'''Nalezeni minima pres cyklus'''
	minimum=ZvolList[0]
	for x in ZvolList:
		if x < minimum:
			minimum=x 
     
	return minimum

# prazdny list
cisla = [] 
# velikost listu 
try:
	vel = int(input("Zadej počet prvků v listu: "))	
except ValueError:
	print("Toto není číslo, zadejte číslo")	# zadani jineho typu nez cisla
except Exception as e:
	print(f"Neočekávaná vyjímka: \n{e}") 	# ostatni vyjimky

# naplnění listu
for i in range(1, int(vel) + 1): 
    prvek =  random.randint(0,99999)		# random cislo od 0 do 99 999
    cisla.append(prvek) 
#funkce max()
#print(cisla)

zac=time.time()								#do zac se ulozi cas jak dlouho jede projekt

maximum=max(cisla)
print("Nejvetsi prvek:", maximum) 

kon=time.time()								#do kon se ulozi jak dlouho jede projekt
print("Vykonání funkce max() trvalo: "+str(kon-zac))	#od konce odecteme zacatek tak zjistime jak dlouho jela cast mezi koncem a zacatkem
cas1=(kon-zac)		#ulozime si cas(navic)
'''#############################################################################'''

zac2=time.time()

maximum=NajdiMax(cisla)
print("Nejvetsi prvek:", maximum) 

kon2=time.time()

print("Vykonání vlastní funkce NajdiMax trvalo: "+str(kon2-zac2))
cas2=(kon2-zac2)
'''#############################################################################'''

zac3=time.time()

maximum=SeradAvratMax(cisla)
print("Nejvetsi prvek:", maximum) 

kon3=time.time()

print("Vykonání vlastní funkce SeradAvratMax trvalo: "+str(kon3-zac3))
cas3=(kon3-zac3)

##################################################################

casy=[cas1,cas2,cas3]		#vytvoreni listu casu
minCas=NajdiMin(casy)		#nalezeni nejmensiho casu
print("\n\n\nNejrychlejsi nalezeni maxima trvalo: "+str(minCas))

