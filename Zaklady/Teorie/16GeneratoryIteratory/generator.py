"""
Python poskytuje jednu velice užitečnou schopnost a tou je vytvářet vlastních generátorů posloupnosti.
Tyto generátory nám umožňují vytvořit posloupnosti a přistupovat k nim prvek po prvku, nebo je využít v rámci cyklů.
Genrátory jsou velice jsdnoduché na implementaci v různých situacích, efektivně pracují s pamětí systému 
a jsou výborné pro vytváření nekončných posloupností (správně využité chrání proti nekonečným cyklům)
"""


#Vytvoření jednoduchého generátoru
def prvniGenerator():
	"""Tento generátor tiskne tři řetězce"""
	n = 1
	print('První vytištěný string')
	# V rámci generátorů využíváme funkce yield pro vyolání odpovědi
	yield n

	n += 1
	print('Druhý vytištěný string')
	yield n

	n += 1
	print('Třetí vytištěný string')
	yield n



#vytvoříme instanci našeho generátoru
instancePrvnihoGeneratoru = prvniGenerator()

print("První prvek:")
#k prvkům generátoru přistupujeme postupne zavoláním funkce next
next(instancePrvnihoGeneratoru)

print("Druhý prvek:")
next(instancePrvnihoGeneratoru)

print("Třetí prvek:")
next(instancePrvnihoGeneratoru)

print("Čtvrtý prvek:")
#Jak je možné vidět na dalším řádků pokus o získání čtrvtého prvku vyvolá vyjímku StopIteration
try:
	next(instancePrvnihoGeneratoru)
except Exception as e:
	print(f"Vzniklá vyjímka {e}")
print("")



instancePrvnihoGeneratoru2=prvniGenerator()

print("Použití cyklu pro procházení prvků generátoru")
#K generátorům také můžeme přistupovat pomcí cyklu
for n in instancePrvnihoGeneratoru2:
	#Výstup jak můžeme vidět se skládá z print() zavolanáho v rámci generátoru
	#a hodnoty n, která je v rámci generátoru navyšována
	print(n)



#V rámci generátorů samozřejmě můžeme použít i cykly
def reverzniGen(retezec):
	"""Reverzní generátor

	Generuje obrácený řetězec tomu, který byl předán v argumentu.
	"""
	for pismeno in range(len(retezec) - 1, -1, -1):
		yield retezec[pismeno]

print("")



obracene=""
#Cyklus pro vyvolání generátoru a přidání znaku k retezci obracene
for znak in reverzniGen("Jak se máš"):
	obracene+=znak

print(f"Obrácený řetězec: {obracene}\n")


#Generátory také můžeme vytvářet jednoduše na řádku pomocí kulatých závorek
#syntaxe je následovná: (operace for prvek in rozsah)
#	operace může být zcela libivolná včetně volání funkcí například
#	prvek je jedním z prvků iterátoru za klíčovým slovem in (iterátory jsou všechny datové struktury, nebo i jiné generátory)
generator = (x**2 for x in range(0,10,2))

#Můžeme zde vidět že generator je objekt typy genexpr
print(f"O jakou třídu se jedná? {generator}")
print(f"První prvek genratoru: {next(generator)}")
print(f"Druhý prvek genratoru: {next(generator)}")
print(f"atd..\n")

#Na závěr ukázka několika generátorů pro spočítání průměrné hodnoty čísel fibonciho posloupnosti na druhou
def fibonacihoPsoloupnostGen(cisla):
	"""Generátor fibonaciho posloupnosti"""
	x, y = 0, 1

	# _ potžítko využíváme v situaci kdy nepotřebujeme využívat prvku cyklu(čísla vyjadřujícího o kolikáté opakován cyklu se jedná)
	for _ in range(cisla):
		x, y = y, x+y
		yield x

def naDruhouGen(cisla):
	"""Generátor provádějící mocnění na druhou"""
	for cislo in cisla:
		yield cislo**2

print(f"Průměrná hodnota druhé mocniny fibonaciho posloupnosti s desti čísly: {sum(naDruhouGen(fibonacihoPsoloupnostGen(10)))/10}")