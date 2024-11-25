## Dekorátory

### Úvod

Dekorátory jsou funkce, které modifikují chování jiných funkcí bez nutnosti měnit jejich kód. Fungují jako obal, který můžeme "navléknout" na libovolnou funkci.

### Princip dekorátorů

Dekorátory v Pythonu využívají dvou klíčových vlastností:

1. **Funkce jako objekty:** V Pythonu jsou funkce objekty první třídy, což znamená, že je můžeme předávat jako argumenty jiným funkcím a vracet je jako návratové hodnoty.
2. **Vnořené funkce:** Funkce mohou být definovány uvnitř jiných funkcí.

### Jednoduchý dekorátor

Zde je příklad jednoduchého dekorátoru, který vypíše text před a po volání dekorované funkce:

```python
def muj_dekorator(func):
  def wrapper():
    print("Před voláním funkce.")
    func()
    print("Po volání funkce.")
  return wrapper

@muj_dekorator
def pozdrav():
  print("Ahoj!")

pozdrav()
```

Výstup:

```
Před voláním funkce.
Ahoj!
Po volání funkce.
```

Dekorátor `muj_dekorator` přijímá funkci `func` jako argument. Uvnitř definuje vnořenou funkci `wrapper`, která volá `func` a vypisuje text před a po volání. Dekorátor vrací funkci `wrapper`.

Znak `@` před definicí funkce `pozdrav` je zkratka pro `pozdrav = muj_dekorator(pozdrav)`.

### Dekorátory s argumenty

Dekorátory mohou přijímat i argumenty. V takovém případě musíme definovat další vnořenou funkci, která přijímá argumenty dekorátoru.

```python
def opakuj(pocet):
  def dekorator(func):
    def wrapper(*args, **kwargs):
      for _ in range(pocet):
        func(*args, **kwargs)
    return wrapper
  return dekorator

@opakuj(3)
def pozdrav(jmeno):
  print(f"Ahoj, {jmeno}!")

pozdrav("Světe")
```

Výstup:

```
Ahoj, Světe!
Ahoj, Světe!
Ahoj, Světe!
```

Dekorátor `opakuj` přijímá argument `pocet`. Vrací funkci `dekorator`, která přijímá funkci `func` a vrací funkci `wrapper`. Funkce `wrapper` volá `func` `pocet`-krát.

### functools.wraps

Při použití dekorátorů se může ztratit informace o původní funkci (např. její název a dokumentace). Pro zachování těchto informací použijeme dekorátor `functools.wraps`.

```python
from functools import wraps

def muj_dekorator(func):
  @wraps(func)
  def wrapper():
    print("Před voláním funkce.")
    func()
    print("Po volání funkce.")
  return wrapper

@muj_dekorator
def pozdrav():
  """Tato funkce pozdraví uživatele."""
  print("Ahoj!")

print(pozdrav.__name__)  # Vypíše "pozdrav"
print(pozdrav.__doc__)  # Vypíše "Tato funkce pozdraví uživatele."
```

### Použití dekorátorů

Dekorátory se používají pro různé účely, například:

* **Logování:** Zaznamenávání volání funkcí.
* **Měření času:** Měření doby vykonávání funkcí.
* **Ověřování:** Kontrola vstupních argumentů funkcí.
* **Caching:** Ukládání výsledků funkcí pro opakované použití.

