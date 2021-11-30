import re

soubor = open("D:/skola UNOB/Python/adventofcode/pas.txt", "r")

pasy=[]
#slovnik={'eyr','pid','iyr','byr','hgt','ecl','hcl','cid'}

for pas in soubor.read().split("\n\n"):	#rozdeleni souboru do jednotlivych pasu podle vynechaneho radku
	 
	
	pasy.append(re.split('[: \n]',pas))	# oddeleni ":", " " a "\n"
	
pocet=0
for pas in pasy:
	#print(pas)
	pocet=pocet+1			#pricitam pocet pasu
	try:
		byr=pas.index("byr")+1
		iyr=pas.index("iyr")+1
		eyr=pas.index("eyr")+1
		hgt=pas.index("hgt")+1
		hcl=pas.index("hcl")+1
		ecl=pas.index("ecl")+1
		pid=pas.index("pid")+1
									#zkusim vyhledat slovicka krome "cid" to je dobrovolne
		#cid=pas.index("cid")+1
	except ValueError:				#pokud slovo nenajdu (nemuzu vratit index) tak odectu od poctu pasu -1 a pokracuju na dalsi
		pocet=pocet-1
		pas.clear()
		continue
	#print(byr,iyr,eyr,hgt,hcl,ecl,pid)

print("pocet spravnych pasu: "+str(pocet))

#----------------------------- DRUHA CAST -----------------------------------#

"""
Zbytecne slozite a roztahane, vim o tom, jen jsem to chtel zkusit timto zpusobem podminek.

Dalo by se to dat do jednoho cyklu a zkusit vsechyn podminky.
Ale rad vidim co se deje v jakym cyklu a muzu si to kontrolovat :)

"""


pocetnew=0
for pas in pasy:
	#print(pas)
	#pocetnew=pocetnew+1			#pricitam pocet pasu
	try:
		byr=pas.index("byr")+1
		if(int(pas[byr])>=1920) and (int(pas[byr])<=2002):
			pocetnew=pocetnew+1
		else:
			pas.clear()
			print("Pas vymazan ze seznamu pasu\n")

		
	except ValueError:
		pas.clear()
		print("Prazdny pas preskocen pasu\n")
		continue

pocetnew=0
for pas in pasy:
	#print(pas)
	#pocetnew=pocetnew+1			#pricitam pocet pasu
	try:
		iyr=pas.index("iyr")+1
		if(int(pas[iyr])>=2010) and (int(pas[iyr])<=2020):
			pocetnew=pocetnew+1
		else:
			pas.clear()
			print("Pas vymazan ze seznamu pasu\n")

		
	except ValueError:
		pas.clear()
		print("Prazdny pas preskocen pasu\n")
		continue

pocetnew=0
for pas in pasy:
	#print(pas)
	#pocetnew=pocetnew+1			#pricitam pocet pasu
	try:
		eyr=pas.index("eyr")+1
		if(int(pas[eyr])>=2020) and (int(pas[eyr])<=2030):
			pocetnew=pocetnew+1
		else:
			pas.clear()
			print("Pas vymazan ze seznamu pasu\n")

		
	except ValueError:
		pas.clear()
		print("Prazdny pas preskocen pasu\n")
		continue

for pas in pasy:
	#print(pas)
	#pocetnew=pocetnew+1			#pricitam pocet pasu
	try:
		hgt=pas.index("hgt")+1
		if 'cm' in str(pas[hgt]):
			print("CM vyska: "+str(pas[hgt]))
			if(int(pas[hgt][0:3])<150) or (int(pas[hgt][0:3])>193):
				pas.clear()
			else: continue
		elif 'in' in str(pas[hgt]):
			print("IN vyska: "+str(pas[hgt]))
			if(int(pas[hgt][0:2])<59) or (int(pas[hgt][0:2])>76):
				pas.clear()
			else: continue
		else:
			pas.clear()
			print("Pas vymazan")
		
	except ValueError:
		pas.clear()
		print("Prazdny pas preskocen pasu\n")
		continue

for pas in pasy:
	#print(pas)
	#pocetnew=pocetnew+1			#pricitam pocet pasu
	try:
		hcl=pas.index("hcl")+1
		if(pas[hcl][0]=="#"):
			if(len(str(pas[hcl]))==7):
				print("Spravny klic Hair Color: "+str(pas[hcl]))	#vynechal jsem kontrolu podminky ze nesmi byt pismeno vetsi nez F
			else:pas.clear()
		else:pas.clear()

	except ValueError:
		pas.clear()
		print("Prazdny pas preskocen pasu\n")
		continue


for pas in pasy:
	#print(pas)
	#pocetnew=pocetnew+1			#pricitam pocet pasu
	try:
		ecl=pas.index("ecl")+1
		if((str(pas[ecl])=="amb") or (str(pas[ecl])=="blu") or (str(pas[ecl])=="brn") or (str(pas[ecl])=="gry") or (str(pas[ecl])=="grn") or (str(pas[ecl])=="hzl") or (str(pas[ecl])=="oth")):
			print("Barva oci sedi a je : " + str(pas[ecl]))
		else: pas.clear()

	except ValueError:
		pas.clear()
		print("Prazdny pas preskocen pasu\n")
		continue

pocetnew=0
for pas in pasy:
	#print(pas)
	pocetnew=pocetnew+1			#pricitam pocet pasu
	try:
		pid=pas.index("pid")+1
		if(len(str(pas[pid]))==9):
			print("Delka PID je 9 kontrola: "+str(pas[pid]))
		else:
			pas.clear()
			pocetnew=pocetnew-1

	except ValueError:
		pas.clear()
		pocetnew=pocetnew-1
		print("Prazdny pas preskocen pasu\n")
		continue

print("Pocet novych pasu : "+str(pocetnew))