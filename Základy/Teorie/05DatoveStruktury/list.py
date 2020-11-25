#Seznam se kterým budeme pracovat
jazyky = ['python', 'C++', 'C#', 'Java', 'Kotlin', 'TypeScript',['C', 'Basic'],66]



#Přístup k jednotlivým prvkům je prováděn přes indexy. Index prvního prvku je vždy nula.
print(f"Prvek s nultým indexem: {jazyky[0]}\n")

#Při použití záporných indexů přistupujeme k prvkům v opačném pořadí tedy od konce.
print(f"Poslední prvek: {jazyky[-1]}\n")

#Při použití [index:index] tvoříme podmnožinu seznamu v rozsahu těchto dvou indexů. Takzvaný slicing.
print(f"Druhý až pátý prvek: {jazyky[2:5]}\n")

#Při použití [:index] nebo [index:] vytváříme podmnožinu všech prvků z leva po index, nebo z prava po index
print(f"Všechny prvky od druhého prvku: {jazyky[:2]}\n")

#Přistup k prvkům vnořeného seznamu je prováděn kombinací indexu vnořeného seznamu, a indexu prvku uvnitř vnořeného seznamu.
print(f"Poslední prvek vnořeného seznamu: {jazyky[-2][-1]}\n")



#Změna hodnoty
jazyky[0]='Python'
print(f"Změněný první prvek: {jazyky}\n")

#Přidávání prvků
jazyky.append("Go")
print(f"Přidán nový prvek: {jazyky}\n")

#Rozšíření seznamu a monžinu prvků (jiným seznamem) 
jazyky.extend(['Swift','NodeJS'])
print(f"Seznam rozšířen o dva prvky: {jazyky}\n")

#Pro rozšírení je také možné použít operátor + a přiřazení
jazyky=jazyky+['HTML','CSS']
print(f"Seznam rozšířen o dva prvky pomocí operátor: {jazyky}\n")

#Pro vložení prvku do seznamu používáme metodu insert(index,hodnota), které přijímá dva argumenty index, kam má být prvkek vložen, a prvek samotný.
jazyky.insert(2,"F#")
print(f"Na druhý index seznamu byl vložen F#: {jazyky}\n")

#Odstranění konkrétního prvku můžeme použít remove(hodnota), do kterého předáme hodnotu prvku k odstranění. První prvek se stejnou hodnotou je odstraněn.
jazyky.remove(['C', 'Basic'])
print(f"Vložený seznam odstraněn: {jazyky}\n")

#pro odstranění také můžeme použít výraz del následovaný prvkem k odstranění
del jazyky[-6]
print(f"Prvek s indexem -6 odstraněn: {jazyky}\n")

#Nebo pop(index) který odstraní prvek s patřičným indexem a vrátí jeho hodnotu. Pokud není uveden index odstraní poslední prvek.
print(f"Odstraněný prvek: {jazyky.pop(2)}\n")



#Hledání indexu prvku metodou index() 
print(f"Index prvku Java: {jazyky.index('Java')}\n")

#Pro zjištění počtu prvků v listu používáme metodu count
print(f"Počet prvků Python: {jazyky.count('Python')}\n")



#Pro seřazení seznamu se používá metoda sort(key,reverese). Pokud není zadána žádná hdnota sezname se seřadí defaultním způsobem.
jazyky.sort()
print(f"Seřazený seznam: {jazyky}\n")

#Pro převrácení pořadí se používá metoda revese()
jazyky.reverse()
print(f"Obrácené pořadi: {jazyky}\n")



#Seznam je možné procházet za použití kombinace cyklu for a operátoru in
print("Procházení seznamem pomocí for loop")
for jazyk in jazyky:
	print(jazyk)



#List comprehension - je velice specifická schopnost pythonu umožňuje generovat seznam v rámci deklarace a to buď z jiného seznamu nebo z nějakých pravidel
#způsob zápisu 
#výstupní hodnota for člen iterované datové struktury in datová struktura if podmínka výstupu pokud je třeba

#výstup z jiného listu
maleJazyky= [jazyk.lower() for jazyk in jazyky]
print(f"\nJazyky malými písmeny: {maleJazyky}\n")

#generování nového listu pomocí range
sudaCisla= [str(cislo) for cislo in range(20) if cislo%2==0]
print(f"Suda cisla: {sudaCisla}\n")

#Pro vytvoření kopie listu musíme použít metodu copy() operátor = vytvoří pouze referenci
kopieJazyku=jazyky.copy()
print(f"Suda cisla: {kopieJazyku}\n")