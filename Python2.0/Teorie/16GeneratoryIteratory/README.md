## Generátory a iterátory

### Úvod

Iterátory a generátory jsou v Pythonu důležité pro efektivní práci s daty, zejména s velkými objemy dat. Umožňují nám procházet data postupně, aniž bychom museli celou sekvenci načítat do paměti najednou.

### Iterátory

Iterátor je objekt, který umožňuje procházet prvky kolekce (např. seznamu, n-tice, slovníku) jeden po druhém. Implementuje metodu `__next__()`, která vrací další prvek kolekce.

```python
seznam = [1, 2, 3]
iterator = iter(seznam)

print(next(iterator))  # Vypíše 1
print(next(iterator))  # Vypíše 2
print(next(iterator))  # Vypíše 3
```

Funkce `iter()` vytvoří iterátor z dané kolekce. Funkce `next()` zavolá metodu `__next__()` iterátoru a vrátí další prvek. Pokud již nejsou žádné další prvky, vyvolá se výjimka `StopIteration`.

### Generátory

Generátor je speciální typ funkce, která vrací iterátor. Místo klíčového slova `return` používá `yield`. Při každém zavolání `next()` na iterátor generátoru se provede kód funkce až do příkazu `yield`, který vrátí hodnotu a pozastaví vykonávání funkce. Při dalším volání `next()` se pokračuje od místa, kde se funkce pozastavila.

```python
def muj_generator(n):
  for i in range(n):
    yield i * 2

generator = muj_generator(5)

for cislo in generator:
  print(cislo)
```

Výstup:

```
0
2
4
6
8
```

Funkce `muj_generator()` je generátor, který vrací iterátor. Cyklus `for` prochází prvky iterátoru a vypisuje je.

### Výhody generátorů

* **Efektivita:** Generátory generují prvky jeden po druhém, takže nemusíme celou sekvenci ukládat do paměti. To je užitečné pro práci s velkými objemy dat.
* **Jednoduchost:** Syntaxe generátorů je jednoduchá a srozumitelná.
* **Flexibilita:** Generátory můžeme použít pro různé účely, například pro generování nekonečných sekvencí.
