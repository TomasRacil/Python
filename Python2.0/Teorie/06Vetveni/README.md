## Větvení

### Úvod

Větvení umožňuje programu vykonávat různé bloky kódu v závislosti na splnění podmínek. V Pythonu se k větvení používají klíčová slova `if`, `elif` a `else`.

### Příkaz `if`

Příkaz `if` provede blok kódu, pokud je podmínka pravdivá.

```python
cislo = 5
if cislo > 0:
  print("Číslo je kladné.")
```

### Příkaz `else`

Příkaz `else` se používá v kombinaci s `if` a provede blok kódu, pokud podmínka v `if` není pravdivá.

```python
cislo = -5
if cislo > 0:
  print("Číslo je kladné.")
else:
  print("Číslo je záporné nebo nula.")
```

### Příkaz `elif`

Příkaz `elif` (zkratka pro "else if") umožňuje testovat více podmínek.

```python
cislo = 0
if cislo > 0:
  print("Číslo je kladné.")
elif cislo < 0:
  print("Číslo je záporné.")
else:
  print("Číslo je nula.")
```

### Vnořené podmínky

Podmínky lze vnořovat do sebe.

```python
cislo = 5
if cislo > 0:
  if cislo % 2 == 0:
    print("Číslo je kladné a sudé.")
  else:
    print("Číslo je kladné a liché.")
else:
  print("Číslo je záporné nebo nula.")
```

### Inline podmínka

Pro jednoduché podmínky lze použít inline zápis.

```python
jmeno = input("Tvoje jméno: ")
print(f"Tvoje jmeno je {jmeno}") if jmeno != "" else print("Nezadal jsi jmeno")
```

### Přepínač s `match` a `case` (Python 3.10+)

Od verze Python 3.10 je k dispozici příkaz `match`, který funguje podobně jako `switch` v jiných jazycích.

```python
den = input("Zadej den v týdnu (1-7): ")

match den:
  case "1":
    print("Pondělí")
  case "2":
    print("Úterý")
  case "3":
    print("Středa")
  case "4":
    print("Čtvrtek")
  case "5":
    print("Pátek")
  case "6":
    print("Sobota")
  case "7":
    print("Neděle")
  case _:  # Defaultní větev
    print("Neplatný den.")
```
