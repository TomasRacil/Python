soubor = open("cisla.txt", "r")

for prvek in soubor:
    cislo = int(prvek.strip()) 
    """Zbavím se mezer"""
    zbytek = 2020 - cislo
    """od čísla 2020 odečtu číslo a vznikne nám zbytek, ke kterému když přičtu ono číslo, tak vyjde požadovaný součet 2020"""
    soucin = zbytek*cislo
    if (cislo + zbytek == 2020):
        print(f"Součet čísla {zbytek} a čísla {cislo} = 2020 a jejich součin je {soucin}")
        """Na závěr vypíšu varianty součtů čísel a jejich součiny"""
