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

import os  # [https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html)

os.environ  # TODO: Prozkoumat objekt environ

x, y = 2, 1
print(x / y)  # TODO: Ošetřit dělení nulou

def funkce(parametr='výchozí'):
    """Demonstruje komentování funkce.

    Args:
        parametr (str): Vysvětlení parametru (výchozí 'výchozí').

    Returns:
        str: Vrací parametr.
    """
    return parametr

real = 4.0  # Reálná část čísla
imag = 1.0  # Imaginární část čísla