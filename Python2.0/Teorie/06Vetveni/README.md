## Větvení

V Pythonu se pro větvení programu používají klíčová slova `if`, `elif` a `else`. Umožňují vykonávat různé bloky kódu v závislosti na splnění podmínek.

### Syntaxe

* **Jednoduché větvení (`if`)**

```python
if podmínka:
    # Blok kódu, který se provede, pokud je podmínka True
```

* **Větvení s alternativou (`if-else`)**

```python
if podmínka:
    # Blok kódu, který se provede, pokud je podmínka True
else:
    # Blok kódu, který se provede, pokud je podmínka False
```

* **Vícenásobné větvení (`if-elif-else`)**

```python
if podmínka1:
    # Blok kódu, který se provede, pokud je podmínka1 True
elif podmínka2:
    # Blok kódu, který se provede, pokud je podmínka2 True
elif podmínka3:
    # Blok kódu, který se provede, pokud je podmínka3 True
else:
    # Blok kódu, který se provede, pokud žádná z podmínek není True
```

### Příklady

* **Jednoduchý `if-else` statement:**

```python
vyraz = input("zadej A jestli souhlasíš: ") == 'A'

if vyraz:
    print("Souhlasíš")
else:
    print("Nesouhlasiš")
```

* **Vícenásobné větvení s `elif`:**

```python
try:
    cislo = int(input("zadej cislo: "))

    if cislo > 0:
        print(f"{cislo} je větší jak nula")
    elif cislo < 0:
        print(f"{cislo} je menší jak nula")
    else:
        print(f"{cislo} je nula")

except ValueError:
    print("Toto není číslo")
except Exception as e:
    print(e)
```

* **Inline podmínka:**

```python
jmeno = input("Tvoje jméno: ")
print(f"Tvoje jmeno je {jmeno}") if jmeno != "" else print("Nezadal jsi jmeno")
```

### Přepínač

Od verze Pythonu 3.10 je možné použít `match` a `case` pro simulaci přepínače.

```python
volba = int(input("Zadej číslo volby (1-3): "))

match volba:
    case 1:
        print("Zvolil jsi možnost 1")
    case 2:
        print("Zvolil jsi možnost 2")
    case 3:
        print("Zvolil jsi možnost 3")
    case _:  # Defaultní case pro neplatné volby
        print("Neplatná volba")
```

V tomto případě příkaz `match` porovnává hodnotu proměnné `volba` s jednotlivými `case` bloky. Pokud dojde ke shodě, provede se kód v daném bloku. Klíčové slovo `_` funguje jako defaultní case a zachytí všechny hodnoty, které neodpovídají žádnému z předchozích `case` bloků.

## Cvičení

**1. Kontrola věku:**

* Napište program, který si vyžádá od uživatele jeho věk.
* Program vypíše, zda je uživatel:
    * Dítě (věk < 18 let)
    * Dospělý (18 <= věk < 65 let)
    * Senior (věk >= 65 let)

**2. Kalkulačka:**

* Napište program, který si vyžádá od uživatele dvě čísla a operaci (+, -, *, /).
* Program provede zadanou operaci a vypíše výsledek.
* Použijte `match` a `case` pro výběr operace.
* Ošetřete případné chyby, např. dělení nulou.

**3. Hádání čísla:**

* Program si náhodně vygeneruje číslo od 1 do 100.
* Uživatel hádá číslo. Program mu napovídá, zda je hádané číslo větší nebo menší než to správné.
* Po uhodnutí čísla program vypíše počet pokusů.

**4. Přestupný rok:**

* Napište program, který si vyžádá od uživatele rok.
* Program zjistí a vypíše, zda je zadaný rok přestupný.
* Rok je přestupný, pokud je dělitelný 4, ale není dělitelný 100, s výjimkou roků dělitelných 400.

**5. Kámen, nůžky, papír**

* Vytvořte program, který simuluje jednoduchou hru "kámen, nůžky, papír" proti počítači.
* Počítač náhodně vybere jednu z možností.
* Uživatel zadá svou volbu.
* Program vyhodnotí výsledek hry a vypíše, kdo vyhrál.

**Doporučení:**

* Pro generování náhodných čísel použijte modul `random`.
* Pro ošetření chyb použijte `try-except` bloky.
* Pro kontrolu vstupu od uživatele použijte podmínky a cykly.
* Nezapomeňte na komentáře v kódu, které vysvětlují, co program dělá.
