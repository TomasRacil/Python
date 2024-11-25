def pozdrav(jmeno):
  """Tato funkce pozdraví uživatele."""
  print(f"Ahoj, {jmeno}!")

def secti(a, b):
  """Tato funkce sečte dvě čísla."""
  return a + b

def faktorial(n):
  """Tato funkce vypočítá faktoriál čísla n."""
  if n == 0:
    return 1
  else:
    return n * faktorial(n-1)

mocnina = lambda x, y: x ** y

# Volání funkcí
pozdrav("Světe")
print(secti(5, 3))
print(faktorial(5))
print(mocnina(2, 3))