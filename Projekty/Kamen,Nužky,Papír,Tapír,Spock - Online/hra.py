from random import *
class Hra:
	def __init__(self,id):
		self.p1Went = False
		self.p2Went = False
		self.ready = False
		self.id= id  #každá hra bude mít svou ID
		self.tahy = [None, None] #dvě pozice tahá které budeme měnit
		self.vyhra = [0,0]
		self.ties = 0

	def dostan_tah_hrace(self,p):
		return self.tahy[p]


	

	def hrat(self,hrac,tah):
		self.tahy[hrac] = tah
		if hrac == 0:
			self.p1Went = True #změní z false na true jelikož odehrál
		else:
			self.p2Went = True #pokud neodehrál hráč 1 musel hráč 2
	#hlídá jestli jsou připojeni dva hráči a potom jim to umožní hrát
	def pripojeni(self):
		return self.ready
	# jestli oba odešli 
	def obaWent(self):
		return self.p1Went and self.p2Went
	def vitez(self):

		p1 = self.tahy[0].upper()[0] #vezme do porovnání pouze první písmeno slova hráče1
		p2 = self.tahy[1].upper()[0] #vezme do porovnání pouze první písmeno slova hráče2

		vitez = -1 #protože může být remíza 0(výhra hráč1),1(výhra hráč2)
		if p1 == "K" and p2 == "N":
			vitez = 0
		elif p1 == "N" and p2 == "K":
			vitez = 1
		elif p1 == "P" and p2 == "K":
			vitez = 0
		elif p1 == "K" and p2 == "P":
			vitez = 1
		elif p1 == "N" and p2 == "P":
			vitez = 0
		elif p1 == "P" and p2 == "N":
			vitez = 1
		elif p1 == "T" and p2 == "K":
			vitez = 1
		elif p1 == "K" and p2 == "T":
			vitez = 0
		elif p1 == "T" and p2 == "S":
			vitez = 0
		elif p1 == "S" and p2 == "T":
			vitez = 1
		elif p1 == "S" and p2 == "N":
			vitez = 0
		elif p1 == "N" and p2 == "S":
			vitez = 1
		elif p1 == "N" and p2 == "T":
			vitez = 0
		elif p1 == "T" and p2 == "N":
			vitez = 1
		elif p1 == "P" and p2 == "T":
			vitez = 1
		elif p1 == "T" and p2 == "P":
			vitez = 0
		elif p1 == "S" and p2 == "P":
			vitez = 1
		elif p1 == "P" and p2 == "S":
			vitez = 0
		elif p1 == "S" and p2 == "K":
			vitez = 0
		elif p1 == "K" and p2 == "S":
			vitez = 1

		return vitez

	def resetWent(self):
		self.p1Went = False
		self.p2Went = False