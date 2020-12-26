import re

soubor = open("D:/skola UNOB/Python/adventofcode/pas.txt", "r")

pasy=[]
#slovnik={'eyr','pid','iyr','byr','hgt','ecl','hcl','cid'}

for pas in soubor.read().split("\n\n"):	#rozdeleni souboru do jednotlivych pasu podle vynechaneho radku
	 
	
	pasy.append(re.split('[: \n]',pas))	# oddeleni ":", " " a "\n"
	
pocet=0
for pas in pasy:
	print(pas)
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
		continue
	#print(byr,iyr,eyr,hgt,hcl,ecl,pid)

print("pocet spravnych pasu: "+str(pocet))
	