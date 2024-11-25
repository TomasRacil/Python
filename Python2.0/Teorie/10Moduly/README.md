## Moduly

### Úvod

Importování modulů je klíčovou součástí programování v Pythonu. Umožňuje nám znovu používat kód, zpřehlednit strukturu programu a využívat rozsáhlé knihovny vytvořené komunitou.

### Základní import

Pro import celého modulu použijeme klíčové slovo `import` následované názvem modulu.

```python
import math

print(math.sqrt(25))  # Vypíše 5.0
```

### Import specifických prvků

Pro import specifických funkcí, tříd nebo proměnných z modulu použijeme `from ... import ...`.

```python
from math import sqrt, pi

print(sqrt(25))  # Vypíše 5.0
print(pi)  # Vypíše 3.141592653589793
```

### Import všech prvků

Pro import všech prvků z modulu použijeme `from ... import *`. Toto se ale obecně nedoporučuje, protože může vést k nejasnostem a konfliktům jmen.

```python
from math import *

print(sqrt(25))  # Vypíše 5.0
print(pi)  # Vypíše 3.141592653589793
```

### Vlastní moduly

Můžeme importovat i vlastní moduly, které jsou uložené v `.py` souborech.

```python
# Soubor muj_modul.py
def pozdrav(jmeno):
  print(f"Ahoj, {jmeno}!")

# V jiném souboru
import muj_modul

muj_modul.pozdrav("Světe")  # Vypíše "Ahoj, Světe!"
```

### Balíčky (packages)

Balíčky jsou složky obsahující více modulů. Pro vytvoření balíčku stačí do složky přidat soubor `__init__.py`.

```
muj_balicek/
├── __init__.py
├── modul1.py
└── modul2.py
```

Pro import z balíčku použijeme tečkovou notaci.

```python
from muj_balicek import modul1

modul1.funkce_z_modulu1()
```

### Relativní import

Relativní import se používá pro import modulů v rámci stejného balíčku. Používá se tečková notace.

* `.`  označuje aktuální modul
* `..` označuje rodičovský modul

```python
# V modulu modul1.py
from . import modul2  # Import modulu modul2.py ze stejného balíčku
from .. import jiny_balicek  # Import modulu jiny_balicek z rodičovského balíčku
```

### Struktura projektu a importy

V projektu s více moduly a balíčky je důležité správně organizovat importy, aby se předešlo cyklickým závislostem a konfliktům jmen. Doporučuje se:

* Uvádět importy na začátku souboru.
* Vyhýbat se `from ... import *`.
* Dodržovat konvence pro pojmenování modulů a balíčků.
