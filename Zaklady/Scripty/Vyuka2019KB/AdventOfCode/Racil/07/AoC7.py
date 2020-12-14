pravidla={" ".join(pravidlo.split("contain")[0].split()[0:2]):{" ".join(obsah.split()[1:3]):obsah.split()[0] for obsah in pravidlo.split("contain")[1].split(",")} for pravidlo in open("rules.txt", "r")}

gold=set()
def find(hledany):
	for pravidlo,obsah in pravidla.items():
		if hledany in obsah:
			gold.add(pravidlo + (" ".join(obsah)))
			find(pravidlo)

find("shiny gold")

print(len(gold))


pravidla={" ".join(pravidlo.split("contain")[0].split()[0:2]):{" ".join(obsah.split()[1:3]):obsah.split()[0] for obsah in pravidlo.split("contain")[1].split(",")} for pravidlo in open("rules1.txt", "r")}
for batoh, obsah in pravidla.items():
	print(batoh, obsah)
input()
def find(hledany):
	helper=[]
	for batoh,pocet in pravidla[hledany].items():
		if not "other bags." == batoh: 
			helper.append(int(pocet)*find(batoh))
	return sum(helper)+1

print(find("shiny gold")-1)