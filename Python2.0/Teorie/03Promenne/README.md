## Proměnné

V Pythonu se datový typ proměnné neurčuje explicitně, ale je dynamicky přiřazen při jejím vytvoření. K ověření typu proměnné slouží funkce `type()`. Každá proměnná je ve skutečnosti objekt s vlastními metodami.

### Základní datové typy

#### Číselné typy

* **int:** Celá čísla, bez omezení velikosti (kromě paměti zařízení). Python interně používá pouze tento typ pro celá čísla.
* **float:** Čísla s plovoucí desetinou čárkou, bez omezení velikosti.
* **complex:** Komplexní čísla, bez omezení.

```python
integer: int = 1
print(f"hodnota {integer} typ {type(integer)}")

binary: bin = 0b10  # Binární číslo
print(f"hodnota {binary} typ {type(binary)}")

octal = 0o10  # Osmičkové číslo
print(f"hodnota {octal} typ {type(octal)}")

hexadecimal = 0x10  # Šestnáctkové číslo
print(f"hodnota {hexadecimal} typ {type(hexadecimal)}")

floatingPointNumber = 2.58
print(f"hodnota {floatingPointNumber} typ {type(floatingPointNumber)}")

floatingPointNumber = 4.2e-4  # Vědecký zápis
print(f"hodnota {floatingPointNumber} typ {type(floatingPointNumber)}")

complexNumber = 2 + 3j
print(f"hodnota {complexNumber} typ {type(complexNumber)}")
```

#### Řetězce (str)

Řetězce lze zapisovat třemi způsoby:

* Pomocí dvojitých uvozovek (`"`).
* Pomocí jednoduchých uvozovek (`'`).
* Pomocí trojice uvozovek (`"""`). Umožňuje zápis víceřádkových řetězců.

```python
text1: str = "Ahoj "
text2: str = 'světe!'
print(f"hodnoty: {text1}, {text2} typ {type(text1)}, {type(text2)}")

text3: str = """
Mezi trojící uvozovek je text ukládán
ve stejném formátu jako byl napsán
včetně řádků 
  a odstavců
"""
print(f"hodnota: {text3} typ {type(text3)}")
```

#### Boolean (bool)

Binární typ s hodnotami `True` a `False`.

```python
boolean: bool = True
print(f"hodnota {boolean} typ {type(boolean)}")
```

### Práce s řetězci

Řetězce v Pythonu jsou sekvence znaků, které lze indexovat a iterovat.

#### Formátování řetězců

Existují tři způsoby formátování:

* Pomocí operátoru `%`.
* Pomocí metody `format()`.
* Pomocí f-stringů (od Pythonu 3.6).

```python
pozdrav, poradi = 'Zdravím', '3'

formatovanyText1 = "%s. Toto je %s. lekce" % (pozdrav, poradi)
print(formatovanyText1)

formatovanyText2 = "{1}. Toto je {0}. lekce".format(poradi, pozdrav)
print(formatovanyText2)

formatovanyText3 = f"{pozdrav}. Toto je {poradi}. lekce"
print(formatovanyText3)
```

#### Escape sekvence

Pro vložení speciálních znaků do řetězce se používají escape sekvence (např. `\n` pro nový řádek, `\t` pro tabulátor).

```python
print('\n "Naučila jsem se, že cesta pokroku není rychlá ani snadná." \n \t— Marie Curie-Skłodowská\n')
print("Například jednu uvozovku: \", \nnebo znak pro nový rádek je \\n\n")
```

#### Indexování a slicing

```python
text = "Ukázkový text pro potřeby indexace a iterace\n"
print(text)
print(f'Symbol na druhém místě je {text[2]}\n')  # Indexování začíná od 0
print(f'Symbol na druhém místě od konce je {text[-2]}\n')  # Záporné indexování
print(f'Symboly od 8 znaku do 8 znaku před koncem  {text[8:-8]}\n')  # Slicing
```

#### Iterace

```python
for znak in text:
    print(znak)
```

#### Užitečné metody

* `len()`: Vrací délku řetězce.
* `lower()`: Převede řetězec na malá písmena.
* `upper()`: Převede řetězec na velká písmena.
* `replace()`: Nahradí část řetězce jiným řetězcem.
* `split()`: Rozdělí řetězec na seznam podřetězců.
* `strip()`: Odstraní bílé znaky ze začátku a konce řetězce.
* `find()`: Najde index prvního výskytu podřetězce.
* `count()`: Spočítá počet výskytů podřetězce.
* `join()`: Spojí seznam řetězců do jednoho řetězce.

```python
print(f'Délka řetězce:  {len(text)}\n')
print(f'Text malými písmeny:  {text.lower()}\n')
print(f'Text kapitálky:  {text.upper()}\n')
print(f'Změna prvního slova:  {text.replace("Ukázkový", "Vzorový")}\n')
print(f'Rozdělení podle mezer:  {text.split(" ")}\n')

zbytecneMocPomlcek = '-------text------'
print(f'Bez pomlcek: {zbytecneMocPomlcek.strip("-")}\n')

print(f'Index prvního ř:  {text.find("ř")}\n')
print(f'Počet znaků a:  {text.count("a")}\n')

programovaciJazyky = ['Python', 'Kotlin', 'Go']
print(f'Převedení seznamu do stringu: {", ".join(programovaciJazyky)}')
```

### Přetypování (casting)

V Pythonu lze přetypovat proměnné z jednoho typu na jiný pomocí funkcí `int()`, `float()` a `str()`.

```python
string = '5'
print(f'1. Hodnota {string} typ {type(string)}\n')

cislo = int(string)  # Převod string na int
print(f'2. Hodnota {cislo} typ {type(cislo)}\n')

desetineCislo = 5.5
print(f'3. Hodnota {desetineCislo} typ {type(desetineCislo)}\n')

cislo = int(desetineCislo)  # Převod float na int (ztráta desetinné části)
print(f'4. Hodnota {cislo} typ {type(cislo)}\n')

desetineCislo = float(cislo)  # Převod int na float
print(f'5. Hodnota {desetineCislo} typ {type(desetineCislo)}\n')

desetineCislo = float(string)  # Převod string na float
print(f'6. Hodnota {desetineCislo} typ {type(desetineCislo)}\n')

string = str(cislo)  # Převod int na string
print(f'7. Hodnota {string} typ {type(string)}\n')

string = str(string)  # Převod string na string (beze změny)
print(f'8. Hodnota {string} typ {type(string)}\n')
```
## Cvičení

**1. Výměna hodnot:**

* Vytvořte dvě proměnné `a` a `b` s libovolnými hodnotami.
* Vyměňte hodnoty těchto proměnných bez použití třetí proměnné.
* Vypište hodnoty proměnných `a` a `b` před a po výměně.

**2. Formátování textu:**

* Vytvořte proměnné `jmeno`, `prijmeni` a `vek` s vašimi údaji.
* Naformátujte a vypište text: "Jmenuji se [jmeno] [prijmeni] a je mi [vek] let." pomocí f-stringů.

**3. Práce s řetězcem:**

* Vytvořte proměnnou `veta` s libovolnou větou.
* Zjistěte délku věty.
* Převeďte větu na velká písmena.
* Nahraďte ve větě první výskyt slova "a" slovem "nebo".
* Rozdělte větu na seznam slov.
* Vypište třetí slovo z věty.

**4. Přetypování:**

* Vytvořte proměnnou `cislo_str` s hodnotou "123".
* Převeďte tuto proměnnou na typ `int`.
* Vynásobte číslo 5 a vypište výsledek.

**5. Palindrom:**

* Vytvořte program, který si od uživatele vyžádá vstupní řetězec.
* Program vypíše, zda je vstupní řetězec palindrom (tj. čte se stejně zepředu i zezadu, např. "kajak").

