
soubor=[int(line.strip()) for line in open("sequence.txt", "r")]
"""que=[]

def najdiScitance(cislo,seznam,vnoreni=1):
	print(vnoreni)
	for prvek in seznam:
		if cislo-prvek>0:
			print(cislo-prvek)
			#najdiScitance(cislo-prvek,seznam,vnoreni+1)

			

for cislo in soubor:
	if len(que)<25:
		que.append(cislo)
	elif len(que)==25:
		if not len(set(que).intersection(set([cislo-prvek for prvek in que])))>=2:
			print(cislo,que,set(que).intersection(set([cislo-prvek for prvek in que])))
			print(najdiScitance(cislo,que))
			input()
		que.pop(0)
		que.append(cislo)"""


def valid(i):
	if len(set(soubor[i-26:i]).intersection(set([soubor[i]-prvek for prvek in soubor[i-26:i] if prvek<soubor[i]])))>=2 or i<26: return True
	else: return False

"""i=0
podminka=True
while podminka:
	podminka= valid(i)
	if podminka==False:
		print(soubor[i],i)
	i+=1"""

def findWrong(i):
	if valid(i)==False: return(i,soubor[i])
	else: return findWrong(i+1)
print(findWrong(0))

cislo=findWrong(0)[1]



def secti(i,zbytek):
	if zbytek-soubor[i+1]<=0: return [soubor[i]]
	else: return secti(i+1,zbytek-soubor[i])+[soubor[i]]
x=secti(0,cislo)
#print(x,cislo-sum(x[1:]))

def findWeakness(i):
	x=secti(i,cislo)
	if sum(x)==cislo: return x
	else: return findWeakness(i+1)

"""podminka=True
i=0
while podminka:
	x=secti(0,cislo)
	if sum(x)==cislo:
		#print(sum(x),i,cislo)
		podminka=False
	else:
		i+=1"""
x=findWeakness(0)
print(max(x)+min(x))

