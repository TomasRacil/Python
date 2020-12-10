from ..postavy import Postavy

class NPC(Postavy):
	def __init__(self, jmeno, status):
		super().__init__(jmeno)
		self.status= status
	def getInfo(self):
		print(self.status,self.jmeno)