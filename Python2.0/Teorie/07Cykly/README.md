## Cykly

### Úvod

Cykly umožňují opakovat blok kódu vícekrát. V Pythonu máme dva základní typy cyklů: `while` a `for`.

### Cyklus `while`

Cyklus `while` opakuje blok kódu, dokud je podmínka pravdivá.

```python
i = 0
while i < 5:
  print(i)
  i += 1
```

V tomto příkladu se cyklus opakuje 5krát a vypíše čísla od 0 do 4.

### Klíčové slovo `break`

Klíčové slovo `break` slouží k okamžitému ukončení cyklu.

```python
i = 1
while i < 6:
    print(i)
    if i == 4:
        print("přerušení cyklu!")
        break
    i += 1
```

Zde se cyklus `while` používá pro iteraci a klíčové slovo `break` slouží k předčasnému ukončení cyklu, pokud `i` dosáhne hodnoty 4.

### Cyklus `for`

Cyklus `for` se používá k iteraci přes sekvence (např. seznamy, řetězce, n-tice) nebo generátory.

```python
seznam = ["jablko", "hruška", "banán"]
for ovoce in seznam:
  print(ovoce)
```

V tomto příkladu cyklus projde všechny prvky seznamu a vypíše je.

### Funkce `range()`

Funkce `range()` generuje sekvenci čísel. Často se používá v cyklech `for`.

```python
for i in range(5):  # Generuje čísla od 0 do 4
  print(i)

for i in range(2, 8, 2):  # Generuje čísla od 2 do 6 s krokem 2
  print(i)
```

### Vnořené cykly

Cykly lze vnořovat do sebe.

```python
for i in range(3):
  for j in range(2):
    print(f"i = {i}, j = {j}")
```

V tomto příkladu se vnější cyklus opakuje 3krát a vnitřní cyklus 2krát pro každou iteraci vnějšího cyklu.
