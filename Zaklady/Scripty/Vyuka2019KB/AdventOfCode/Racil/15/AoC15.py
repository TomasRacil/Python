def game(startList,rounds):
	numbers=startList.copy()
	while True:
		if numbers[-1] not in numbers[:-1]: numbers.append(0)
		else: numbers.append(numbers[::-1][1:].index(numbers[-1])+1)
		if len(numbers)==rounds: return(numbers[-1])

def gameUpgraded(startList,rounds):
	numbers={number:index for index,number in enumerate(startList[:-1])}
	index,last=len(startList[:-1]), startList[-1]
	while True:
		if last not in numbers: numbers[last],last=index, 0
		else: numbers[last],last=index,index-numbers[last]
		index+=1
		if index==rounds-1: return(last)

startList=[0,14,1,3,7,9]
#print(game(startList,2020))
#print(game(startList,30000000))
#print(gameUpgraded(startList,2020))
#print(gameUpgraded(startList,30000000))