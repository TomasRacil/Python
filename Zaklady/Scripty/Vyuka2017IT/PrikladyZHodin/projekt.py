print("Hello world")
jmeno = input("Jak se jmenujete? ")
print(f"Zadal jste jmeno {jmeno}")

cislo = input("zadejte číslo pro dělení desítky")
try:
	delitel = int(cislo)
	podil = 10/delitel
	print(f"{podil}")
except ValueError:
	print("toto není číslo!")
except Exception as e:
	print(f"Neočekávaná chyba {e}")

cislo=input("zadej cislo")
cislo=int(cislo)

if (cislo>10):
	print("cislo vetsi jak deset")

elif (cislo<10):
	print("cislo mensi jak deset")
else:
	print("rovnost")
