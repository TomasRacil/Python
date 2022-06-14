"""
Způsob jakým bych já odpověděl na otázky, které byly v uvodnim testu
"""
import logging
from random import randint


def prvni_algoritmus(jmeno: str, prijmeni: str, rozsah: int):
    """
    První algoritmus

    Args:
            jméno (str): křestní jméno
            prijmeni (str): příjmení
            rozsah (int): velikost prohledávaného vzorku
    """
    for cislo in range(1, rozsah):
        if cislo % len(jmeno + prijmeni) == 0:
            val = "x" if cislo % len(jmeno) == 0 else cislo * 2
            print(val)
        elif cislo % len(jmeno) != 0:
            print(cislo)


def vytvor_2d_pole(
    col: int, row: int, hodnoty_od: int, hodnoty_do: int
) -> list[list[int]]:
    """
    Vytvori 2D pole

    Args:
            row (int): počet sloupců
            col (int): počet řádků
            od (int): nejnižší možná hodnota v poli
            do (int): nejvyšší možná hodnota v poli

    Returns:
            list: vrací vygenerované 2D pole náhodných hodnot
    """
    return [
        [randint(hodnoty_od, hodnoty_do) for radek in range(col)]
        for sloupec in range(row)
    ]


def druhy_algoritmus(pole: list[list[int]], prijmeni: str) -> tuple[int, int, int]:
    """
    Druhý algoritmus

    Args:
            pole (list[list[int]]): 2D pole k vyhodnocení
            prijmeni (str): přijmení

    Returns:
            tuple[int,int]: vrací maximum, minimum a počet shod v matici
    """
    maximum, minimum, pocet = pole[0][0], pole[0][0], 0
    for radek in pole:
        for prvek in radek:
            if prvek == len(prijmeni):
                pocet += 1
            if prvek < minimum:
                minimum = prvek
            elif prvek > maximum:
                maximum = prvek
    return maximum, minimum, pocet


def treti_algoritmus(cislo: int):
    """Třetí algoritmus

    Args:
            cislo (int): číslo, nad kterým má být proveden faktoriál

    Returns:
            int: vrací faktoriál čísla
    """
    if cislo > 0:
        if cislo in [0, 1]:
            return 1
        else:
            return cislo * treti_algoritmus(cislo - 1)
    else:
        logging.exception("Nastala vyjímka")


def main():
    """
    main
    """
    jmeno = input("Zadej jméno: ")
    prijmeni = input("Zadej prijmeni: ")

    print("\nNásleduje výpis čísel splňujících podmínky")

    prvni_algoritmus(jmeno, prijmeni, 100)

    pole = vytvor_2d_pole(5, 5, 0, 100)
    input("Enter pro pokracovani")
    print("\nNásleduje výpis náhodně vygenerovaného pole")

    for radek in pole:
        print(radek)

    maximum, minimum, pocet = druhy_algoritmus(pole, prijmeni)

    print(
        f"Maximum v poli je {maximum}; minimum je {minimum};\
            počet výskytů {len(prijmeni)} je {pocet}"
    )

    while True:
        try:
            cislo = input("\nFaktoriál jakého čísla chcete spočítat: ")
            cislo = int(cislo)
            break
        except ValueError:
            logging.exception("Toto neni cislo. Zkuste to znovu")

    print(f"Faktoriál je {treti_algoritmus(cislo)}")


if __name__ == "__main__":
    main()
