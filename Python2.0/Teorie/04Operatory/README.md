## Operátory

Python nabízí širokou škálu operátorů, podobně jako ostatní programovací jazyky. 

### Kategorie operátorů

* **Aritmetické operátory:** Používají se pro matematické operace.
* **Operátory přiřazení:** Slouží k přiřazení a modifikaci hodnot proměnných.
* **Operátory porovnání:** Umožňují porovnávat hodnoty proměnných.
* **Logické operátory:** Pracují s booleovskými hodnotami (True/False).
* **Operátory příslušnosti:** Zjišťují, zda je hodnota prvkem dané struktury.
* **Binární operátory:** Provádějí operace s binárními čísly.

### Aritmetické operátory

| Operátor | Popis              | Příklad      |
| -------- | ------------------ | ------------ |
| `+`      | Sčítání           | `6 + 6`      |
| `-`      | Odčítání           | `6 - 6`      |
| `*`      | Násobení           | `6 * 6`      |
| `/`      | Dělení             | `6 / 6`      |
| `%`      | Modulus (zbytek)   | `7 % 6`      |
| `**`     | Mocnění            | `2** 2`     |
| `//`     | Celočíselné dělení | `7 // 2`     |

```python
print(f'Sčítat můžeme čísla stejného typu {6+6},')
print(f'ale i různých typů {6+6.5}')
print(f'Sčítat můžeme'+'i řetězce')

print(f'Stejně jako u sčítaní,\n odčítat můžeme čísla stejného typu {6-6},')
print(f'ale i různých typů {6-6.5}')

print(f'Násobit můžeme čísla stejného typu {6*6},')
print(f'ale i různých typů {6*6.5}')
print(f'Násobit můžeme i řetězce. '*3)

print(f'Stejně jako u dělení,\n dělit můžeme čísla stejného typu {6/6},')
print(f'ale i různých typů {6/6.5}')

print(f'Modulus můžeme použít u stejných typů {7%6},')
print(f'ale i různých typů {7%6.5}')

print(f'Mocnit můžeme stejné typy {2**2},')
print(f'ale i různé typy {4**0.5}')

print(f'Dělení na nejnižší celé číslo je možné použít na stejné typy {7//2},')
print(f'ale i různé typy {9//3.5}')
```

### Operátory přiřazení

| Operátor | Popis                                    | Příklad         |
| -------- | --------------------------------------- | --------------- |
| `=`      | Přiřazení hodnoty                        | `x = 5`         |
| `+=`     | Přičtení a přiřazení (`x = x + 3`)       | `x += 5`        |
| `-=`     | Odečtení a přiřazení (`x = x - 3`)       | `x -= 5`        |
| `*=`     | Vynásobení a přiřazení (`x = x * 3`)     | `x *= 5`        |
| `/=`     | Vydělení a přiřazení (`x = x / 3`)       | `x /= 2`        |
| `%=`     | Modulus a přiřazení (`x = x % 3`)        | `x %= 17`       |
| `//=`    | Celočíselné dělení a přiřazení (`x = x // 3`) | `x //= 5`       |
| `**=`    | Umocnění a přiřazení (`x = x ** 3`)     | `x **= 3`       |

```python
x=5
text='text'
print(x,text)

x+=5
text+=' text2'
print(x,text)

x-=5
print(x)

x*=5
text*=2
print(x,text)

x/=2
print(x)

x%=17
print(x)

x//=5
print(x)

x**=3
print(x)
```

### Operátory porovnání

| Operátor | Popis                      | Příklad        |
| -------- | ------------------------- | -------------- |
| `==`     | Rovná se                  | `12 == 12`     |
| `!=`     | Nerovná se                | `12 != 12`     |
| `>`      | Větší než                 | `12 > 12`      |
| `<`      | Menší než                 | `12 < 12`      |
| `>=`     | Větší nebo rovno          | `12 >= 12`     |
| `<=`     | Menší nebo rovno          | `12 <= 12`     |

```python
print(f'12 se rovná  12: {12==12}')
print(f'12 se nerovná 12: {12!=12}')
print(f'12 je menší 12: {12<12}')
print(f'12 se menší nebo rovno 12: {12<=12}')
```

### Logické operátory

| Operátor | Popis                               | Příklad             |
| -------- | ---------------------------------- | ------------------- |
| `and`    | Logický součin (AND)               | `True and False`    |
| `or`     | Logický součet (OR)                | `True or False`     |
| `not`    | Negace (NOT)                       | `not True`          |

```python
print(f'pravda a lež je: {True and False}')
print(f'pravda nebo lež je: {True or False}')
print(f'opak pravdy je: {not True}')
```

### Operátory příslušnosti

| Operátor | Popis                                  |
| -------- | ------------------------------------- |
| `in`     | Je hodnota prvkem struktury?         |
| `not in` | Není hodnota prvkem struktury?       |

```python
seznam = ['python','go','kotlin']
prvek = 'python'

print(f'je {prvek} v {seznam}: {prvek in seznam}')
print(f'není {prvek} v {seznam}: {prvek not in seznam}')
```

### Operátory typu

| Operátor  | Popis                                     |
| --------- | ---------------------------------------- |
| `is`      | Jsou proměnné stejného typu?            |
| `is not`  | Nejsou proměnné stejného typu?          |

```python
text,cislo="text",8

print(f'je {text} a {cislo} stejného typu: {text is cislo}')
print(f'není {text} a {cislo} stejného typu: {text is not cislo}')
```

### Binární operátory

V Pythonu existují i binární operátory (`&, |, ^, ~, <<, >>`), které pracují s čísly na bitové úrovni. Vzhledem k dynamickému typování v Pythonu se však používají méně často.

## Cvičení pro procvičení operátorů v Pythonu

**1. Základní aritmetické operace:**

* Vytvořte proměnné `a = 10` a `b = 3`.
* Vypočítejte a vypište:
    * Součet `a` a `b`
    * Rozdíl `a` a `b`
    * Součin `a` a `b`
    * Podíl `a` a `b` (s desetinnou čárkou)
    * Zbytek po dělení `a` a `b`
    * Celočíselný podíl `a` a `b`
    * `a` umocněno na `b`

**2. Operátory přiřazení:**

* Vytvořte proměnnou `x = 5`.
* Zvyšte hodnotu `x` o 7 pomocí operátoru `+=`.
* Vynásobte hodnotu `x` číslem 3 pomocí operátoru `*=`.
* Odečtěte od hodnoty `x` číslo 4 pomocí operátoru `-=`.
* Vypište výslednou hodnotu `x`.

**3. Porovnávání hodnot:**

* Vytvořte proměnné `a = 15` a `b = 20`.
* Zjistěte a vypište, zda platí:
    * `a` je rovno `b`
    * `a` je různé od `b`
    * `a` je menší než `b`
    * `a` je větší nebo rovno `b`

**4. Logické operátory:**

* Vytvořte proměnné `pravda = True` a `lez = False`.
* Zjistěte a vypište, zda platí:
    * `pravda` a `lez`
    * `pravda` nebo `lez`
    * negace `pravda`

**5. Operátory příslušnosti:**

* Vytvořte seznam `seznam = [1, 2, 3, 4, 5]`.
* Zjistěte a vypište, zda:
    * číslo 3 je v seznamu
    * číslo 6 je v seznamu
    * řetězec "ahoj" je v seznamu

**6. Modulo:**

* Vytvořte program, který si od uživatele vyžádá dvě čísla.
* Program vypíše, zda je první číslo dělitelné druhým číslem (bez zbytku).
* Použijte operátor modulo `%`.