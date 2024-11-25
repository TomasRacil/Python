## Předávání argumentů

### Úvod

Předávání argumentů z příkazové řádky umožňuje uživatelům interagovat se skriptem a předávat mu data. To je užitečné pro automatizaci, konfiguraci a spouštění skriptů s různými parametry.

### Modul `argparse`

Modul `argparse` je standardní knihovna Pythonu pro parsování argumentů z příkazové řádky. Umožňuje definovat argumenty, jejich typy, popisky a výchozí hodnoty.

### Vytvoření parseru

Prvním krokem je vytvoření instance třídy `ArgumentParser`.

```python
import argparse

parser = argparse.ArgumentParser(description='Popis programu.')
```

### Přidání argumentů

Pomocí metody `add_argument()` přidáme argumenty, které skript očekává.

```python
parser.add_argument('jmeno', type=str, help='Jméno uživatele.')
parser.add_argument('-v', '--vek', type=int, default=18, help='Věk uživatele.')
```

* `jmeno`: Poziční argument typu `str` s popiskem "Jméno uživatele."
* `-v`, `--vek`: Nepovinný argument typu `int` s krátkou vlajkou `-v`, dlouhou vlajkou `--vek`, výchozí hodnotou `18` a popiskem "Věk uživatele."

### Parsování argumentů

Metoda `parse_args()` zpracuje argumenty z příkazové řádky a vrátí objekt s atributy odpovídajícími argumentům.

```python
args = parser.parse_args()

print(f"Jméno: {args.jmeno}")
print(f"Věk: {args.vek}")
```

### Spuštění skriptu

Skript spustíme z příkazové řádky s argumenty:

```
python muj_skript.py Jan -v 25
```

Výstup:

```
Jméno: Jan
Věk: 25
```

### Další možnosti

Modul `argparse` nabízí mnoho dalších možností, například:

* **Definování typů argumentů:**  Můžeme použít vlastní funkce pro validaci a konverzi argumentů.
* **Vytváření skupin argumentů:**  Můžeme logicky seskupovat argumenty.
* **Definování vzájemně se vylučujících argumentů:**  Můžeme definovat argumenty, které se nesmí použít společně.
* **Generování nápovědy:**  Modul `argparse` automaticky generuje nápovědu pro skript.
