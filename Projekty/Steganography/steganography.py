"""
Python implementation of Steganography
Author: Josef Němec
Date of birth: December 2020
Update (author, date): None
"""

from PIL import Image #Module for image manipulation

def openImage(image_name):
	"""Returns pointer to readable image"""
	return Image.open(image_name, 'r')

def textToBinary(text):
	"""Rewrites text message into binary values"""
	return ''.join([format(ord(i), "08b") for i in text])

def binaryToText(binary):
	"""Converts binary representation of characters into string"""
	return ''.join(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)//8))

def loadThreePixels(data, pointer):
	"""Returns a list with rgb values of three pixels and a new pointer"""
	three_pixels = []
	for pixel in range(3):
		for rgb in range(3):
			three_pixels.append(data[pointer+pixel][rgb]) #Creates a list of rgb values, nine in total
	return three_pixels, pointer + 3

def alterPixels(image, x, y, new_pixel, image_width):
	"""Inserts three altered pixels into image, returns pointer to unaltered pixel"""
	for pixel in range(3):
		image.putpixel((x, y), tuple(new_pixel[0:3]))
		del new_pixel[0:3]
		if (x == image_width - 1):
			x = 0
			y += 1
		else:
			x += 1
	return x, y

def encodingCore(three_pixels, bit_character):
	"""Returns a list of three altered pixel rgb values, nine values in total"""
	bit = 0
	new_pixels = []
	for rgb in three_pixels:
		if (int(bit_character[bit]) % 2 == 0):
			if (rgb % 2 == 1):
				new_pixels.append(rgb - 1)
			else:
				new_pixels.append(rgb)
		else:
			if (rgb % 2 == 0):
				new_pixels.append(rgb + 1)
			else:
				new_pixels.append(rgb)
		bit += 1
	return new_pixels

def preEncode(image, message):
	"""Checks if target is big enought to encode to"""
	old_image_data = list(image.getdata())
	if (len(old_image_data) > (len(message)*3)):
		new_image = image.copy()
		image.close()
		encode(old_image_data, new_image, message)
	else:
		image.close()
		print("Not enought target space! Aborting...\n")

def encode(pixel_list, new_image, message):
	"""Encodes text into image"""
	width = new_image.size[0]
	pixel_pointer = 0
	x, y = 0, 0 #Location of pixel being altered
	for character in message:
		three_pixels, pixel_pointer = loadThreePixels(pixel_list, pixel_pointer)
		if (len(message) * 3 > pixel_pointer + 1):
			bit_character = list(textToBinary(character) + '0')
		else:
			bit_character = list(textToBinary(character) + '1') #Appends odd number if no more characters are left, end condition
		new_pixel = encodingCore(three_pixels, bit_character) #Core of encoding
		x, y = alterPixels(new_image, x, y, new_pixel, width) #Inserts altered pixels into new image
	postEncoding(new_image)

def postEncoding(altered_image):
	"""Saves altered image"""
	image_name = input("Name of new image [with extension]: ")
	altered_image.save(image_name, str(image_name.split(".")[1].upper()))
	print("Done encoding...\n")

def decode(image):
	"""Decodes text from image"""
	pixel_list = list(image.getdata())
	image.close()
	pixel_pointer = 0
	binary_message = ""
	try:
		while(True):
			three_pixels, pixel_pointer = loadThreePixels(pixel_list, pixel_pointer)
			for bit in range(8): #Core of decoding
				if (three_pixels[bit] % 2 == 0):
					binary_message += "0"
				else:
					binary_message += "1"
			if (three_pixels[-1] % 2 == 1): #Checks if message is over
				return binaryToText(binary_message)
	except:
		print("Reached end of image! Aborting...")
		return binaryToText(binary_message)
