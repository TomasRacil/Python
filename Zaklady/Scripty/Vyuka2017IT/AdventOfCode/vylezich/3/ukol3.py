soubor = open("3.txt", "r").readlines()
pocetStromu = 0
index=0
start = 3
necojineho =0
stav=0
promenna=0
promenna2=12
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
    if(index%11!= 0):
        print(f"start: {start}")
        if(radek[start]=='#'):
            print(radek[start])
            pocetStromu = pocetStromu+1
        if(start==28):
            start = -3
        if(start==29):
            start = -2
        if(start==30):
            start = -1
        start = start + 3
    index = index + 1
print(f"Pocet stromu po tomhle cyklu je: {pocetStromu}")