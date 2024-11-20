## Datové struktury

Datové struktury slouží k ukládání kolekcí dat. V Pythonu existují čtyři základní typy:

### Seznam (list)

* Umožňuje ukládat **uspořádanou** kolekci prvků **různých typů**, včetně dalších datových struktur.
* Prvky seznamu se mohou **opakovat**.
* Seznam je **modifikovatelný** (mutable) - lze přidávat, odebírat a měnit prvky.
* Deklaruje se pomocí hranatých závorek `[]`.

```python
ukazkovyList = ['první prvek', 'druhý prvek', '...']
print(f'obsah listu: {ukazkovyList} a typ {type(ukazkovyList)}\n')
```

### N-tice (tuple)

* Podobná seznamu, ale je **neměnná** (immutable) - po vytvoření nelze prvky měnit.
* Umožňuje ukládat **uspořádanou** kolekci prvků **různých typů**.
* Prvky n-tice se mohou **opakovat**.
* Deklaruje se pomocí kulatých závorek `()`.

```python
ukazkovyTuple = ('první prvek', 'druhý prvek', '...')
print(f'obsah tuple: {ukazkovyTuple} a typ {type(ukazkovyTuple)}\n')
```

### Množina (set)

* Umožňuje ukládat **neuspořádanou** kolekci **unikátních** prvků.
* Prvky množiny se **nemohou opakovat**.
* Množina je **modifikovatelná** - lze přidávat a odebírat prvky.
* Deklaruje se pomocí složených závorek `{}`.

```python
ukazkovySet = {'první prvek', 'druhý prvek', '...'}
print(f'obsah setu: {ukazkovySet} a typ {type(ukazkovySet)}\n')
```

### Slovník (dictionary)

* Umožňuje ukládat **neuspořádanou** kolekci dvojic **klíč-hodnota**.
* **Klíče** musí být **unikátní** a **neměnné** (immutable).
* **Hodnoty** mohou být libovolného typu.
* Slovník je **modifikovatelný**.
* Deklaruje se pomocí složených závorek `{}` a dvojic klíč-hodnota oddělených dvojtečkou `:`.

```python
ukazkovyDict = {'Jmeno': 'Tomáš', 'Prijmeni': 'Ráčil', 'Další': '...'}
print(f'obsah slovníku: {ukazkovyDict} a typ {type(ukazkovyDict)}\n')
```

## Práce se seznamy (list)

### Přístup k prvkům

* K prvkům seznamu se přistupuje pomocí **indexů**, počínaje od 0.
* Záporné indexy se používají pro přístup od konce seznamu (-1 je poslední prvek).

```python
jazyky = ['python', 'C++', 'C#', 'Java', 'Kotlin', 'TypeScript', ['C', 'Basic'], 66]

print(f"Prvek s nultým indexem: {jazyky[0]}\n")
print(f"Poslední prvek: {jazyky[-1]}\n")
print(f"Druhý až pátý prvek: {jazyky[2:5]}\n")
print(f"Poslední prvek vnořeného seznamu: {jazyky[-2][-1]}\n")
```

### Modifikace seznamu

* `append(prvek)`: Přidá prvek na konec seznamu.
* `extend(iterable)`: Přidá všechny prvky z iterovatelného objektu (např. jiného seznamu) na konec seznamu.
* `insert(index, prvek)`: Vloží prvek na daný index.
* `remove(prvek)`: Odstraní první výskyt prvku.
* `del seznam[index]`: Odstraní prvek na daném indexu.
* `pop(index)`: Odstraní prvek na daném indexu a vrátí jeho hodnotu.

```python
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
```

### Vyhledávání a řazení

* `index(prvek)`: Vrací index prvního výskytu prvku.
* `count(prvek)`: Vrací počet výskytů prvku v seznamu.
* `sort()`: Seřadí seznam.
* `reverse()`: Obrátí pořadí prvků v seznamu.

```python
print(f"Index prvku Java: {jazyky.index('Java')}\n")
print(f"Počet prvků Python: {jazyky.count('Python')}\n")

jazyky.sort()
print(f"Seřazený seznam: {jazyky}\n")

jazyky.reverse()
print(f"Obrácené pořadí: {jazyky}\n")
```

### Iterace a kopírování

* Seznam lze procházet pomocí cyklu `for`.
* `copy()`: Vytvoří kopii seznamu.

```python
print("Procházení seznamem pomocí for loop")
for jazyk in jazyky:
    print(jazyk)

kopieJazyku = jazyky.copy()
print(f"Kopie jazyku: {kopieJazyku}\n")
```

### List comprehension

* Umožňuje vytvářet nové seznamy na základě existujících seznamů a podmínek.

```python
maleJazyky = [jazyk.lower() for jazyk in jazyky]
print(f"\nJazyky malými písmeny: {maleJazyky}\n")

sudaCisla = [str(cislo) for cislo in range(20) if cislo % 2 == 0]
print(f"Suda cisla: {sudaCisla}\n")
```

### Mazání seznamu

* `clear()`: Vymaže všechny prvky seznamu.
* `del seznam`: Odstraní seznam.

```python
jazyky.clear()
print(f"Prázdný seznam: {jazyky}\n")

del jazyky
print(f"Existuje seznam jazyky: {'jazyky' in vars() or 'jazyky' in globals()}\n")
```

## Práce s n-ticemi (tuple)

### Přístup k prvkům

* Stejný jako u seznamů - pomocí indexů.

```python
petice = ('první prvek', 2, ['prvni prvek listu', 2], 2, 'poslední prvek')

print(f"První prvek: {petice[1]}\n")
print(f"Poslední prvek: {petice[-1]}\n")
print(f"Třetí až předposlední prvek: {petice[3:-2]}\n")
print(f"Všechny prvky od druhého prvku: {petice[:2]}\n")
print(f"Poslední prvek vnořeného seznamu: {petice[2][-1]}\n")
```

### Neměnnost

* N-tice nelze po vytvoření modifikovat.
* Pro změnu je nutné ji převést na seznam, provést změny a pak zpět na n-tici.

```python
print(f"Původní n-tice: {petice}\n")
seznam = list(petice)
seznam[2] = 'změněný prvek'
petice = tuple(seznam)
print(f"Změněná n-tice: {petice}\n")
```

### Rozbalení

* Prvky n-tice lze rozbalit do jednotlivých proměnných.

```python
(prvni, druhy, treti, ctvrty, paty) = petice
print(f"Prvnky n-tice jako proměnné:")
print(prvni, type(prvni), druhy, type(druhy), treti, type(treti), ctvrty, type(ctvrty), paty, type(paty), '\n')
```

### Iterace a metody

* Iterace a metody `index()` a `count()` fungují stejně jako u seznamů.

```python
print(f"Procházení n-tice:")
for prvek in petice:
    print(prvek)

print(f"\nIndex změněného prvku: {petice.index('změněný prvek')}\n")
print(f"Počet dvojek: {petice.count(2)}\n")
```

### Mazání

* N-tici lze odstranit pomocí `del`.

```python
del petice
print(f"Existuje n-tice petice: {'petice' in vars() or 'petice' in globals()}\n")
```

## Práce s množinami (set)

### Vytvoření a vlastnosti

* Sety nemohou obsahovat duplicitní hodnoty.
* Prvky v setu nemají dané pořadí.

```python
zelenina = {"paprika", "rajče", "cuketa", "cuketa"}
print(f"Cvicny set: {zelenina}\n")
```

### Kopírování a iterace

* `copy()`: Vytvoří kopii setu.
* Iterace pomocí cyklu `for`.

```python
kopieZeleniny = zelenina.copy()

print("Jednotlivé prvky cvičného setu:\n")
for prvek in zelenina:
    print(prvek)
```

### Modifikace

* `add(prvek)`: Přidá prvek do setu.
* `update(iterable)`: Přidá všechny prvky z iterovatelného objektu do setu.
* `remove(prvek)`: Odstraní prvek ze setu.
* `discard(prvek)`: Odstraní prvek ze setu, pokud existuje.
* `pop()`: Odstraní a vrátí libovolný prvek ze setu.

```python
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
```

### Operace s množinami

* `union(druhý_set)`: Vrací nový set obsahující všechny prvky z obou setů.
* `intersection(druhý_set)`: Vrací nový set obsahující prvky, které se nacházejí v obou setech.
* `symmetric_difference(druhý_set)`: Vrací nový set obsahující prvky, které se nacházejí pouze v jednom z setů.

```python
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
```

### Mazání

* `clear()`: Vymaže všechny prvky setu.
* `del set`: Odstraní set.

```python
zelenina.clear()
print(f"Prázdný seznam: {zelenina}\n")

del zelenina
print(f"Existuje set zelenina: {'zelenina' in vars() or 'zelenina' in globals()}\n")
```

## Práce se slovníky (dictionary)

### Přístup k prvkům

* K prvkům slovníku se přistupuje pomocí **klíčů**.

```python
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
```

### Modifikace

* Přidání nového prvku: `slovník[klíč] = hodnota`
* Změna hodnoty: `slovník[klíč] = nová_hodnota`
* `update({klíč: hodnota})`: Přidá nebo změní prvek.
* `pop(klíč)`: Odstraní prvek s daným klíčem a vrátí jeho hodnotu.
* `popitem()`: Odstraní a vrátí poslední přidaný prvek.
* `del slovník[klíč]`: Odstraní prvek s daným klíčem.

```python
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
```

### Metody pro práci se slovníky

* `keys()`: Vrací seznam klíčů.
* `values()`: Vrací seznam hodnot.
* `items()`: Vrací seznam dvojic (klíč, hodnota).

```python
print(f"Klíče slovníku: {studenti.keys()}\n")
print(f"Hodnoty slovníku: {studenti.values()}\n")
print(f"Dvojice hodnota klíč: {studenti.items()}\n")
```

### Operátor `in`

* Zjišťuje, zda se daný **klíč** nachází ve slovníku.

```python
print(f"Je novýKlíč v listu: {'novýKlíč' in studenti}\n")
```

### Iterace

* **Procházení klíčů:**

```python
print("Klíče slovníku:")
for klic in studenti:
    print(klic)
```

* **Procházení hodnot:**

```python
print("\nHodnoty slovníku první způsob:")
for klic in studenti:
    print(studenti[klic])

print("\nHodnoty slovníku druhý způsob:")
for hodnota in studenti.values():
    print(hodnota)
```

* **Procházení klíčů a hodnot:**

```python
print("\nKlíč hodnota:")
for klic, hodnota in studenti.items():
    print(klic, hodnota)
```

### Mazání slovníků

* `clear()`: Vymaže všechny prvky slovníku.
* `del slovnik`: Odstraní slovník.

```python
studenti.clear()
print(f"Prázdný slovník: {studenti}\n")

del studenti
print(f"Existuje slovník studenti: {'studenti' in vars() or 'studenti' in globals()}\n")
```

### Kopírování slovníků

* `copy()`: Vytvoří kopii slovníku.

```python
studentiKopie = studenti.copy()
print(f"Kopie slovníku: {studentiKopie}\n") 
```

## Cvičení

**Cvičení 1: Seznam (list)**

1. Vytvořte seznam s názvem `mesta` obsahující 5 libovolných měst.
2. Vypište třetí město v seznamu.
3. Nahraďte druhé město v seznamu městem "Brno".
4. Přidejte na konec seznamu město "Olomouc".
5. Vypište počet měst v seznamu.
6. Seřaďte seznam abecedně.
7. Vytvořte kopii seznamu a uložte ji do proměnné `mesta_kopie`.
8. Vymažte všechna města ze seznamu `mesta`.

**Cvičení 2: N-tice (tuple)**

1. Vytvořte n-tici s názvem `dny` obsahující 7 dnů v týdnu.
2. Vypište pátý den v n-tici.
3. Pokuste se změnit třetí den v n-tici na "Středa".
4. Vytvořte novou n-tici, která bude obsahovat první 3 dny z n-tice `dny`.

**Cvičení 3: Množina (set)**

1. Vytvořte množinu s názvem `barvy` obsahující 5 libovolných barev.
2. Přidejte do množiny barvu "červená".
3. Zkontrolujte, zda se v množině nachází barva "modrá".
4. Odeberte z množiny barvu "zelená".
5. Vytvořte novou množinu s názvem `dalsi_barvy` obsahující 3 barvy.
6. Vypište sjednocení množin `barvy` a `dalsi_barvy`.

**Cvičení 4: Slovník (dictionary)**

1. Vytvořte slovník s názvem `osoba` s klíči "jméno", "věk" a "město".
2. Naplňte slovník libovolnými hodnotami.
3. Vypište věk osoby.
4. Změňte město osoby na "Brno".
5. Přidejte do slovníku nový klíč "zaměstnání" s hodnotou "programátor".
6. Vypište všechny klíče slovníku.
7. Zkontrolujte, zda slovník obsahuje klíč "email".

**Cvičení 5: Kombinace datových struktur**

1. Vytvořte seznam s názvem `zamestnanci`, který bude obsahovat slovníky. Každý slovník bude reprezentovat jednoho zaměstnance a bude obsahovat klíče "jméno", "věk" a "pozice".
2. Přidejte do seznamu 3 zaměstnance.
3. Vypište jméno druhého zaměstnance v seznamu.
4. Změňte pozici prvního zaměstnance na "manažer".
5. Vytvořte nový slovník, který bude reprezentovat dalšího zaměstnance.
6. Přidejte tento slovník na konec seznamu `zamestnanci`.

**Cvičení 6: Nakupni kosik**

Vytvořte program, který bude simulovat jednoduchý nákupní košík. Program by měl umožnit uživateli:

1. Přidat položku do košíku (název položky a cena).
2. Odebrat položku z košíku.
3. Zobrazit obsah košíku.
4. Vypočítat celkovou cenu nákupu.

Pro reprezentaci košíku použijte slovník, kde klíčem bude název položky a hodnotou bude její cena.
