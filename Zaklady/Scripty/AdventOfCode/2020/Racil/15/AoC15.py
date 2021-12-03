"""
Tento skript simuluje paměťovou hru. Začínáme se seznamem čísel startList. Tento seznam budeme v každém kole rozšiřovat.
Další číslo na seznamu musí dodržet následující pravidla.
Pokud posldení číslo ještě v seznamu není přidáme do seznamu číslo 0.
Pokud poslední číslo již v seznamu je přidáme do seznamu číslo rovanjící se počtu kol které uplynuly od posledního výskytu.
Cílem je nalézt poslední číslo v 2020 kolech a 30000000 kolech.
"""

#Správné odpovědi:	1. 763
#					2. 1876406 

def play(startList,rounds):
	"""Play memory game

	Function which every round append number to the end of the list based on two rules.
		if last number is not in list append 0
		if last number is in list append number of rouds passed form time when it was last added
	
	Args:
		startList (list): list of starting values
		rounds (int): number of rounds to be done

	Returns:
		int: last number added
	"""
	numbers=startList.copy()
	while True:
		if numbers[-1] not in numbers[:-1]: numbers.append(0)
		else: numbers.append(numbers[::-1][1:].index(numbers[-1])+1)
		if len(numbers)==rounds: return(numbers[-1])

def playUpgraded(startList,rounds):
	"""Play memory game upgraded

	Function which every round append number to the end of the list based on two rules.
		if last number is not in list append 0
		if last number is in list append number of rouds passed form time when it was last added
	This one is modified for solving larger numbers of rounds
	
	Args:
		startList (list): list of starting values
		rounds (int): number of rounds to be done

	Returns:
		int: last number added
	"""
	numbers={number:index for index,number in enumerate(startList[:-1])}
	index,last=len(startList[:-1]), startList[-1]
	while True:
		if last not in numbers: numbers[last],last=index, 0
		else: numbers[last],last=index,index-numbers[last]
		index+=1
		if index==rounds-1: return(last)

def main():
	startList=[0,14,1,3,7,9]
	print(f"Poslední číslo v 2020 kolech: {play(startList,2020)}")
	#print(play(startList,30000000))
	#print(playUpgraded(startList,2020))
	print(f"Poslední číslo v 30000000 kolech: {playUpgraded(startList,30000000)}")

if __name__=="__main__":
	main()