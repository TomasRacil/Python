class NeniVRozsahu(Exception):
    pass

while True:
	try:
		x=int(input("Zadej: "))
		if x not in range(0,10): raise NeniVRozsahu
		break
	except NeniVRozsahu:
		print("Neni v rozsahu")
	except ValueError:
		print("Neni cislo")
	except Exception as e:
		print(f"Neocekavana vyjimka: {type(e)}")