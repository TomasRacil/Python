"""1. Program do kterého je možné uložit osobu a datum narození a v případě že má dnes někdo narozeniny tak na to při spuštění upozorní."""
soubor1=open("datumy.txt","r").readlines()
jmeno=input("Zadejte svoje jmeno a prijmeni:")
datum_Narozeni=input("Zadejte datum narozeni:")
for radek in soubor1:
	"""print(radek)"""
	radek.strip()
	if radek==datum_Narozeni:
		print("Gratuluji, mate dnes narozeniny!")
	else:
		with open('datumy.txt', mode='w', encoding='utf-8') as soubor1:	
			print("\n")
			print(datum_Narozeni,file=soubor1)	
		print("Dnes nemate narozeniny")	
with open('osoby.txt', mode='w', encoding='utf-8') as soubor2:	
	print("\n")
	print(jmeno,file=soubor2)	

