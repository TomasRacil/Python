from os import path

# Nalezení souboru ve stejné složce
cesta_k_souboru = path.join(path.dirname(path.realpath(__file__)), "muj_soubor.txt")

# Čtení ze souboru
with open(cesta_k_souboru, "r") as soubor:
  obsah = soubor.read()
  print(obsah)

# Zápis do souboru
with open(cesta_k_souboru, "w") as soubor:
  soubor.write("Toto je nový obsah souboru.")

# Přidávání do souboru
with open(cesta_k_souboru, "a") as soubor:
  soubor.write("\nToto je přidaný řádek.")