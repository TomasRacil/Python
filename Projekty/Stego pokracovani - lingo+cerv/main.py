from moduls.encode import *
from moduls.decode import *
import sys

def check(i):
	if (i[-4:] != ".png"):
		print("\nUnsupported file format!")
		exit()


def main():
	"""Function dealing with user input"""
	if ((len(sys.argv) == 2) and (sys.argv[1] == "--help") or (len(sys.argv) == 1)):	
		print("\n Syntax: *.py <mode> <input file> <input text>\n -e\tEncode\n -d\tDecode")
		exit()
	try:
		if (sys.argv[1] == "-e"): 
			switch = 1
			input_message = sys.argv[3]
		if (sys.argv[1] == "-d"): switch = 2		
		input_image = sys.argv[2]
	except:
		print("Syntax error!")
		exit()
	check(input_image)
	go_on = True
	while (go_on):
		#switch = input("(1)Encode\n(2)Decode\n(-)End program\nYour choice: ")
		try:
			if (int(switch) == 1): #Encode
				#input_image = input("Select target image: ")
				#input_message = input("Message to encode: ")
				preEncode(openImage(input_image), input_message)
			elif (int(switch) == 2): #Decode
				#input_image = input("Select image to decode: ")
				print("Message: " + decode(openImage(input_image)) + "\n")
			else:
				go_on = False
		except:
			go_on = False
			print("\nSomething's wrong!")
			exit()
	
	print("\nGoodbye for now!") #End of program

main()