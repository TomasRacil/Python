"""
Python program implementation of Steganography
Author: Josef Němec
Date of birth: December 2020
"""

#TODO: podminka kdy se nevejde

from PIL import Image #Module for image manipulation

def openPicture(picture_name):
	"""Returns pointer to readable image"""
	return Image.open(picture_name, 'r')

def textToBinary(text):
	"""Rewrites text message into binary values"""
	return ''.join([format(ord(i), "08b") for i in text])

def binaryToText(binary):
	"""Converts binary representation of characters into string"""
	return ''.join(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)//8))

def imageToData(image):
	"""Convertes image into a list of pixel values"""
	tmp = list(image.getdata()) #Creates matrix of image values
	width, height = image.size
	return [tmp[i * width:(i + 1) * width] for i in range(height)] #Rewrites matrix into single line

def encode(picture, message):
	"""Encodes text into picture"""
	changed_picture = picture.copy()
	width = picture.size[0]
	pixels = list(picture.getdata())
	new_pixel = []
	counter = 0 #For tracking number of pixels used
	(x, y) = (0, 0) #Location of pixel being altered
	for character in message:
		three_pixels = []
		for pixel in range(3):
			for rgb in range(3): #Ignores 'a' from rgba
				three_pixels.append(pixels[counter][rgb]) #Creates a list of rgb values, nine in total
			counter += 1
		if (len(message) * 3 > counter + 1):
			bit_character = list(textToBinary(character) + '0')
		else:
			bit_character = list(textToBinary(character) + '1') #Append odd number if no more characters are left, end condition
		bit = 0
		for rgb in three_pixels:
			if (int(bit_character[bit]) % 2 == 0): #Core conditions of steganography
				if (rgb % 2 == 1):
					new_pixel.append(rgb - 1)
				else:
					new_pixel.append(rgb)
			else:
				if (rgb % 2 == 0):
					new_pixel.append(rgb + 1)
				else:
					new_pixel.append(rgb)
			bit += 1
		print(new_pixel)
		for i in range(3): #Puts altered pixels into new image
			changed_picture.putpixel((x, y), tuple(new_pixel[0:3]))
			del new_pixel[0:3]
			if (x == width - 1):
				x = 0
				y += 1
			else:
				x += 1
	changed_picture.save("NaB.png", str("NaB.png".split(".")[1].upper()))

def decode(picture):
	"""Decodes text from picture"""
	pixels = list(picture.getdata())
	BinaryMessage = ""
	counter = 0
	try:
		while(True):
			three_pixels = []
			for pixel in range(3):
				for rgb in range(3): #Ignores 'a' from rgba
					three_pixels.append(pixels[counter][rgb]) #Creates a list of rgb values, nine in total
				counter += 1
			for bit in range(8): #Core of decoding
				if (three_pixels[bit] % 2 == 0):
					BinaryMessage += "0"
				else:
					BinaryMessage += "1"
			if (three_pixels[-1] % 2 == 1): #Checks if message is over
				return binaryToText(BinaryMessage)
	except:
		print("Reached end of image.")
		return binaryToText(BinaryMessage)

def main():
	"""Function dealing with user input"""
	switch = int(input("(1)Encode\n(2)Decode\n(-)End program\nYour choice: "))
	
	if (switch == 1): #Encode
		#input_picture = input("Select target picture: ")
		#input_message = input("Message to encode: ")
		encode(openPicture("test.png"), "Hello") #input_picture, input_message
		
	elif (switch == 2): #Decode
		#input_picture = input("Select suspicious picture: ")
		print("Message: " + decode(openPicture("NaB.png"))) #input_picture
	
	#input_picture.close()
	print("\nGoodbye for now!") #End of program

if __name__ == '__main__' :
	"""Establishes main function as start of the program"""
	main()
