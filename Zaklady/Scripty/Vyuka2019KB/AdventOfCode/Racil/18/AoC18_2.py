"""
Script, který řeší výrazy uvedené v textovém souboru math.txt zapíše je do listu a nakonec je všechny sečte.
V první variantě nemají operátory žádnou přednost tedy řešení probíhá zleva doprava. Vyjímkou jsou závorky ty mají prioritu.
V druhé části mají prioritu závorky a znaménko plus právě v tomto pořadí.
"""

#Správné odpověďi: 	1: 	21022630974613                                                                                                                                                   
#				 	2:	169899524778212

def solveL2R(expression):
	"""Solve left to right
	Solving expression from left to right(no operators preference).
	
	Args:
		expression (list): expresion in form of list of characters; allowed char: + * [0-9]+

	Returns:
		integer: return solved expresion in form of one integer
	"""

	value,operator=0,"+"
	for char in expression:
		if char.isdigit(): value = value+int(char) if operator == "+" else value*int(char)
		else: operator = char
	return value

def add(expression):
	"""Add in expression
	Solving all addition in expression from left to right.
	
	Args:
		expression (list): expresion in form of list of characters; allowed char: + * [0-9]+

	Returns:
		integer: return expression with all addition done
	"""

	while "+" in expression:
		plusIndex=expression.index("+")
		value=int(expression[plusIndex-1])+int(expression[plusIndex+1])
		expression=expression[:plusIndex-1]+[value]+expression[plusIndex+2:]
	return expression

def multiply(expression):
	"""Multiply in expression
	Solving all multiplication in expression from left to right.
	
	Args:
		expression (list): expresion in form of list of characters; allowed char: + * [0-9]+

	Returns:
		integer: return expression with all multiplication done
	"""

	while "*" in expression:
		starIdex=expression.index("*")
		value=int(expression[starIdex-1])*int(expression[starIdex+1])
		expression=expression[:starIdex-1]+[value]+expression[starIdex+2:]
	return expression

def count(expression):
	"""Solve left to right
	Solve whole expression left to right (no operator priority except parenthessis) 
	by firsty solving expressions in parenthessis and replacing them with their value.
	Then solve whole expression. It uses L2R function for solving expression without parenthessis
	
	Args:
		expression (list): expresion in form of list of characters; allowed char: + * [0-9]+

	Returns:
		integer: return solved expression
	"""

	while "(" in expression:
		sectionEnd=expression.index(")")
		sectionBeginning=len(expression[:sectionEnd])-expression[:sectionEnd][::-1].index("(")
		section=expression[sectionBeginning:sectionEnd]
		expression = expression[:sectionBeginning-1]+[str(solveL2R(section))]+expression[sectionEnd+1:]
	return solveL2R(expression)

def count2(expression):
	"""Solve addition priority
	Solve whole expression parenthessis and addition priority (in this order)
	by firsty solving expressions in parenthessis and replacing them with their value.
	Then solve whole expression. It uses add and multiply functions for solving expression without parenthessis
	
	Args:
		expression (list): expresion in form of list of characters; allowed char: + * [0-9]+

	Returns:
		integer: return solved expression
	"""

	while "(" in expression:
		sectionEnd=expression.index(")")
		sectionBeginning=len(expression[:sectionEnd])-expression[:sectionEnd][::-1].index("(")
		section=expression[sectionBeginning:sectionEnd]
		section=add(section)
		section=multiply(section)
		expression = expression[:sectionBeginning-1]+section+expression[sectionEnd+1:]
	expression=add(expression)
	expression=multiply(expression)
	return int(expression[0])

def main():
	#priklady=[line.strip().replace(" ","") for line in open("math.txt","r")]
	solved1=[count(list(line.strip().replace(" ",""))) for line in open("math.txt","r")]
	solved2=[count2(list(line.strip().replace(" ",""))) for line in open("math.txt","r")]
	print(sum(solved1))
	print(sum(solved2))

if __name__=="__main__":
	main()