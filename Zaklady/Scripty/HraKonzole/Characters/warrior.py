from .character import *

class warrior(character):
	def __init__(self,hp=120,energy=60,lvl=1,xp=0,damage=90):
		self.type=1
		self.hp=hp
		self.energy=energy
		self.lvl=lvl
		self.xp=xp
		self.damage=damage

	def sleep(self):  
		hod=hodKostkou(1,8)
		print("\nHodil jsi: " + str(hod) + "\n")   

		if hod==1:
			print("Během spánku jsi byl přepaden. \nNezískal jsi žádnou energii")

		elif hod==2:
			print("Sotva jsi zamhouřil oči, okolní rámus tvému spánku rozhodně nedopřál!\nZískáváš 30 energie")
			self.energy=30
		elif hod==3:
			print("V průběhu spánku ses několikrát probudil kvůli nočním můrám !\nZískáváš 60 energie")
			self.energy=60

		elif hod==4 or hod==5:
			print("Po několika hodinách se probouzíš, ale spaní na tvrdé podložce nebylo to pravé!\nZískáváš 90 energie")
			self.energy=90

		elif hod==6:
			print("Bylo ti nabídnuto lůžko v blízkém hostinci, takhle dobře ses už dlouho nevyspal!\nZískáváš 120 energie")
			self.energy=120

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

	def train(self):
		hod=hodKostkou(1,6)
		print("\nHodil jsi: " + str(hod) + "\n")   

		if hod == 1:
			print("Promrhal si celý den. Nechtěl jsi náhodou trénovat?\nZískáváš 0 xp.")

		elif hod == 2:
			print("Zkusil sis rychle zacvičit. A stejně rychle tě to přešlo.\nZískáváš 10 xp.")
			self.xp = xp + 10

		elif hod == 3 or hod == 4:
			print("Přečetl jsi půlku manuálu pro dobrodruhy.\nZískáváš 30 xp.")
			self.xp= xp + 30

		elif hod == 5:
			print("Přemluvil jsi náhodného kolemjdoucího na sparring. Snad to ještě někdy rozchodí...\nZískáváš 60 xp.")
			self.xp = xp + 60

		elif hod == 6:
			print("DING!\nZískáváš level.")
			self.lvl = lvl + 1