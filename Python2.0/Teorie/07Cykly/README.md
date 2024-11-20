## Cykly

Python nabízí dva základní typy cyklů: `while` a `for`. Oba slouží k opakování bloku kódu, ale liší se v způsobu použití a podmínkách opakování.

### Cyklus `while`

Cyklus `while` opakuje blok kódu, dokud je daná podmínka pravdivá. Syntaxe je následující:

```python
while podmínka:
    # Blok kódu, který se provede, dokud je podmínka True
```

**Příklad:**

```python
podminka = True

while podminka:
    podminka = input("Pro opakování cyklu zadej r: ") == 'r'
```

V tomto příkladu se cyklus opakuje, dokud uživatel zadává písmeno 'r'.

**Iterace s `while` a `break`:**

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

Cyklus `for` se primárně používá k procházení iterovatelných objektů, jako jsou seznamy, n-tice, řetězce a slovníky. Syntaxe je následující:

```python
for prvek in iterovatelný_objekt:
    # Blok kódu, který se provede pro každý prvek v objektu
```

**Příklady:**

* **Iterace seznamem:**

```python
seznam = ['python', 'go', 'kotlin']
for prvek in seznam:
    print(prvek)
```

* **Iterace řetězcem:**

```python
veta = "Procházení řetězce písmeno po písmenu"
for pismeno in veta:
    print(pismeno)
```

* **Iterace s `range()`:**

```python
for cislo in range(5, 50, 5):
    print(cislo)
```

Funkce `range(od, do, krok)` generuje sekvenci čísel od `od` do `do` (včetně) s krokem `krok`.

### Vnořené cykly

Cykly `while` a `for` lze libovolně vnořovat.

**Příklad:**

```python
i = 1
while i < 6:
    line = ""
    for cislo in range(6):  # Generuje čísla od 0 do 5
        line += str(cislo) + ", "
    print(line)
    i += 1
```

Tento kód demonstruje vnořený cyklus `for` uvnitř cyklu `while`.

### Klíčové slovo `break`

Klíčové slovo `break` slouží k okamžitému ukončení cyklu, ve kterém se nachází.

**Příklad:**

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

V tomto případě se cyklus ukončí, když `i` dosáhne hodnoty 5.

## Cvičení

**1. Součet čísel:**

* Napište program, který sčítá čísla od 1 do `n`, kde `n` je zadáno uživatelem.
* Použijte cyklus `for` a funkci `range()`.

**2. Faktoriál:**

* Napište program, který vypočítá faktoriál čísla `n` zadaného uživatelem.
* Faktoriál čísla `n` (značí se `n!`) je součin všech kladných celých čísel menších nebo rovných `n`. Například 5! = 5 * 4 * 3 * 2 * 1 = 120.
* Použijte cyklus `for` nebo `while`.

**3. Fibonacciho posloupnost:**

* Napište program, který vygeneruje prvních `n` členů Fibonacciho posloupnosti, kde `n` je zadáno uživatelem.
* Fibonacciho posloupnost je definována takto: první dva členy jsou 0 a 1, každý další člen je součtem dvou předchozích. 
  * Například: 0, 1, 1, 2, 3, 5, 8, 13, ...
* Použijte cyklus `for` nebo `while`.

**4. Hledání prvočísel:**

* Napište program, který najde všechna prvočísla v intervalu od 2 do `n`, kde `n` je zadáno uživatelem.
* Prvočíslo je přirozené číslo větší než 1, které je dělitelné pouze 1 a sebou samým.
* Použijte vnořené cykly `for` nebo `while`.

**5. Hra "hádej číslo" s omezeným počtem pokusů:**

* Upravte hru "hádej číslo" z předchozího cvičení tak, aby měl uživatel omezený počet pokusů na uhodnutí čísla.
* Po vyčerpání pokusů program oznámí, že uživatel prohrál.
