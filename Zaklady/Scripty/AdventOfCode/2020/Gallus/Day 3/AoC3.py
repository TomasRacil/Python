#prochazim input.txt a jdu o 3DOPRAVA a 1DOLU a pocitam hashtagy na ktere narazim na konci kazdeho cyklu
"""soubor = open ("input.txt","r").readlines()
strom=0
for radek in soubor:
    soubor[strom] = radek.strip()
    strom+=1

            TENTO POSTUP JE TO SAME CO PRVNI RADEK (nacitani souboru)
"""
soubor = [radek.strip() for radek in open("input.txt","r").readlines()]

pozice = 0
strom = 0

for radek in soubor:
    if radek[pozice]=="#": strom+=1
    if pozice+3>=len(radek): pozice=pozice-len(radek)
    pozice+=3

print(f"Pocet stromu v ceste (*): {strom}")

"""SECOND STAR -> 
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""
strom2 = 0
for radek in soubor:
    if radek[pozice]=="#": strom2+=1
    if pozice+1>=len(radek): pozice=pozice-len(radek)
    pozice+=1

strom3 = 0
for radek in soubor:
    if radek[pozice]=="#": strom3+=1
    if pozice+5>=len(radek): pozice=pozice-len(radek)
    pozice+=5

strom4 = 0
for radek in soubor:
    if radek[pozice] == "#": strom4 += 1
    if pozice + 7 >= len(radek): pozice = pozice - len(radek)
    pozice += 7


strom5 = 0
for radek in soubor:
    if radek[pozice]=="#": strom5+=1
    if pozice+1>=len(radek): pozice=pozice-len(radek)
    pozice+=1

soucin = strom*strom2*strom3*strom4*strom5

print(f"Pocet stromu v ceste(**): {strom},{strom2},{strom3},{strom4},{strom5}")
print(f"\t -> soucin cisel(**): {soucin}")


