"""1. Program do kterého je možné uložit osobu a datum narození a v případě že má dnes někdo narozeniny tak na to při spuštění upozorní."""
import datetime

def vrat_Dnesni_Datum():
	date=datetime.datetime.now()
	den=format(date.day)
	mesic=format(date.month)
	rok=format(date.year)
	dnesni_Datum=den+"."+mesic+"."+rok
	dnesni_Datum=str(dnesni_Datum)
	return dnesni_Datum

soubor1=open("datumy.txt","r").readlines()
soubor2=open("osoby.txt","r").readlines()
jmeno=input("Zadejte svoje jmeno a prijmeni:")
datum_Narozeni=input("Zadejte svoje datum narozeni:")
dnes=vrat_Dnesni_Datum()
if datum_Narozeni==dnes:
		print("Gratuluji, mate dnes narozeniny!")
else:
	for radek in soubor1:
		if radek!=datum_Narozeni:
			print("Dnes nemate narozeniny!")
			soubor1=open("datumy.txt","a")	
			soubor1.write(datum_Narozeni+"\n")
	
for radek in soubor2:
	if radek==jmeno:
		print("Vase jmeno uz je v souboru")
	elif radek!=jmeno:
		print("Vase jmeno neni v souboru")
		soubor2=open("osoby.txt","a")
		soubor2.write(jmeno+"\n")
	"""try:
					radek==jmeno
					print("Vase jmeno uz je v souboru")
				except Exception as e:
					print("Nastala {e}, vase jmeno neni v souboru")	
					soubor2.write("\n"+jmeno)"""