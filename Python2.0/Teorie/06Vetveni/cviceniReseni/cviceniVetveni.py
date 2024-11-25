#3 cviceni
import random


hadane_cislo = random.randrange(0,100)

while True:
    try:
        cislo = int(input("Zadej cislo: "))

        if cislo == hadane_cislo:
            print("Uhodl jsi")
            break
        elif cislo>hadane_cislo:
            print("Tvuj tip je vetsi")
        else:
            print("Tvuj tip je mensi")

    except ValueError:
        print("Toto neni platne cislo")
    except Exception as e:
        print(e)
