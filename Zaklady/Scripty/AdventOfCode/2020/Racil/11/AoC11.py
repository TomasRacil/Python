def showPole(pole):
	for radek in pole: print("".join(radek))
	print()

def surounding(pole,r,s):
	x=[]
	for radek in pole[r-1 if r>0 else r:r+2 if r<=len(pole) else None]: x.append(radek[s-1 if s>0 else s:s+2 if s<=len(pole) else None])
	return x

def visible(seating,r,s):
	d1="#" if "#" == next(iter(list(filter((".").__ne__,[radek[:s][-1-index] if s>=1+index else "L" for index,radek in enumerate(seating[:r][::-1])]))),None) else "L"
	up="#" if "#" == next(iter(list(filter((".").__ne__,[radek[s] for radek in seating[:r][::-1]]))),None) else "L"
	d2="#" if "#" == next(iter(list(filter((".").__ne__,[radek[s:][1+index] if len(radek[s:])>index+1 else "L" for index,radek in enumerate(seating[:r][::-1])]))),None) else "L"
	
	lf= "#" if "#" == next(iter([seat for seat in seating[r][:s][::-1] if seat != "."]),None) else "L"
	c=seating[r][s]
	rg= "#" if "#" == next(iter([seat for seat in seating[r][s+1:] if seat != "."]),None) else "L"
	
	d3="#" if "#" == next(iter(list(filter((".").__ne__,[radek[:s][-1-index] if s>=1+index else "L" for index,radek in enumerate(seating[r+1:])]))),None) else "L"
	dw="#" if "#" == next(iter([radek[s] for radek in seating[r+1:] if radek[s] != "."]),None) else "L"
	d4="#" if "#" == next(iter(list(filter((".").__ne__,[radek[s:][index+1] if len(radek[s:])>index+1 else "L" for index,radek in enumerate(seating[r+1:])]))),None) else "L"
			
	return [
	[d1,up,d2],
	[lf,c,rg],
	[d3,dw,d4]
	]


def countOcupiedSeats(pole):
	celkem=0
	for radek in pole: celkem+=radek.count("#")
	return celkem

def fill(seating):
	seatingCopy=[prvek.copy() for prvek in seating]
	for r in range(len(seating)):
		for s in range(len(seating[0])):
			if countOcupiedSeats(surounding(seating,r,s))==0 and seating[r][s]=="L" : seatingCopy[r][s]="#"
	return seatingCopy


def remove(seating):
	seatingCopy=[prvek.copy() for prvek in seating]
	for r in range(len(seating)):
		for s in range(len(seating[0])):
			if countOcupiedSeats(surounding(seating,r,s))>4 and seating[r][s]=="#" : seatingCopy[r][s]="L"
	return seatingCopy

def fill2(seating):
	seatingCopy=[prvek.copy() for prvek in seating]
	for r in range(len(seating)):
		for s in range(len(seating[0])):
			if countOcupiedSeats(visible(seating,r,s))==0 and seating[r][s]=="L" : seatingCopy[r][s]="#"
	return seatingCopy


def remove2(seating):
	seatingCopy=[prvek.copy() for prvek in seating]
	for r in range(len(seating)):
		for s in range(len(seating[0])):
			if countOcupiedSeats(visible(seating,r,s))>5 and seating[r][s]=="#" : seatingCopy[r][s]="L"
	return seatingCopy

def solveSeating(seating,variant):
	while True:
		pocet=countOcupiedSeats(seating)
		seating=fill2(seating) if variant == 2 else fill(seating)
		seating=remove2(seating) if variant == 2 else remove(seating)
		if pocet==countOcupiedSeats(seating):
			showPole(seating)
			return countOcupiedSeats(seating)

seating=[[char for char in line.strip()] for line in open("seats.txt", "r")]
print(solveSeating(seating,1)) #1,91s

#seating=[[prvek for prvek in line.strip()] for line in open("seats.txt", "r")]
#print(solveSeating(seating,2)) #101,48s