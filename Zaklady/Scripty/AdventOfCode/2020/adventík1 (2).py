soubor = open("cisla.txt", "r")

for prvek in soubor:
    cislo = int(prvek.strip()) 
    zbytek = 2020 - cislo
    soucin = zbytek*cislo
    if (cislo + zbytek == 2020):
        print(f"Součet čísla {zbytek} a čísla {cislo} = 2020 a jejich součin je {soucin}")
"""<<<<<<< HEAD
        Na závěr vypíšu varianty součtů čísel a jejich součiny

=======
        
>>>>>>> 115a6eb54c01f25d8e442be525aac8aaaa3fa5f9"""
