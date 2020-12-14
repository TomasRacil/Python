soubor = open("3.txt", "r").readlines()
pocetStromu = 0
index=0
start = 3
stav=0

for radek in soubor:
    print(index)
    if(index%11!= 0):
        print(f"start: {start}")
        if(radek[start]=='#'):
            print(radek[start])
            pocetStromu = pocetStromu+1
            print(f"Pocet stromu je: {pocetStromu}")
        if(start==28):
            start = -3
        if(start==29):
            start = -2
        if(start==30):
            start = -1
        start = start + 3
    index = index + 1
print(f"Pocet stromu po tomhle cyklu je: {pocetStromu}")