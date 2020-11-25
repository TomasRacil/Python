"""
Python je objektově orientovaný jazyk. Toho už jsme si mohly všimnout u proměných a datových typů.
Tato částs má zaúkol vysvětlit základní principy psaní tříd v jazyce python.
"""



#základní třídu definujeme pomocí výrazu class, který je následován jménem třídy
#na dalších řádcích pak odsazený obsah třídy (atributy a metody)
class UkazkovaTrida:
	"""Ukázková třida ..."""
	#v rámci třídy můžeme definovat atributy v tomto případe x který má defaultní hodnotu 5
	x=5 

#vytvoření objektu
instanceUkazkoveTridy=UkazkovaTrida() 	
#stojí za povšimnutí, že jsme nemuseli definovat konstruktor, python si ho sám vytvoří

#přímý přistup k parametrům je možný protože nejsou chráněny
#čtení hodnoty
print(f"Výchozí hodnota atributu x {instanceUkazkoveTridy.x}\n")

#zápis hodnoty
instanceUkazkoveTridy.x=4		
print(f"Hodnota atributu x {instanceUkazkoveTridy.x}\n")			



#Často budeme potřebovat upravit konstruktor. V takovém případě sami definujeme metodu s jménem __init__, která slouží jako konstruktor.
class TridaSKonstruktorem:
 	"""Třída s konstruktorem ..."""
 	#metody jsou definovány stejným způsobem jako funkce, tedy výraz def následovaný názvem metody (v případě konstruktoru vždy __init__)
 	#v závorkách pak následují argumety, vždy musí být přítomen alespoň jeden argument (pojmenovávámeho self), který odkazuje na instanci třídy
 	def __init__(self,arg):
 		self.arg=arg			
 		print(f"Objekt inicializován\n")

 	def getValue(self):
 		print(f"Hodnota: {self.arg}\n")

instanceTridySKonstruktorem=TridaSKonstruktorem(5)

#zavolání metody
instanceTridySKonstruktorem.getValue()



