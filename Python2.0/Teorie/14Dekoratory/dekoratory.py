from functools import wraps

def muj_dekorator(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    print("Před voláním funkce.")
    vysledek = func(*args, **kwargs)
    print("Po volání funkce.")
    return vysledek
  return wrapper

@muj_dekorator
def secti(a, b):
  """Tato funkce sečte dvě čísla."""
  return a + b

vysledek = secti(5, 3)
print(f"Výsledek: {vysledek}")
print(secti.__name__)
print(secti.__doc__)