#ukázkový set
#Sety nemohou obsahovat jednu hodnotu více jak dvakrát
zelenina={"paprika","rajče", "cuketa","cuketa"}

#Prvky které se opakují jsou ignorovány
#Set nemá dané pořadí
print(f"Cvicny set: {zelenina}\n")



#Kopii setu vytvoříme pomocí metody copy()
kopieZeleniny=zelenina.copy()

#Procházení setu pomocí cyklu for
print("Jednotlivé prvky cvičného setu:\n")
for prvek in zelenina:
	print(prvek)



#Přidání prvku provádíme pomocí metody add(prvek)
zelenina.add("jablko")
print(f"\nZelenina + jablko: {zelenina}\n")


#Pro přidání prvků jiné datové struktury používáme metodu update(datová struktura)
tykvovité={'meloun','tykev'}
zelenina.update(tykvovité)
print(f"Zelenia včetně tykví: {zelenina}\n")

korenovaZelenina=['celér', 'petržel','mrkev']
zelenina.update(korenovaZelenina)
print(f"Cvicny včetně kořenové zeleniny: {zelenina}\n")



#Pro odstranění prvku používáme metodu remove('hodnota prvku')
zelenina.remove("jablko")
print(f"Zelenia bez jablka: {zelenina}\n")

#Pro odstranění prvku používáme metodu discard('hodnota prvku'), která nehlásí chybu pokud již prvek neexistuje
zelenina.discard("jablko")

#Metoda pop() odstraní poslední přidaný prvek
zelenina.pop()
print(f"Zelenia bez posledně přidaného prvku: {zelenina}\n")



#Pro propojení dvou setů můžeme také použít metody union(),intersection(),symmetric_difference()
#union(druhý set) vrací nový set který obsahuje prvky obou setu
unionSet=zelenina.union(korenovaZelenina)
print(f"Spojení setů:")
print(f"kopie zelenina: {kopieZeleniny}")
print(f"a kořenová zelenina: {korenovaZelenina}")
print(f"je: {unionSet}\n")

#intersection(druhý set) vrací set prvků které se nacházejí v obou setech
intersectionSet=zelenina.intersection(korenovaZelenina)
print(f"Průnik setů:")
print(f"zelenina: {zelenina}")
print(f"a kořenová zelenina: {korenovaZelenina}")
print(f"je: {intersectionSet}\n")

#symmetric_difference(druhý set) vrací set prvků které se nenacházejí v obou setech
differenceSet=zelenina.symmetric_difference(korenovaZelenina)
print(f"Rozdíl setů:")
print(f"zelenina: {zelenina}")
print(f"a kořenová zelenina: {korenovaZelenina}")
print(f"je: {differenceSet}\n")



#Pro smazání obsahu celého setu můžeme použít metodu clear()
zelenina.clear()
print(f"Prázdný seznam: {zelenina}\n")

#Odstranění setu můžeme provést výrazem del
del zelenina
print(f"Existuje set zelenina: {'zelenina' in vars() or 'zelenina' in globals()}\n")