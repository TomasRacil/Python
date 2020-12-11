"""Rano na UNOBU"""
print("Na otazky odpovidejte ve formatu A,B,C,D")
print("Prave jste dorazil na nastup, pripravte se, ze se vas brzy major na neco zepta!")
otazky=["Proc jste prisel pozde?","2. Vite v kolik mate byt na nastupu?","3. Vy jste chrapal v pracovní dobe?"]
moznosti=["A) Ja jsem myslel, že..., B) Ja jsem zapomnel, ze..., C) Oni mi rikali, ze..., D) Vracel jsem se pro vstupku","A) V 7:00, B) o pet minut predem, C) pet minut predem pred peti minutama, D) 7:05","A) Ano, B) Ne, C) To neni mozny, D) Jenom sem hral kulecnik"]
for otazka in otazky:
	urovenSpokojenosti=0
	print(otazka[0])
	print(moznosti[0])
	odpoved=input()
	if odpoved=="D":
		print("Ti-ti-ticho!")
		urovenSpokojenosti=urovenSpokojenosti+1
	else: 
		print("Kecy,kecy,kecy!!!!!")
		urovenSpokojenosti=urovenSpokojenosti-1	
	print(otazka[1])
	print(moznosti[1])
	odpoved=input()
	if odpoved=="C":
		print("Ti-ti-ticho^2!")
		urovenSpokojenosti=urovenSpokojenosti+1
	else: 
		print("To je hnus!!!!!")		
		urovenSpokojenosti=urovenSpokojenosti-1
	print(otazka[2])
	print(moznosti[2])
	odpoved=input()  
	if odpoved=="D":
		print("Ti-ti-ticho^3!")
		urovenSpokojenosti=urovenSpokojenosti+1
	else: 
		print("Kecy,kecy,kecy!!!!!")	  
		urovenSpokojenosti=urovenSpokojenosti-1
	if urovenSpokojenosti>=2:
		print("Major je s vasi odpovedi spokojeny")
	else: print("Majorovi se z vas chce zvracet")	