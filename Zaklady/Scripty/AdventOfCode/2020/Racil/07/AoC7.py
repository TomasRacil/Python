import functools
pravidla={" ".join(pravidlo.split("contain")[0].split()[0:2]):{" ".join(obsah.split()[1:3]):obsah.split()[0] for obsah in pravidlo.split("contain")[1].split(",")} for pravidlo in open("rules.txt", "r")}

gold=set()
def find_2(hledany):
	for pravidlo,obsah in pravidla.items():
		if hledany in obsah:
			gold.add(pravidlo + (" ".join(obsah)))
			find_2(pravidlo)



@functools.lru_cache(maxsize=1000)
def find(hledany):
	helper,batohy=[],{}
	for batoh,pocet in pravidla[hledany].items():
		if not "other bags." == batoh: 
			helper.append(int(pocet)*find(batoh))
			batohy[batoh]=pocet
	#print(hledany,batohy)
	return sum(helper)+1

find_2("shiny gold")
print(len(gold))

print(find("shiny gold")-1)