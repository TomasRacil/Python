from moduls.encode import *
from moduls.decode import *
import sys

def check(i):
	if (i[-4:] != ".png"):
		print("\nUnsupported file format!")
		exit()


def main():
	outfname = "out.png"
	"""Function dealing with user input"""
	if ((len(sys.argv) == 2) and (sys.argv[1] == "--help") or (len(sys.argv) == 1)):	
		print("\n Syntax: *.py <mode> <input file> <input text> <output file>\n -e\tEncode\n -d\tDecode")
		exit()
	try:
		if (sys.argv[1] == "-e"): 
			switch = 1
			input_image = sys.argv[2]
			input_message = sys.argv[3]
			if (len(sys.argv) == 5):
				outfname = sys.argv[4]
			else:
				print("No output filename given, defaulting to out.<format>!")
		if (sys.argv[1] == "-d"): switch = 2		
		input_image = sys.argv[2]
	except:
		print("Syntax error!")
		exit()

	check(input_image)
	img = openImage(input_image)

#try:
	if (int(switch) == 1): #Encode

		preEncode(img, input_message, outfname) #Mozny problem
	elif (int(switch) == 2): #Decode

		print("Message: " + decode(img) + "\n")
	else:
		print("Error in command parsing!")
		exit()

#except:
#		print("\nSomething's wrong!")
#		exit()
	
	print("\nGoodbye for now!") #End of program

main()
