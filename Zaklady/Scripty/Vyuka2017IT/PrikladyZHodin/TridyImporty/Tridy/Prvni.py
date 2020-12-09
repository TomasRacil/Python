class Prvni:
	"""První třída"""
	#arg="def"
	def __init__(self, *args,**kwargs):
		self.kwargs = kwargs
		self.args = args
	def getValues(self):
		return self.kwargs,self.args

def ukazkovaFunkce():
	"""Ukázková funkce"""
	print("test")
