

zacitHru = input("Chcete začít hru? (A-ano) \n")

behHry = True

while behHry:
	if zacitHru.lower().strip() == "a":
		print("Hra zacala")

		slovo="__g_c"
		hada=True
		spatnePokusy=0
		while hada:
			print(f" Uhádni nápis  {slovo}")
			tip=input("tipni písmeno")
			if tip in "magic":
				indexPismena="magic".index(tip)
				x=list(slovo)
				x[indexPismena]=tip
				slovo= "".join(x)
				print(f"Ano je soucasti.")
			else:
				print("Není součástí")
				spatnePokusy+=1
				if spatnePokusy > 5:
					behHry=False
					break

		behHry=False
	else:
		behHry=False