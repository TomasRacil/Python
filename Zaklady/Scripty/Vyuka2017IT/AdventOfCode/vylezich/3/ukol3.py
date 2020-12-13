soubor = open("3.txt", "r").readlines()
print(f"Velikost {len(soubor)}")
pocetStromu = 0
index=1
start = 0
stav=0
"""
for radek in soubor:
    print(index)
    print(f"start: {start}")
    if(radek[start]=='#'):
        print(radek[start])
        pocetStromu = pocetStromu+1
    index=index+1
    if(start==30):
        stav=1
    if(start==0):
        stav=0
    if (stav == 0):
        start = start + 3
    if (stav == 1):
        start = start - 3

print(f"Pocet stromu po tomhle cyklu je: {pocetStromu}")"""
for radek in soubor:
    print(index)
    print(f"start: {start}")
    if(radek[start]=='#'):
        print(radek[start])
        pocetStromu = pocetStromu+1
    index=index+1
    if(start==30):
        start=-3
    start = start + 3

print(f"Pocet stromu po tomhle cyklu je: {pocetStromu}")