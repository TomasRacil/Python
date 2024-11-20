vyraz = input("zadej A jestli souhlasíš: ") == 'A'

if vyraz:
    print("Souhlasíš")
else:
    print("Nesouhlasiš")

try:
    cislo = int(input("zadej cislo: "))

    if cislo > 0:
        print(f"{cislo} je větší jak nula")
    elif cislo < 0:
        print(f"{cislo} je menší jak nula")
    else:
        print(f"{cislo} je nula")

except ValueError:
    print("Toto není číslo")
except Exception as e:
    print(e)

jmeno = input("Tvoje jméno: ")
print(f"Tvoje jmeno je {jmeno}") if jmeno != "" else print("Nezadal jsi jmeno")

volba = int(input("Zadej číslo volby (1-3): "))

match volba:
    case 1:
        print("Zvolil jsi možnost 1")
    case 2:
        print("Zvolil jsi možnost 2")
    case 3:
        print("Zvolil jsi možnost 3")
    case _:  # Defaultní case pro neplatné volby
        print("Neplatná volba")