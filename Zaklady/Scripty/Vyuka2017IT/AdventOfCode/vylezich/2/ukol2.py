import re
soubor = open("Hesla.txt", "r").readlines()
pocetplatnychhesel=0
for radek in soubor:
   parts=re.split('[- :]', radek.strip())
   if(int(parts[0]) <= parts[4].count(parts[2]) & parts[4].count(parts[2]) <= int(parts[1])):
      pocetplatnychhesel=pocetplatnychhesel+1
      print(radek)
print(f"pocet platnych cisel :{pocetplatnychhesel}")
