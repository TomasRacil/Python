import random

volby ={
    "kamen":"nuzky",
    "nuzky":"papir",
    "papir":"kamen"
}

nahodna_volba = random.choice([volba for volba in volby.keys()])

zadana_volba = input("Zadej volbu: ")

if nahodna_volba == zadana_volba:
    print("remiza")
elif nahodna_volba == volby[zadana_volba]:
    print("vyhra")
else:
    print("prohra")
