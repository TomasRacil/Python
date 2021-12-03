"""
Python defaulně nepodporuje přepínače, ale existuje cesta jak tuto fonkčnost zajistit.
Abychom tuto funčnost zajistili vytvoříme vlastní funkci, která přepínač nahradí.
Obecně se však, ale nedoporučuje přepínače vytvářet, ovšem určitě se najdou problémy,
pro které bude přepínač ideálním řešením.
"""

def ahojSvete():
  """Funkce tisknoucí ahoj světe"""
  print("Ahoj svete")

def funkcePrepinace(cislo):
  """Funkce sloužící jako přepínač

	Args:
		cislo (int): zvolené číslo

	Returns:
		string: vrací číslo předané v argumentu jako string 
  """

	#Datový typ slovnik, který skladuje všechny možnosti a hodnoty které mají být vráceny přepínačem
  prepinac = { 
      0: "nula", 
      1: "jedna", 
      2: "dva",
      "Ahoj": ahojSvete #Tímto způsobem můžeme předávat i funkce. Více o této možnosti v pythonu v kapitole dekorátory.
  } 
	#Získání hodnoty na kterou odkazuje argument. Metoda get(klíč, defaultní hodnota), 
	#příjíma dva parametry klíč odkazující na prvek v slovníku a defaultní hodnotu, 
	#která je vrácena pokud prvek s daným klíčem neexistuje
  return prepinac.get(cislo, "nic") 
  

print(f"Hodnota jedna předána přepínači: {funkcePrepinace(1)}\n")
print(f"Nedefinovaná hodnota předána přepínači: {funkcePrepinace(10)}\n")

print("Volání funkce získané z přepínače")
#Ukázka způsobu zavolání fuknce vrácené přepínačem.
funkcePrepinace("Ahoj")()