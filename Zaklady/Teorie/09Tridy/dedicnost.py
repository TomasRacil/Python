class Clovek:
	"""Rodičovská třída"""
	def __init__(self, jmeno, prijmeni):
		self.jmeno = jmeno
		self.prijmeni = prijmeni
	def jmenujiSe(self):
		print(f"Jmenuji se {self.jmeno} {self.prijmeni}")

#U třídy, která je potomkem musíme uvést rodičovskou třídu v kulatých závorkách
class Vojak(Clovek):
	"""Třída potomka"""

	#Z rodičovské metody můžeme kompletně zdědit funkce v takovém případě je nijak neuvádíme, zde takto dědíme metodu jmenujiSe()
	#Pokud chceme nějakou metodu upravit vytvoříme metodu se stejným názvem a tím přepíšeme metodu rodičovské třídy, zde uvádím na příkladu init
	def __init__(self, jmeno, prijmeni, hodnost):
		#Pokud chceme využít metody rodičovské třídy můžeme ji zavolat pomocí super(), zde využíváme konstruktoru rodičovské metody
		super().__init__(jmeno, prijmeni)
		#Dále zde rozšíříme konstruktor o přiřazení parametru hodnost
		self.hodnost =hodnost

	#Doplnění třídy o novou metodu 
	def vypisHodnostJmeno(self):
		print(self.hodnost,self.jmeno,self.prijmeni)

x = Clovek("Alda", "Králik")
x.jmenujiSe()

y = Vojak("Zip","Zipser","desátník")
y.jmenujiSe()
y.vypisHodnostJmeno()