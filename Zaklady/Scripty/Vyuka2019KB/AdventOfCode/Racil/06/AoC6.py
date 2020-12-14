
#vytváříme list skupin, kde každá skupina obsahuje set jednotlivých osob; split pomocí dvojitých newline skupiny a jedné newline osoby 
customs=[ [set(osoba) for osoba in skupina.split("\n")] for skupina in open("customs.txt", "r").read().split("\n\n")]

#proměnné pro ukládání součtů všech možností a stejných možností ve skupinách
vsechny, stejne=0,0
#procházíme skupin po skupině
for skupina in customs:
	#nad každou skupinou provedeme operaci intersection která vrací set prvků společných všem setům; hvězdička slouží k odkázání na celou množinu
	stejne+=len(set.intersection(*skupina))
	#nad každou skupinou provedeme operaci union která vrací set všech jedinečných prvků těmto setům
	vsechny+=len(set.union(*skupina))
#vytiskneme součet všech délek setů 
print(vsechny, stejne)


#stejné jako předchozí varianta ale převedeno do list comprehension a funkce suma pro součet všech prvků v seznamu
vsechny=sum([len(set.union(*[set(osoba) for osoba in skupina.split("\n")])) 
	for skupina in open("customs.txt", "r").read().split("\n\n")])
stejne=sum([len(set.intersection(*[set(osoba) for osoba in skupina.split("\n")])) 
	for skupina in open("customs.txt", "r").read().split("\n\n")])
print(vsechny,stejne)