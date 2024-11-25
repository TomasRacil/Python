# Jednoduchý if-else
cislo = 5
if cislo > 0:
  print("Číslo je kladné.")
else:
  print("Číslo je záporné nebo nula.")

# if-elif-else
cislo = 0
if cislo > 0:
  print("Číslo je kladné.")
elif cislo < 0:
  print("Číslo je záporné.")
else:
  print("Číslo je nula.")

# Vnořené podmínky
cislo = 5
if cislo > 0:
  if cislo % 2 == 0:
    print("Číslo je kladné a sudé.")
  else:
    print("Číslo je kladné a liché.")
else:
  print("Číslo je záporné nebo nula.")

# Inline podmínka
jmeno = input("Tvoje jméno: ")
print(f"Tvoje jmeno je {jmeno}") if jmeno != "" else print("Nezadal jsi jmeno")

# Přepínač s match a case
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