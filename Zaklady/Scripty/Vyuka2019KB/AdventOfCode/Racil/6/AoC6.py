customs=[ [set(osoba) for osoba in skupina.split("\n")] for skupina in open("customs.txt", "r").read().split("\n\n")]

vsechny=0
stejne=0
for skupina in customs:
	stejne+=len(set.intersection(*skupina))
	vsechny+=len(set.union(*skupina))
print(vsechny, stejne)



vsechny=sum([len(set.union(*[set(osoba) for osoba in skupina.split("\n")])) 
	for skupina in open("customs.txt", "r").read().split("\n\n")])
stejne=sum([len(set.intersection(*[set(osoba) for osoba in skupina.split("\n")])) 
	for skupina in open("customs.txt", "r").read().split("\n\n")])
print(vsechny,stejne)