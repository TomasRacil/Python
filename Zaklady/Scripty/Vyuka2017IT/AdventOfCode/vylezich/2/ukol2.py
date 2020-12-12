import time
import re
soubor = open("Hesla.txt", "r").readlines()
starttime = time.time()
pocetplatnychhesel=0
for radek in soubor:
   print(re.split('[- :]', radek.strip()))
   parts=re.split('[- :]', radek.strip())
   if(int(parts[0]) <= parts[4].count(parts[2]) & parts[4].count(parts[2]) <= int(parts[1])):
      pocetplatnychhesel=pocetplatnychhesel+1
      print(radek)

   ##cislo = Petr[2].count(Petr[1])
   ##print(cislo)
print(f"pocet platnych cisel :{pocetplatnychhesel}")
print(f"{time.time()-starttime}\n")