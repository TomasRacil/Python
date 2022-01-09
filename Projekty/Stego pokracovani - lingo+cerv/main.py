from moduls.encode import *
from moduls.decode import *
import sys

def main():
	"""Function dealing with user input"""
	if ((len(sys.argv) == 2) and (sys.argv[1] == "--help") or (len(sys.argv) == 1)):	
		print("\n Syntax: *.py <mode> <input file> <output file>\n -e\tEncode\n -d\tDecode")
		go_on = False
	else: 
		go_on = True

	
	
	while (go_on):
		#switch = input("(1)Encode\n(2)Decode\n(-)End program\nYour choice: ")
		try:
			if (int(switch) == 1): #Encode
				input_image = input("Select target image: ")
				input_message = input("Message to encode: ")
				preEncode(openImage(input_image), input_message)
			elif (int(switch) == 2): #Decode
				input_image = input("Select image to decode: ")
				print("Message: " + decode(openImage(input_image)) + "\n")
			else:
				go_on = False
		except:
			go_on = False
			print("\nSomething's wrong!")
	
	print("\nGoodbye for now!") #End of program

main()
