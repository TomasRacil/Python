ukazkovyList = ['první prvek', 'druhý prvek', '...']
print(f'obsah listu: {ukazkovyList} a typ {type(ukazkovyList)}\n')

ukazkovyTuple = ('první prvek', 'druhý prvek', '...')
print(f'obsah tuple: {ukazkovyTuple} a typ {type(ukazkovyTuple)}\n')

ukazkovySet = {'první prvek', 'druhý prvek', '...'}
print(f'obsah setu: {ukazkovySet} a typ {type(ukazkovySet)}\n')

ukazkovyDict = {'Jmeno': 'Tomáš', 'Prijmeni': 'Ráčil', 'Další': '...'}
print(f'obsah slovníku: {ukazkovyDict} a typ {type(ukazkovyDict)}\n')

jazyky = ['python', 'C++', 'C#', 'Java', 'Kotlin', 'TypeScript', ['C', 'Basic'], 66]

print(f"Prvek s nultým indexem: {jazyky[0]}\n")
print(f"Poslední prvek: {jazyky[-1]}\n")
print(f"Druhý až pátý prvek: {jazyky[2:5]}\n")
print(f"Poslední prvek vnořeného seznamu: {jazyky[-2][-1]}\n")

jazyky[0] = 'Python'
print(f"Změněný první prvek: {jazyky[0]}\n")

jazyky.append("Go")
print(f"Přidán nový prvek: {jazyky}\n")

jazyky.extend(['Swift', 'NodeJS'])
print(f"Seznam rozšířen o dva prvky: {jazyky}\n")

jazyky = jazyky + ['HTML', 'CSS']
print(f"Seznam rozšířen o dva prvky pomocí operátor: {jazyky}\n")

jazyky.insert(2, "F#")
print(f"Na druhý index seznamu byl vložen F#: {jazyky}\n")

jazyky.remove(['C', 'Basic'])
print(f"Vložený seznam odstraněn: {jazyky}\n")

del jazyky[-6]
print(f"Prvek s indexem -6 odstraněn: {jazyky}\n")

print(f"Odstraněný prvek: {jazyky.pop(2)}\n")

print(f"Index prvku Java: {jazyky.index('Java')}\n")
print(f"Počet prvků Python: {jazyky.count('Python')}\n")

jazyky.sort()
print(f"Seřazený seznam: {jazyky}\n")

jazyky.reverse()
print(f"Obrácené pořadí: {jazyky}\n")

print("Procházení seznamem pomocí for loop")
for jazyk in jazyky:
    print(jazyk)

kopieJazyku = jazyky.copy()
print(f"Kopie jazyku: {kopieJazyku}\n")

maleJazyky = [jazyk.lower() for jazyk in jazyky]
print(f"\nJazyky malými písmeny: {maleJazyky}\n")

sudaCisla = [str(cislo) for cislo in range(20) if cislo % 2 == 0]
print(f"Suda cisla: {sudaCisla}\n")

jazyky.clear()
print(f"Prázdný seznam: {jazyky}\n")

del jazyky
print(f"Existuje seznam jazyky: {'jazyky' in vars() or 'jazyky' in globals()}\n")

petice = ('první prvek', 2, ['prvni prvek listu', 2], 2, 'poslední prvek')

print(f"První prvek: {petice[1]}\n")
print(f"Poslední prvek: {petice[-1]}\n")
print(f"Třetí až předposlední prvek: {petice[3:-2]}\n")
print(f"Všechny prvky od druhého prvku: {petice[:2]}\n")
print(f"Poslední prvek vnořeného seznamu: {petice[2][-1]}\n")

print(f"Původní n-tice: {petice}\n")
seznam = list(petice)
seznam[2] = 'změněný prvek'
petice = tuple(seznam)
print(f"Změněná n-tice: {petice}\n")

(prvni, druhy, treti, ctvrty, paty) = petice
print(f"Prvnky n-tice jako proměnné:")
print(prvni, type(prvni), druhy, type(druhy), treti, type(treti), ctvrty, type(ctvrty), paty, type(paty), '\n')

print(f"Procházení n-tice:")
for prvek in petice:
    print(prvek)

print(f"\nIndex změněného prvku: {petice.index('změněný prvek')}\n")
print(f"Počet dvojek: {petice.count(2)}\n")

del petice
print(f"Existuje n-tice petice: {'petice' in vars() or 'petice' in globals()}\n")

zelenina = {"paprika", "rajče", "cuketa", "cuketa"}
print(f"Cvicny set: {zelenina}\n")

kopieZeleniny = zelenina.copy()

print("Jednotlivé prvky cvičného setu:\n")
for prvek in zelenina:
    print(prvek)

zelenina.add("jablko")
print(f"\nZelenina + jablko: {zelenina}\n")

tykvovité = {'meloun', 'tykev'}
zelenina.update(tykvovité)
print(f"Zelenia včetně tykví: {zelenina}\n")

korenovaZelenina = ['celér', 'petržel', 'mrkev']
zelenina.update(korenovaZelenina)
print(f"Cvicny včetně kořenové zeleniny: {zelenina}\n")

zelenina.remove("jablko")
print(f"Zelenia bez jablka: {zelenina}\n")

zelenina.discard("jablko")

zelenina.pop()
print(f"Zelenia bez posledně přidaného prvku: {zelenina}\n")

unionSet = zelenina.union(korenovaZelenina)
print(f"Spojení setů:")
print(f"kopie zelenina: {kopieZeleniny}")
print(f"a kořenová zelenina: {korenovaZelenina}")
print(f"je: {unionSet}\n")

intersectionSet = zelenina.intersection(korenovaZelenina)
print(f"Průnik setů:")
print(f"zelenina: {zelenina}")
print(f"a kořenová zelenina: {korenovaZelenina}")
print(f"je: {intersectionSet}\n")

differenceSet = zelenina.symmetric_difference(korenovaZelenina)
print(f"Rozdíl setů:")
print(f"zelenina: {zelenina}")
print(f"a kořenová zelenina: {korenovaZelenina}")
print(f"je: {differenceSet}\n")

studenti = {
    1: {
        "Jméno": "Josef",
        "Příjmení": "Kolík"
    },
    2: {
        "Jméno": "David",
        "Příjmení": "Ryba"
    },
    3: {
        "Jméno": "Ladislav",
        "Příjmení": "Valda"
    }
}

print(f"První student: {studenti[1]}")
print(f"Jméno druhého studenta: {studenti[2]['Jméno']}\n")

studenti['novýKlíč'] = 'nová hodnota'
print(f"Slovník s novou hodnotou: {studenti}\n")

studenti['novýKlíč'] = 'změněná hodnota'
print(f"Slovník se změněnou hodnotou: {studenti}\n")

studenti.update({'dalšíKlíč': 'další nová hodnota'})
print(f"Slovník se další novou hodnotou: {studenti}\n")

studenti.pop('novýKlíč')
print(f"Slovník s odstraněným klíčem: {studenti}\n")

studenti.popitem()
print(f"Slovník s odstraněným posledním klíčem: {studenti}\n")

print(f"Klíče slovníku: {studenti.keys()}\n")
print(f"Hodnoty slovníku: {studenti.values()}\n")
print(f"Dvojice hodnota klíč: {studenti.items()}\n")

print(f"Je novýKlíč v listu: {'novýKlíč' in studenti}\n")

print("Klíče slovníku:")
for klic in studenti:
    print(klic)

print("\nHodnoty slovníku první způsob:")
for klic in studenti:
    print(studenti[klic])

print("\nHodnoty slovníku druhý způsob:")
for hodnota in studenti.values():
    print(hodnota)

print("\nKlíč hodnota:")
for klic, hodnota in studenti.items():
    print(klic, hodnota)

studentiKopie = studenti.copy()
print(f"Kopie slovníku: {studentiKopie}\n") 

studenti.clear()
print(f"Prázdný slovník: {studenti}\n")

del studenti
print(f"Existuje slovník studenti: {'studenti' in vars() or 'studenti' in globals()}\n")