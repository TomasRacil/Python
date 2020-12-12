soubor = open("cisla.txt", "r")

for prvek in soubor:
    cislo = int(prvek.strip()) 
    zbytek = 2020 - cislo
    soucin = zbytek*cislo
    if (cislo + zbytek == 2020):
        print(f"Součet čísla {zbytek} a čísla {cislo} = 2020 a jejich součin je {soucin}")
        
