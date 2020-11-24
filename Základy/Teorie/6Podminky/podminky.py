"""
V rámci jazyku python podobně jak v dalších programovacích jazycích máme prostředky pro větvení programu v závislostin na splnění určitých podmínek. 
V rámci pythonu je k tomu užíváno výrazů if, else, elif.
"""

#Jednoduchá ukázka snytaxe if else statementu. 
#Pokud má blok kódu jen jeden řádek je možné ho psát přímo za podmínku.
vyraz = input("zadej A jestli souhlasíš: ")=='A'

if vyraz: print("Souhlasíš")
else:
	print("Nesouhlasiš")


#Složitější if větvení používající elif pro specifikování dalších podmínek.
#try používáme pro zabezpečení potenciálních chyb.
try:
	cislo = int(input("zadej cislo: "))

	if cislo>0:
		print(f"{cislo} je větši jak nula")
	elif cislo<0:
		print(f"{cislo} je menši jak nula")
	else:
		print(f"{cislo} je nula")

except ValueError:
	print("Toto není číslo")
except Exception as e:
	print(e)

#Další možnost zápisu je inline podmínka

jmeno = input("Tvoje jméno: ")
#co se stane pokud je podmínka True if podmínka else co se stane pokud je podmínka False
print(f"Tvoje jmeno je {jmeno}") 	if jmeno!="" else print("Nezadal jsi jmeno")

