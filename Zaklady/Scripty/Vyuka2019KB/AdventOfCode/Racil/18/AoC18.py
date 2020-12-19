"""
Následdujícím způsobem by to sice bylo možné řešit, ale je zbytečně komplikovaný a člověk se v něm lehce ztratí.
Je vždy vhodné strávit čas hledáním dobrého řešení a jednoduchého řešení. Na konec to ušetříé hodně času.
Nad tímto problémem jsem stávil zhruba 5 hodin. 
Pro srovnání druhé řešení (AoC18_2.py) jsem měl vyřešeno za zhruba 30 minut.
"""

import re

def showList(shlist):
	for line in shlist:
		print(line)

def count(vyraz):
	#print(vyraz)
	if not "(" in vyraz:
		value,operator=0,"+"
		for char in vyraz:
			if char.isdigit():value= value+ int(char) if operator=="+" else value*int(char)
			else:operator=char
		return value
	else:
		value,operator,parenthesis,inParenthesis=0,"+",[[],[]],False
		for index,char in enumerate(vyraz):
			if char.isdigit() and not inParenthesis: value= value+ int(char) if operator=="+" else value*int(char)
			elif char=="(":
				parenthesis[0].append(index)
				inParenthesis=True
			elif char==")":
				parenthesis[1].append(index)
				if len(parenthesis[1]) ==len(parenthesis[0]):
					value = value+count(vyraz[parenthesis[0][0]+1:parenthesis[1][-1]]) if operator=="+" else value*count(vyraz[parenthesis[0][0]+1:parenthesis[1][-1]])
					parenthesis,inParenthesis=[[],[]],False
			if not inParenthesis: operator=char
		return value
def addParenthesis(vyraz):
	print("Vstup: ",vyraz)
	vyraz=list(vyraz)
	if not "(" in vyraz:
		vyraz2=[]
		opened=None
		for index,char in enumerate(vyraz):
			try:
				if (vyraz[index-1]=="*" or vyraz[index-1].isdigit()) and vyraz[index+1]=="+":
					vyraz2.extend(["(",char])
					opened=True
				elif vyraz[index-1]=="+" and vyraz[index+1]=="*":
					vyraz2.extend([char,")"])
					opened=False
				else:vyraz2.append(char)
			except:
				if opened: vyraz2.extend([char,")"])
				else: vyraz2.append(char)
		print("".join(["("]+vyraz2+[")"]))
		return "".join(["("]+vyraz2+[")"])
	else:
		parenthesis,opened,inParenthesis,vyraz2=[[],[]],[],False,[]
		for index,char in enumerate(vyraz):
			#print(char)
			try:
				#print(vyraz[index-1]=="*" and vyraz[index+1]=="+" and not inParenthesis,vyraz[index-1]=="+" and vyraz[index+1]=="*" and not inParenthesis,char=="(",char==")",not inParenthesis)
				if (vyraz[index-1]=="*" or (index-1<0)) and vyraz[index+1]=="+" and not inParenthesis:
					vyraz2.extend(["(",char])
					opened=True
				elif vyraz[index-1]=="+" and vyraz[index+1]=="*" and not inParenthesis:
					vyraz2.extend([char,")"])
					opened=False
				elif char=="(":
					parenthesis[0].append(index)
					inParenthesis=True
				elif char==")":
					parenthesis[1].append(index)
					if len(parenthesis[1]) ==len(parenthesis[0]):
						try:
							if vyraz[index+1]=="+":
								vyraz2.append("(")
								opened=True
						except Exception as e:
							#print(e)
							pass
						vyraz2.append(addParenthesis("".join(vyraz[parenthesis[0][0]+1:parenthesis[1][-1]])))
						parenthesis,inParenthesis=[[],[]],False
				elif not inParenthesis: vyraz2.append(char)
			except:
				if opened: 
					vyraz2.extend([char,")"])
					opened=False
				else: vyraz2.append(char)
		if opened:
			vyraz2.extend([")"])
			opened=False
		print("".join(["("]+vyraz2+[")"]))
		return "".join(["("]+vyraz2+[")"])

priklady=[line.strip().replace(" ","") for line in open("math.txt","r")]
#priklady=[count(line.strip().replace(" ","")) for line in open("math.txt","r")]
#priklady=[count(addParenthesis(line.strip().replace(" ",""))) for line in open("math.txt","r")]

test0='2*2+3+4+4*3'
test1='1+(2*3)+(4*(5+6))'
test2='2*3+(4*5)'
test3='5+(8*3+9+3*4*3)'
test4='5*9*(7*3*3+9*3+(8+6*4))'
test5='((2+4*9)*(6+9*8+6)+6)+2+4*2'
test6='(2+4*9)*(6+9*8+6)+6'
#print(sum(priklady))
print(priklady[15])
print(count(addParenthesis(priklady[15])))
print(count('((7+(((3+8+2+5))*2)*(5+4)))'))
#showList(priklady)

"""parenthesis,inParenthesis=[[],[]],False

test=test6
for index, char in enumerate(test):
	#print(parenthesis)
	if char=="(":
		parenthesis[0].append(index)
		inParenthesis=True
	elif char==")":
		parenthesis[1].append(index)
		if len(parenthesis[1]) == len(parenthesis[0]):
			print(test[parenthesis[0][0]+1:parenthesis[1][-1]])
			parenthesis,inParenthesis=[[],[]],False
	elif char in ["+","*"] and not inParenthesis:
		print(char)"""
