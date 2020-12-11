zacitHru= input("Chcete zacit hru? (A-ano) ")

behHry=True
while behHry:
	if zacitHru.lower().strip()=="A":
		print("Hra zacala")

		#cinnost= input("Uhadni nápis")
		slovo="__g_c"
		spatnePokusy =0
		hada=True
		while hada:
			print(f" Uhádni nápis {slovo}")
			tip=input("tipni písmeno")
			if tip in "magic":
				indexPismena="magic".index(tip)
				x=list(slovo)
				x[indexPismena]=tip
				slovo="".join(x)
				print("Ano je soucasti")
			else:
				print("Není soucasti")
				spatnePokusy+=1
				if spatnePokusy>5:
					break

		behHry=False
	else:
		behHry=False
		

