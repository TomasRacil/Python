## Funkce

### Úvod

Funkce v Pythonu, podobně jako v jiných programovacích jazycích, slouží k organizaci kódu do opakovaně použitelných bloků a ke zvýšení jeho přehlednosti. Definujeme je pomocí klíčového slova `def`, za kterým následuje název funkce a v závorkách seznam parametrů.

**Důležité:** Python je interpretovaný jazyk, proto funkce musí být definovány **před** jejich voláním.

### Definice funkce

Základní syntaxe definice funkce vypadá takto:

```python
def nazev_funkce(parametr1, parametr2, ...):
  # odsazený blok kódu
  # ...
```

* `def`: klíčové slovo pro definici funkce
* `nazev_funkce`: identifikátor funkce (měl by být popisný)
* `parametr1, parametr2, ...`: volitelný seznam parametrů, které funkce přijímá
* odsazený blok kódu: tělo funkce, obsahující příkazy, které se mají provést

**Příklad:**

```python
def pozdrav(jmeno):
  """Tato funkce pozdraví uživatele."""
  print(f"Ahoj, {jmeno}!")

pozdrav("Světe")  # Volání funkce s argumentem "Světe"
```

V tomto příkladu definujeme funkci `pozdrav`, která přijímá jeden parametr `jmeno` a vypíše pozdrav. Řetězec v trojitých uvozovkách je tzv. *docstring*, který slouží k dokumentaci funkce.

### Parametry a argumenty

Parametry jsou proměnné, které funkce přijímá při svém volání. Argumenty jsou konkrétní hodnoty, které předáváme funkci při volání.

```python
def secti(a, b):
  """Tato funkce sečte dvě čísla."""
  return a + b

vysledek = secti(5, 3)  # Volání funkce s argumenty 5 a 3
print(vysledek)  # Vypíše 8
```

V tomto příkladu `a` a `b` jsou parametry funkce `secti`. Při volání funkce `secti(5, 3)` jsou `5` a `3` argumenty.

### Návratová hodnota

Funkce může vracet hodnotu pomocí klíčového slova `return`. Pokud funkce neobsahuje `return`, vrací implicitně hodnotu `None`.

```python
def absolutni_hodnota(cislo):
  """Tato funkce vrací absolutní hodnotu čísla."""
  if cislo < 0:
    return -cislo
  else:
    return cislo

print(absolutni_hodnota(-5))  # Vypíše 5
```

### Typy parametrů

Python umožňuje definovat funkce s různými typy parametrů:

* **Poziční parametry:**  jsou předávány v pořadí, v jakém jsou definovány v definici funkce.
* **Klíčové parametry:** jsou předávány s názvem parametru, takže na pořadí nezáleží.
* **Parametry s defaultní hodnotou:**  mají předdefinovanou hodnotu, kterou lze při volání funkce přepsat.
* **Proměnlivý počet pozičních parametrů:**  umožňují funkci přijímat libovolný počet argumentů. Používá se syntaxe `*args`.
* **Proměnlivý počet klíčových parametrů:**  umožňují funkci přijímat libovolný počet argumentů ve formě klíč-hodnota. Používá se syntaxe `**kwargs`.

### Rekurze

Funkce může volat sama sebe. Tomuto mechanismu se říká rekurze.

```python
def faktorial(n):
  """Tato funkce vypočítá faktoriál čísla n."""
  if n == 0:
    return 1
  else:
    return n * faktorial(n-1)

print(faktorial(5))  # Vypíše 120
```

### Lambda funkce

Lambda funkce jsou anonymní funkce definované pomocí klíčového slova `lambda`. Jsou vhodné pro jednoduché operace, které lze vyjádřit na jednom řádku.

```python
mocnina = lambda x, y: x ** y
print(mocnina(2, 3))  # Vypíše 8
```
