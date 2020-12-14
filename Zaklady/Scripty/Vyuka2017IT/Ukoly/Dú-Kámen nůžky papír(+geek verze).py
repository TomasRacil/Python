import random
import time

vyber_hru=input("Zadej jakou verzi si chceš zahrát -> 1-Kámen Nůžky Papír \t 2-Geek Verze \n")

vyhra =int(0) 
vyhra_pc =int(0)
cislo=int(0)
if vyber_hru == "1":
	print("Vybrali jste si Normální verzi:\n")
	for cislo in range(3):
		seznam=["1","2","3"]
		tah_ui= random.choice(seznam)
		muj_tah= input ("Zadej svuj výběr: Kámen(3),Nůžky(2),Papír(1)\n")
		#Muj tah
		if muj_tah == "1":
			muj_tah = "Papír"
			print("Vybral sis Papír\n")
		if muj_tah == "2":
			muj_tah = "Nůžky"
			print("Vybral sis Nůžky\n")
		if muj_tah == "3":
			muj_tah = "Kámen"
			print("Vybral sis Kámen\n")	

		# Tah CPU
		if tah_ui== "1" :
			tah_ui = "Papír"
			print("PC si vybral Papír\n")
		if tah_ui == "2":
			tah_ui = "Nůžky"
			print("PC si vybral Nůžky\n")
		if tah_ui == "3":
			tah_ui = "Kámen"
			print("PC si vybral Kámen\n")
	
		#Vyhodnocení hry

		if muj_tah == tah_ui:
			print("Remíza")
			time.sleep(1)
		elif ((muj_tah == "Papír") and (tah_ui == "Kámen") or (muj_tah == "Nůžky") and (tah_ui == "Papír") or (muj_tah == "Kámen") and (tah_ui == "Nůžky")):
			print("Vyhrál jsi!\n\n")
			vyhra+=1
			time.sleep(1)
		else:
			print("Prohrál jsi!\n\n")
			vyhra_pc +=1
			time.sleep(1)
	if vyhra_pc>vyhra :
	
		print(f"Celkové skóre je: {vyhra} Ty a {vyhra_pc} Počítač \n\n \t\tVýsledek je:\n\n\t\t\t\tPočítač vyhrál!\t\t\t\t\n\n")
	elif vyhra_pc<vyhra:
	
		print(f"Celkové skóre je: {vyhra} Ty a {vyhra_pc} Počítač \n\n \t\tVýsledek je:\n\n\t\t\t\tVyhrál jsi!\t\t\t\t\n\n")	
	else:
		print(f"Celkové skóre je: {vyhra} Ty a {vyhra_pc} Počítač \n\n \t\tVýsledek je:\n\n\t\t\t\tREMÍZA!\t\t\t\t\n\n")
if vyber_hru == "2":
	print("Vybrali jste si Normální verzi:\n")
	for cislo in range(3):
		seznam=["1","2","3","4","5"]
		tah_ui= random.choice(seznam)
		muj_tah= input ("Zadej svuj výběr(číslo): Kámen(1),Nůžky(2),Papír(3),Tapír(4),Spock(5)\n")
		#Muj tah
		if muj_tah == "1":
			muj_tah = "Kámen"
			print("Vybral sis Kámen\n")
		if muj_tah == "2":
			muj_tah = "Nůžky"
			print("Vybral sis Nůžky\n")
		if muj_tah == "3":
			muj_tah = "Papír"
			print("Vybral sis Papír\n")	
		if muj_tah == "4":
			muj_tah = "Tapír"
			print("Vybral sis Tapír\n")	
		if muj_tah == "5":
			muj_tah = "Spock"
			print("Vybral sis Spocka\n")	

		# Tah CPU
		if tah_ui== "1" :
			tah_ui = "Kámen"
			print("PC si vybral Kámen\n")
		if tah_ui == "2":
			tah_ui = "Nůžky"
			print("PC si vybral Nůžky\n")
		if tah_ui == "3":
			tah_ui = "Papír"
			print("PC si vybral Papír\n")
		if tah_ui == "4":
			tah_ui = "Tapír"
			print("PC si vybral Tapír\n")
		if tah_ui == "5":
			tah_ui =  "Spock"
			print("PC si vybral Spocka\n")	
	
	
		#Vyhodnocení hry

		if muj_tah == tah_ui:
			print("Remíza")
			time.sleep(1)
		elif ((muj_tah == "Papír") and (tah_ui == "Kámen") or (muj_tah == "Nůžky") and (tah_ui == "Papír") or (muj_tah == "Kámen") and (tah_ui == "Nůžky") or (muj_tah == "Kámen") and (tah_ui == "Tapír") or (muj_tah == "Tapír") and (tah_ui == "Spock") or (muj_tah == "Spock") and (tah_ui == "Nůžky") or (muj_tah == "Nůžky") and (tah_ui == "Tapír") or (muj_tah == "Tapír") and (tah_ui == "Papír") or (muj_tah == "Papír") and (tah_ui == "Spock") or (muj_tah == "Spock") and (tah_ui == "Kámen")):
			print("Vyhrál jsi!\n\n")
			vyhra+=1
			time.sleep(1)
		else:
			print("Prohrál jsi!\n\n")
			vyhra_pc +=1
			time.sleep(1)
	if vyhra_pc>vyhra :
	
		print(f"Celkové skóre je: {vyhra} Ty \t\t {vyhra_pc} Počítač \n\n \t\tVýsledek je:\n\n\t\t\t\tPočítač vyhrál!\t\t\t\t\n\n")
	elif vyhra_pc<vyhra:
	
		print(f"Celkové skóre je: {vyhra} Ty \t\t {vyhra_pc} Počítač \n\n \t\tVýsledek je:\n\n\t\t\t\tVyhrál jsi!\t\t\t\t\n\n")	
	else:
		print(f"Celkové skóre je: {vyhra} Ty \t\t {vyhra_pc} Počítač \n\n \t\tVýsledek je:\n\n\t\t\t\tREMÍZA!\t\t\t\t\n\n")
