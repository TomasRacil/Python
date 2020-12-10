import re

"""
volby=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]#, "cid"]

pasy=[{dvojice.split(":")[0]:dvojice.split(":")[1] for dvojice in pas.split()} for pas in open("pasy.txt", "r").read().split("\n\n")]

pocet=0
for pas in pasy:
	if all (k in pas for k in volby):
		pocet+=1

print(pocet)"""

"""spravnyPocetPoli=[pas for pas in [{dvojice.split(":")[0]:dvojice.split(":")[1] for dvojice in pas.split()} for pas in open("pasy.txt", "r").read().split("\n\n")] if all (k in pas for k in volby)]
print(len(spravnyPocetPoli))


spravnyRokNarozeni=[pas for pas in spravnyPocetPoli if 1920<=int(pas['byr'])<=2002]
print(len(spravnyRokNarozeni))

spravnyRokVydani=[pas for pas in spravnyRokNarozeni if 2010<=int(pas['iyr'])<=2020]
print(len(spravnyRokVydani))

spravnyRokExpirace=[pas for pas in spravnyRokVydani if 2020<=int(pas['eyr'])<=2030]
print(len(spravnyRokExpirace))

spravnaVyska=[pas for pas in spravnyRokExpirace if ((pas['hgt'][-2:]=="cm" and 150<=int(pas['hgt'][:-2])<=193) or (pas['hgt'][-2:]=="in" and 59<=int(pas['hgt'][:-2])<=76))]
print(len(spravnaVyska))

spravnaBarvaVlasu=[pas for pas in spravnaVyska if re.fullmatch(r'#[0-9a-f]{6}', pas['hcl'])]
print(len(spravnaBarvaVlasu))

barvyOci=["amb","blu","brn","gry","grn","hzl","oth"]

spravnaBarvaOci=[pas for pas in spravnaBarvaVlasu if pas['ecl'] in barvyOci]
print(len(spravnaBarvaOci))

spravnePID=[pas for pas in spravnaBarvaOci if re.fullmatch(r"[0-9]{9}",pas['pid'])]
print(len(spravnePID))"""


platnePasy=[pas for pas 
in [{dvojice.split(":")[0]:dvojice.split(":")[1] for dvojice 
in pas.split()} for pas 
in open("pasy.txt", "r").read().split("\n\n")] 
if (all (k in pas for k in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]) 
	and 1920<=int(pas['byr'])<=2002 
	and 2010<=int(pas['iyr'])<=2020
	and 2020<=int(pas['eyr'])<=2030
	and ((pas['hgt'][-2:]=="cm" and 150<=int(pas['hgt'][:-2])<=193) or (pas['hgt'][-2:]=="in" and 59<=int(pas['hgt'][:-2])<=76))
	and re.fullmatch(r'#[0-9a-f]{6}', pas['hcl'])
	and pas['ecl'] in ["amb","blu","brn","gry","grn","hzl","oth"]
	and re.fullmatch(r"[0-9]{9}",pas['pid']))]

print(len(platnePasy))