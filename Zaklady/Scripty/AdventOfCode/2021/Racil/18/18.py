from ast import literal_eval
data=[]

def findDepth(L):
    return isinstance(L, list) and max(map(findDepth, L))+1

with open(r"C:\Vyuka\Python\Zaklady\Scripty\AdventOfCode\2021\Racil\18\test.txt","r") as f:
    data=[literal_eval(line.strip()) for line in f]

fishes=data.pop(0)
depthL=findDepth(fishes)

for line in data:
    depthR=findDepth(line)
    fishes=[fishes,line]
    print(fishes)
    depthL+=1
    depthR+=1
    input((depthL, depthR))
    while depthR>4 or depthL>4:
        pass

print(fishes)