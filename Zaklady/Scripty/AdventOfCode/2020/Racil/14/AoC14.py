import re
import functools

def showList(lis):
	for prvek in lis: 
		print(prvek[0])
		for prvek in prvek[1]: print(prvek)
		print()

def aplyMaskOnValue(dockingCommands):
	memory=dict()
	for mask, commands in dockingCommands:
		for mem, value in commands:
			cislo=[]
			for index,char in enumerate(mask):
				if char!="X":cislo.append(char)
				else: cislo.append(value[index])
			memory[mem]=int("".join(cislo),2)
	return memory

#@functools.lru_cache(maxsize=100000)
def variants(binary):
	binList=list(binary)
	try:
		index=binList.index("X")
		helper=[]
		for variant in variants("".join(binList[index+1:])):
			helper.append("".join(binList[:index]+["0"]+[variant]))
			helper.append("".join(binList[:index]+["1"]+[variant]))
		return helper
		#return ["".join(binList[:index]+["0"]+[variant]) for variant in variants(binList[index+1:])]+["".join(binList[:index]+["1"]+[variant]) for variant in variants(binList[index+1:])]
	except:	return ["".join(binList)]

def listOfBinToInt(binList):
	return [int(binary,2)for binary in binList]

def aplyMaskOnMem(dockingCommands):
	memory=dict()
	for mask, commands in dockingCommands:
		for mem, value in commands:
			adress=[]
			for index,char in enumerate(mask):
				if char=="X": adress.append(char)
				elif char=="0": adress.append(mem[index])
				else: adress.append(char)
			for adress in listOfBinToInt(variants("".join(adress))):
				memory[adress]=int(value)
	return memory

def first():
	docking=[[group.split("\n")[0],
	[[re.findall(r"[0-9]+",command)[0],
	(36-len(str(bin(int(re.findall(r"[0-9]+",command)[1])))[2:]))*"0" 
	+ str(bin(int(re.findall(r"[0-9]+",command)[1])))[2:]]
	for command in group.strip().split("\n")[1:]]]
	for group in re.split(r'mask = ',open("docking.txt","r").read().strip())[1:]]

	return sum(aplyMaskOnValue(docking).values())

def second():
	docking=[[group.split("\n")[0],
	[[(36-len(str(bin(int(re.findall(r"[0-9]+",command)[0])))[2:]))*"0" 
	+ str(bin(int(re.findall(r"[0-9]+",command)[0])))[2:],
	re.findall(r"[0-9]+",command)[1],]
	for command in group.strip().split("\n")[1:]]]
	for group in re.split(r'mask = ',open("docking.txt","r").read().strip())[1:]]

	return sum(aplyMaskOnMem(docking).values())



#first()
second()

