import re,regex

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

def openAndSplit(path="messages.txt"):
	"""Open split and fomat data

	Function to split data in form of txt into required chunks.
	
	Args:
		path (string): path to txt file with data (default 'tickets.txt')

	Returns:
		dict: return dictionary of rules name of the rule as key and list of list of ints representing posible rules
		list: list of stings representing messages
	"""

	file=open(path,"r").read().split("\n\n")
	rules={int(line.split(":")[0].strip()):[moznost.split() for moznost in line.split(":")[1].replace('"','').split("|")] for line in file[0].split("\n")}
	messages=[line.strip() for line in file[1].split("\n")]
	return rules,messages

def makePatern(rules,rule,variant=0):
	"""
	"""
	if rules[rule][0][0].isalpha():
		return rules[rule][0][0]
	else:
		pattern=""
		if len(rules[rule])==1:
			if rule==11 and variant==1:
				firstpart,secondpart=makePatern(rules,int(rules[rule][0][0]),variant),makePatern(rules,int(rules[rule][0][1]),variant)
				patern=f"({firstpart}(?1){secondpart}|(?<={firstpart})(?={secondpart}))"
			else: patern="".join([makePatern(rules,int(rules[rule][0][i]),variant) for i in range(len(rules[rule][0]))])
		else:
			firstpart="".join([makePatern(rules,int(rules[rule][0][i]),variant) for i in range(len(rules[rule][0]))])
			secondpart="".join([makePatern(rules,int(rules[rule][1][i]),variant) for i in range(len(rules[rule][1]))])
			firstpart= f"(?:{firstpart})" if len(firstpart)>1 else firstpart
			secondpart= f"(?:{secondpart})" if len(secondpart)>1 else secondpart
			patern=f"(?:{firstpart}|{secondpart})"
		if rule==8 and variant==1: patern+="+?"
		return patern

def countValid(messages,patern):
	"""Count valid messages

	This function loop through messages and count messages that match regex espression.
	
	Args:
		messages (list): list of string containing messages
		patern: regex patter to aply on messages

	Returns:
		int: return number of messages matching regex pattern

	"""
	count=0
	for message in messages:
		if regex.match(patern,message): count+=1
	return count

def main():
	rules,messages=openAndSplit("messages.txt")
	#showDict(rules)
	#showList(messages)
	patern=f"^{makePatern(rules,0)}$"
	print(f"Počet platných zpráv bez úpravy pravidla 11: {countValid(messages,patern)}")
	patern=f"^{makePatern(rules,0,1)}$"
	print(f"Počet platných zpráv po úpravě pravidla 11: {countValid(messages,patern)}")

if __name__=="__main__":
	main()