## Výjimky a logování

### Výjimky

Výjimky jsou chyby, které nastanou během běhu programu. V Pythonu se s nimi pracuje pomocí bloků `try` a `except`.

* **`try`:** Blok kódu, ve kterém může dojít k výjimce.
* **`except`:** Blok kódu, který se provede, pokud v bloku `try` dojde k výjimce.

```python
try:
  cislo = int(input("Zadej číslo: "))
  vysledek = 10 / cislo
  print(vysledek)
except ValueError:
  print("Neplatný vstup. Zadej celé číslo.")
except ZeroDivisionError:
  print("Nelze dělit nulou.")
```

V tomto příkladu `try` blok obsahuje kód, který se pokusí převést vstup uživatele na číslo a následně provést dělení. Pokud uživatel zadá nečíselný vstup, dojde k `ValueError`. Pokud zadá 0, dojde k `ZeroDivisionError`. Každá výjimka je ošetřena vlastním blokem `except`.

### Zachycení obecné výjimky

Pro zachycení libovolné výjimky použijeme `except Exception`.

```python
try:
  # ... nějaký kód ...
except Exception as e:
  print(f"Došlo k chybě: {e}")
```

### Vyvolání výjimky

Výjimku můžeme explicitně vyvolat pomocí klíčového slova `raise`.

```python
def over_vek(vek):
  if vek < 0:
    raise ValueError("Věk nemůže být záporný.")

try:
  over_vek(-5)
except ValueError as e:
  print(e)  # Vypíše "Věk nemůže být záporný."
```

### Klíčová slova `else` a `finally`

* **`else`:** Blok kódu, který se provede, pokud v bloku `try` nedojde k výjimce.
* **`finally`:** Blok kódu, který se provede vždy, bez ohledu na to, zda došlo k výjimce nebo ne.

```python
try:
  soubor = open("muj_soubor.txt", "r")
  # ... práce se souborem ...
except FileNotFoundError:
  print("Soubor nenalezen.")
else:
  print("Soubor úspěšně otevřen.")
finally:
  soubor.close()  # Zavření souboru
```

### Vlastní výjimky

Můžeme definovat vlastní výjimky, které dědí od třídy `Exception`.

```python
class MojeVlastniVyjimka(Exception):
  pass

try:
  # ... nějaký kód ...
  raise MojeVlastniVyjimka("Toto je moje vlastní výjimka.")
except MojeVlastniVyjimka as e:
  print(e)
```

### Logování

Logování slouží k zaznamenávání událostí a chyb během běhu programu. V Pythonu se k logování používá modul `logging`.

```python
import logging

# Konfigurace logování
logging.basicConfig(filename="muj_log.log", level=logging.DEBUG)

# Zaznamenání událostí
logging.debug("Debug zpráva")
logging.info("Info zpráva")
logging.warning("Warning zpráva")
logging.error("Error zpráva")
logging.critical("Critical zpráva")

try:
  # ... nějaký kód ...
except Exception as e:
  logging.exception("Došlo k chybě:")  # Zaznamenání výjimky
```

Modul `logging` nabízí různé úrovně logování (DEBUG, INFO, WARNING, ERROR, CRITICAL) a možnosti konfigurace (např. formát zpráv, cíl logování).

