import re
soubor = open("Hesla.txt", "r").readlines()
pocetplatnychhesel=0
for radek in soubor:
   parts=re.split('[- :]', radek.strip()) ##uložení upraveného řádku do proměnné parts - usnadní budoucí práci - !! vznikl prázdný list parts{2} :(
   """Hledání počtu prvků v heslu a následná kontrola, jestli počet daných prvků spadá do vytyčeného intervalu"""
   if(int(parts[0]) <= parts[4].count(parts[2]) & parts[4].count(parts[2]) <= int(parts[1])):
      pocetplatnychhesel=pocetplatnychhesel+1
print(f"pocet platnych cisel :{pocetplatnychhesel}")

##Druhy ukol
pocet2 =0
for radek in soubor:
   parts = re.split('[- :]', radek.strip()) ##Ulození jednotlivých údajů do listu
   seznam=list(parts[4])
   """Odečtení -1 od zadaného intervalu umožní pracovat s listy na stejných indexech - tedy 7-1=6, takže se bude hovořit o 6. prvku i v seznamu"""
   index1=int(parts[0])-1
   index2=int(parts[1])-1
   """Podmínka zajišťuje, aby byl výskyt prvku pouze jednou - tedy splnil private policy"""
   if((((parts[2])== seznam[index1]) != (parts[2] == seznam[index2])) & ((parts[2] == seznam[index2] or (parts[2]) == seznam[index1]))):
      pocet2=pocet2+1

print(f"Pocet platnych cisel při splnění 2. podmínky: {pocet2}")
