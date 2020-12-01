"""
Vrámci pythonu máme dva typy cyklů while a for. Vycházejí ze stejných principů, jaké můžeme najít u jiných programovacích jazyků.
While opakuje blok kodu dokude je úpodmínka pravdivá.
Oproti tomu for se používá především k procházení datových struktur.
Výraz break je v obou případech používán pro vystoupení z cyklu.
"""

#Základní syntax cyklu while
podminka=True

while podminka:
	podminka=input("Pro opakovani cyklu zadej r: ")=='r'

#Může být využit i pro iterování. V tomto případě je zároveň využito výrazu break pro ukončení cyklu v případě že i je rovno 4.
i = 1
while i < 6:
  print(i)
  if i == 4:
  	print("přerušení cyklu!")
  	break
  i += 1


#Základní syntax for iterujíc seznam. 
seznam = ['python','go','kotlin']
for prvek in seznam:
	print(prvek)

#for je možné použít také nad řetězci
veta = "Procházení řetězce písmeno po písmenu"
for pismeno in veta:
	print(pismeno)

#Ve spojení s for se také čato používá funkce range(od,do,krok), která generuje sekvenci čísel
for cislo in range(5,50,5):
	print(cislo)

#Cykly mohou být samozřejmě i vnořeny jako v jiných jazycích.

i = 1
while i < 6:
	line=""
	for cislo in range(6):			##Při vynechání argumentů ve funkci range(6) -> cisla od 0 do 6 po 1
		line += str(cislo)+", "		## range(1,5) -> cisla od 1 do 5 po 1				range(1,6,2) -> cisla od 1 do 6 po 2
	print(line)
	i += 1