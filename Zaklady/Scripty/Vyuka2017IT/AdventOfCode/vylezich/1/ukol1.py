import time
soubor = open("2000.txt", "r").readlines()
startTime = time.time()
for radek in soubor:
    cislo1 = int(radek.strip())
    rozdil = 2020 - cislo1  # rozdil
    for radek2 in soubor:  # Hledani shody rozdilu a cisla v seznamu
        cislo2 = int(radek2.strip())
        for radek3 in soubor:  # Hledani shody rozdilu a cisla v seznamu
            cislo3 = int(radek3.strip())
            suma = (cislo2+cislo3)
            if rozdil == suma:  # Porovnani daneho cisla ze seznamu
                print(f"Hledaná čísla {cislo1} a {cislo2} a {cislo3}jejich soucin {cislo3*cislo2*cislo1}")

print(f"{time.time()-startTime}\n")