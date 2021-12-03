"""
Ve většíně programovacích jazyků existují takzvané modifikátory přístupu.
Ty ovlivňují odkud je prvek přístupný popřípadně jestli je nebo není možné ho dědit.
Obecně existují tři základní public, protected a private.
Ovšem v jazyk python nic takového neumožňuj a všechny prvky jsou tedy veřejné.
Jako kompenzace byly vytvořeny obecná pravidla toho jak označovat prvky, které mají být chráněné,
a je pak na ostatních programátorech aby tyto pravidla dodržovali.
"""
#Public je volně přístupný prvek. Může být děděn a také k němu může být volně přistupováno. 
class Zvire: 
	def __init__(self, jmeno, vek): 	 
		self.jmeno = jmeno 
		self.vek = vek 

	def jmenoVek(self):
		print(f"{Zvire.__name__} Metoda: \n\tJméno: {obj.jmeno}; věk: {obj.vek}\n")

obj = Zvire("Damian", 10)

#Přímý přístup k objektům objekt.vlastnost
print(f"{Zvire.__name__} Jméno : {obj.jmeno}; věk: {obj.vek}")

#Přímý přístup k metodám
obj.jmenoVek()

#Protected je přístupý pouze třídám, které jsou jeho potomky. Označujeme pomocí jednoho podtržítka.
class Osoba:
	#portected prměnné
	_jmeno = None
	_vek = None
	def __init__(self, jmeno, vek): 	  
		self._jmeno = jmeno 
		self._vek = vek
	#protected metoda
	def _jmenoVek(self):
		print(f"{Osoba.__name__} Metoda: \n\tJméno: {obj._jmeno}; \n\tvěk: {obj._vek}")

class Vojak(Osoba):
	def __init__(self, jmeno, vek, hodnost): 	  
		self._jmeno = jmeno 
		self._vek = vek
		self.hodnost = hodnost

	#metoda která je veřejná a je možnost k ní přistupovat mimo třídu
	def info(self):
		#volání chráněné metody
		self._jmenoVek()
		print(f"\thodnost: {self.hodnost}")

obj = Vojak("Vrana",20,"desatnik") 

obj.info()

#objekt.vlatnost je monžné použít pro přístup k protected prvkům
#ale jedná se o porušení pravidel


#Private prvek je přístupný jen v rámci třídy. Označujeme pomocí dvou podtržítek.
class Droid: 
	 
	# private třídy
	__jmeno = None
	__typ = None

	def __init__(self, jmeno, typ):   
		self.__jmeno = jmeno 
		self.__typ = typ 
  
	# private metoda  
	def __info(self): 
			
		# přístup k private prvkům uvnitř třídy
		print(f"\n{Droid.__name__} Metoda: \n\tJméno: {self.__jmeno}; \n\ttyp: {self.__typ}")
	 
	#public metoda přistupující k private metodě v rámci třídy
	def zavolejPrivateMetodu(self):   
		self.__info()   

obj = Droid("R2D2", "Astromech") 

#volání veřejné metody pro přístup k private prvkům
obj.zavolejPrivateMetodu() 

#objekt.vlatnost je monžné použít pro přístup k private prvkům
#ale jedná se o porušení pravidel


#řešením je property dekorátor
class Budova:
	def __init__(self,cisloPopisne: int, typ: str):
		self._cisloPopisne=cisloPopisne
		self._typ=typ
	
	@property
	def cisloPopisne(self):
		return self._cisloPopisne
	
	@cisloPopisne.setter
	def cisloPopisne(self, cisloPopisne: int):
		if cisloPopisne>1000: print("error")
		else:self.__cisloPopisne=cisloPopisne

	@property
	def typ(self):
		return self.__typ
	
	@typ.setter
	def typ(self, typ: str):
		self.__typ=typ

mujByt=Budova(618,"dum")

mujByt.cisloPopisne

print(f"pristup pres property {mujByt.cisloPopisne}")
mujByt.cisloPopisne=int(input("zadej cislo popisne"))
print(mujByt.cisloPopisne)