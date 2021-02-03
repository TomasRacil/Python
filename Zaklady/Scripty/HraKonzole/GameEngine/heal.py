from GameEngine import *

def heal(self):
		hod=hodKostkou(1,8)
		print("\nHodil jsi: " + str(hod) + "\n")   

		if hod==1:
			print("Spletl jsi si lektvary. \nZtrácíš 20 hp.")
			self.hp=hp-20 

		elif hod==2:
			print("Jsi neohrabaný a lektvar jsi rozlil na zem.")
				
		elif hod==3 or hod==5:
			print("Bohužel lektvar byl prošlý.\nZískáváš 40 hp.")
			self.hp=hp+40

		elif hod==4 or hod==6:
			print("Všechny tvé válečné rány se zahojily!\nZískáváš 95 hp.")
			self.hp=hp+95
