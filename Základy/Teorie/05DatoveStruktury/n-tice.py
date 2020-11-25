#ukázková n-tice
petice = ('první prvek',2,['prvni prvek listu',2],2,'poslední prvek')



#Přístup k jednotlivým prvkům je prováděn přes indexy. Index prvního prvku je vždy nula.
print(f"První prvek: {petice[1]}\n")

#Při použití záporných indexů přistupujeme k prvkům v opačném pořadí tedy od konce.
print(f"Poslední prvek: {petice[-1]}\n")

#Při použití [index:index] tvoříme podmnožinu n-tice v rozsahu těchto dvou indexů. Takzvaný slicing.
print(f"Třetí až předposlední prvek: {petice[3:-2]}\n")

#Při použití [:index] nebo [index:] vytváříme podmnožinu všech prvků z leva po index, nebo z prava po index
print(f"Všechny prvky od druhého prvku: {petice[:2]}\n")

#Přistup k prvkům vnořeného seznamu je prováděn kombinací indexu vnořeného seznamu, a indexu prvku uvnitř vnořeného seznamu.
print(f"Poslední prvek vnořeného seznamu: {petice[2][-1]}\n")



#N-tice není možné po jejich vytvoření změnit
#jediný způsob jak změnit po vytvoření je převést je na seznam pomocí castingu
#změnit list a ntici vytvořit znovu
print(f"Původní n-tice: {petice}\n")
seznam=list(petice)
seznam[2]='změněný prvek'
petice=tuple(seznam)
print(f"Změněná n-tice: {petice}\n")



#Pokud chceme získat jednotlivé prvky n-tice a pracovat s nimi jako s proměnými
#můžeme je rozbalit do stejného počtu proměných jako je prvků v n-tici
(prvni,druhy,treti,ctvrty,paty)=petice
print(f"Prvnky n-tice jako proměnné:")
print(prvni,type(prvni),druhy,type(druhy),treti,type(treti),ctvrty, type(ctvrty), paty, type(paty),'\n')



#Pokud chceme iterovat skrze n-tici použijeme for loop
print(f"Procházení n-tice:")
for prvek in petice:
	print(prvek)



#Pro nalezení indexu konkrétního prvku použijeme metodu index('hodnota prvku')
print(f"\nIndex změněného prvku: {petice.index('změněný prvek')}\n")

#Pro spočítání výskytu konkrétního prvku použijeme metodu count(hodnota prvku)
print(f"Počet dvojek: {petice.count(2)}\n")

#odstranění n-tice můžeme provést pomoci del
del petice
print(petice)