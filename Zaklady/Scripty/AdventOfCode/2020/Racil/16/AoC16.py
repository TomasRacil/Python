"""
Tento skript zpracovává textový soubor skládající se ze tří částí. 
První je seznam pravidel tyto pravidla nám říkají v jakém rozsahu hodnot se pohybují jednotlivé informace.
Druhý je naše jízdenka. Třetím jsou jízdenky ostatních pasažérů.
V tomto textovém souboru prvně nalezneme všechny neplatné jízdenky tedy jízdenky, které obsahují hodnotu/hodnoty
nesplňující žádné pravidlo. V druhé části pracujeme pouze s platnými jízdenkami a zjišťujeme co jednotlivé hodnoty 
znamenají. Například na kterém indexu jízdenky je uvedeno sedadlo.
"""

#Správné odpovědi:	1. 20058
#					2. 366871907221 

import math

def openAndSplit(path="tickets.txt"):
	"""Open split and fomat data

	Function to split data in form of txt into required chunks.
	
	Args:
		path (string): path to txt file with data (default 'tickets.txt')

	Returns:
		dict: return dictionary of rules name of the rule as key and list of list of ints representing ranges as value
		list: list of ints representing our tickets and int values
		list: list of tickets containing list of ints reprsenting values
	"""

	file=open(path,"r").read().split("\n\n")
	rules={rule.split(":")[0]:[[int(cislo)for cislo in rozsah.split("-")] for rozsah in rule.split(":")[1].split("or")] for rule in file[0].split("\n")}
	yourTickets=[int(cislo.strip()) for cislo in file[1].split("\n")[1].split(",")]
	nearbyTickets=[[int(cislo) for cislo in line.split(",")] for line in file[2].split("\n")[1:]]
	return rules,yourTickets,nearbyTickets


def showDict(dictionary):
	"""Show dictionary

	Function to print out dictionary in form of keys and values printed out on separeted lines.
	
	Args:
		dictionary (dict)
	"""

	for key,value in dictionary.items():
		print(key,value)

def showList(listOfItems):
	"""Show list

	Function to print out dictionary in form of items printed out on separeted lines.
	
	Args:
		ListOfItems (list)
	"""

	for item in listOfItems:
		print(item)

def validate(rules,tickets):
	"""Validate tickets
	
	This function find out valid tickets and return them and also return list of invalid values in invalid tickets.
	
	Args:
		rules (dict): rules for ticket fields in form of dictionary key-field value ranges
		tickets (list): list of tickets containing values of those tickets

	Returns:
		list: return list of valid tickets
		list: return list of invalid values in ivalid tickets
	"""

	validTickets,invalidNumbers=[],[]
	for jizdenka in tickets:
		for cislo in jizdenka:
			valid=False
			for pravidlo in rules.values():
				if pravidlo[0][0]<=cislo<=pravidlo[0][1] or pravidlo[1][0]<=cislo<=pravidlo[1][1]:
					valid=True
					break
			if not valid:
				invalidNumbers.append(cislo)
				break
		if valid: validTickets.append(jizdenka)
	return validTickets,invalidNumbers

def posible(rules,tickets):
	"""Posible fields
	
	This function identify and return all posible indexes for all fields based on their rules.
	
	Args:
		rules (dict): rules for ticket fields in form of dictionary key-field value ranges
		tickets (list): list of tickets containing values of those tickets

	Returns:
		dict: return dict where key is field name and value is list of possible indexes
	"""

	position={key:[]for key in rules}

	for field,rule in rules.items():
		index=0
		while index<len(tickets[0]):
			valid=True
			for ticket in tickets:
				if not (rule[0][0]<=ticket[index]<=rule[0][1] or rule[1][0]<=ticket[index]<=rule[1][1]):
					valid=False
					break
			if valid: position[field].append(index)
			index+=1
	return position

def decide(position):
	"""Identify fields
	
	This function identify corect index for each field based on all posible fields.
	
	Args:
		position (dict): dict where key is field name and value is list of possible indexes

	Returns:
		dict: return dict where key is field name and value is list with only one corect index
	"""

	for key in sorted(position, key=lambda k: len(position[k]), reverse=False):
		#showDict(position)
		#input()
		helper=position[key][0]
		for key,value in position.items():
			if len(value)>1 and helper in value:
				position[key].remove(helper)

	return position

def main():
	rules,yourTickets,nearbyTickets=openAndSplit()

	validTickets,invalidNumbers=validate(rules,nearbyTickets)

	print(f"Součet neplatných hodnot: {sum(invalidNumbers)}")

	validTickets.append(yourTickets)
	position = posible(rules,validTickets)
	position = decide(position)

	depValues=[yourTickets[value[0]] for key,value in position.items() if key.split()[0]=='departure']
	print(f'Násobek všech polí zčínajících departure v naší jízdence: {math.prod(depValues)}')

if __name__=="__main__":
	main()