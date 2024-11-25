import logging

# Konfigurace logování
logging.basicConfig(filename="muj_log.log", level=logging.DEBUG)

try:
  cislo = int(input("Zadej číslo: "))
  vysledek = 10 / cislo
  print(vysledek)
except ValueError:
  print("Neplatný vstup. Zadej celé číslo.")
  logging.exception("ValueError")
except ZeroDivisionError:
  print("Nelze dělit nulou.")
  logging.exception("ZeroDivisionError")
else:
  logging.info(f"Výsledek: {vysledek}")
finally:
  logging.debug("Konec programu.")