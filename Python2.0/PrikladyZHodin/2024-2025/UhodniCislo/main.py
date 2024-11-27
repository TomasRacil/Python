import random

vygenerovane_cislo:int = random.randrange(0,10)
uhodl = False

while not uhodl:
    try:
        zadane_cislo = input("Zadej cislo: ")
        zadane_cislo = int(zadane_cislo)

        if vygenerovane_cislo == zadane_cislo:
            print("Uhadl jsi")
            uhodl = True
        elif vygenerovane_cislo > zadane_cislo:
            print("Tvuj tip je mensi")
        else:
            print("Tvuj tip je vetsi")
    except ValueError:
        print("Toto neni cislo")
    except Exception as e:
        print(e)