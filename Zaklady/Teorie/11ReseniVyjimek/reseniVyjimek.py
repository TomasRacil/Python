"""
Řešení vyjímek je v pythonu velice důležité, jako v každém interpretovaném jazyku, protože k nim často dochází.
 Narozdíl od jazyků kompilovaných neprochází kód žádnou kontrolou před spuštěním a je místotoho vyhodnocován řádek po řádku. 
 Dochází tak často k tomu, že nastane problém v nějaké drobnosti a celý program je kvůli tomu ukončen.
Pro obsloužení potenciální chyb se používají dvě klíčová slova try a except. Pro definování jednotlivých bloků kódu používáme odsazení.
"""
try:
	10/0
except:
	print("Dělení nulou není možné")

#můžeme také získat konkrétní vyvolanou chybu aniž by byl program zastaven
try: 
	10/0
except Exception as e: #keyword as slouží k přiřazen aliasu. Tedy proměná e bude zastupovat proměnnou Exception.
	print(e)
	
#Je možné také definovat jednotlivé reakce programu v závislosti na vyvolané chybě
try:
	int('xyz')
	#10/0
	#'2'+2
	#print(vek)
except ValueError:
	print("ValueError")

except (TypeError, ZeroDivisionError):
	print("TypeError or ZeroDivisionError")

except:
   	print("Ostatní chyby")
#Je také možné vyjímku vyvolat za použití raise následovaného chybovou třídou.
#raise KeyboardInterrupt

#try je možné kombinovat s else pr zajištění správného chodu programu
try:
    cislo = int(input("Napiš číslo: "))
    assert cislo % 2 == 0 #assert zkusí jestli je podmínka pravdivá pokud ne vrátí AssertionError
except AssertionError:
    print("Nejedná se o sudé číslo")
except ValueError:
	print("Nejedná se o číslo")
except Exception as e:
	print(e)
else:
    podil = 1/cislo
    print(podil)

#Slovo final je možné také použít v kobinaci s try a exception. Blok kódu uvedený za final se vždy provede.
# try:
# 	raise KeyboardInterrupt
# finally:
# 	print('Konec lekce')
	
class CustomException(Exception):
	def __init__(self, message="message from custom exception"):
		self.message=message
		super().__init__(self.message)


try:
	#some code
	raise CustomException
except CustomException as e:
	print(e)
