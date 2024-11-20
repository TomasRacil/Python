# Komentování

Komentování kódu je klíčové pro jeho srozumitelnost a udržovatelnost. V Pythonu se pro komentování používají následující symboly:

- `#` pro jednořádkové komentáře
- `'''` nebo `"""` pro víceřádkové komentáře

## Funkce komentářů

Komentáře slouží k:

- **Vysvětlení fungování kódu:** Pomáhají pochopit logiku a algoritmy.
- **Hledání a řešení chyb:** Dočasné zakomentování kódu pro debugování.
- **Dokumentaci:** Popis funkcí, tříd a modulů.

## Pravidla pro komentování

- **Stručnost a výstižnost:** Komentáře by měly být jasné a stručné.
- **Přehlednost:** Komentujte složité části kódu.
- **Klíčové části:** Komentujte důležité myšlenky a algoritmy.
- **Definice bloků:** Komentujte funkce, třídy a metody.

## Ukázky komentování

**Komentování funkcí:**

```python
def funkce(parametr='výchozí'):
    """Demonstruje komentování funkce.

    Args:
        parametr (str): Vysvětlení parametru (výchozí 'výchozí').

    Returns:
        str: Vrací parametr.
    """
    return parametr
```

**Komentování proměnných:**

```python
real = 4.0  # Reálná část čísla
imag = 1.0  # Imaginární část čísla
```
**Komentování pro ladění a úpravy:**

```python
import os  # [https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html)

os.environ  # TODO: Prozkoumat objekt environ

x, y = 2, 1
print(x / y)  # TODO: Ošetřit dělení nulou
```

**Komentování modulů:**
```python
# -*- coding: utf-8 -*-
"""Název modulu

Popis účelu a funkcí modulu.

Příklad použití:
    $ python priklad.py

Atributy:
    promenna (int): Dokumentace proměnné.

TODO:
    * Seznam úkolů do budoucna

Odkaz na web modulu (pokud existuje)
"""
```

## Další zdroje

- [sphinxcontrib-napoleon](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
