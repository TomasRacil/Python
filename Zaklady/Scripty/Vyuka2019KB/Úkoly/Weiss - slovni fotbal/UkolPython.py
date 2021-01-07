

with open("slovnik.txt", "r", encoding="utf-8") as f:
    slova = []
    for radek in f.readlines():
        radek = radek.strip()
        slova.append(radek)
         # Odstraníme "\n"

zadej = input("Zadej slovo: ")
for neco in len(f):
    if zadej == slova[neco]: 
        print(f,"ok")
