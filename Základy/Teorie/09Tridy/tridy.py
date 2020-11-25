"""
Python je objektově orientovaný jazyk. Toho už jsme si mohly všimnout u proměných a datových typů.
Tato částs má zaúkol vysvětlit základní principy psaní tříd v jazyce python.
"""

#základní třídu definujeme pomocí výrazu class, který je následován jménem třídy
#na dalších řádcích pak odsazený obsah třídy (atributy a metody)
class UkazkovaTrida:
	"""Ukázková třida ..."""
	x=5 #zde jsme definovali atribut x který má defaultní hodnotu 5

instanceUkazkoveTridy=UkazkovaTrida() 	#stojí za povšimnutí, že jsme nemuseli definovat konstruktor, python si totiž sám vytvoří defaultní konstruktor
print(instanceUkazkoveTridy.x)			#vytiskneme hodnotu atributu x

instanceUkazkoveTridy.x=4				#vzhledem k tomu že atribut není nijak chráněný můžeme ho přímo změnit přiřazením jiné hodnoty
print(instanceUkazkoveTridy.x)			


#Často budeme potřebovat upravit konstruktor. V takovém případě sami definujeme metodu s jménem __init__ a ta nám poslouží jako konstruktor.
class TridaSKonstruktorem(object):
 	"""Třída s konstruktorem ..."""
 	#metody jsou definovány stejným způsobem jako funkce, tedy výraz def následovaný názvem metody (v případě konstruktoru vždy __init__)
 	#v závorkách pak následují 
 	def __init__(self, arg):				
 		super(ClassName, self).__init__()
 		self.arg = arg
