from PIL import Image #Module for image manipulation
from .shared_functions import *

def encodeCore(three_pixels, bit_character):
	"""
	Returns a list of three altered pixel rgb values, nine values in total
	Args:
		three_pixels (list): pixels to alter
		bit_character (string): binary value of character to encode
	Returns:
		new_pixels (list): pixels with encoded character
	"""
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
	old_image_data = list(image.getdata()) #problem 1
	if (len(old_image_data) > (len(message)*3)):
		new_image = image.copy()
		image.close()
		encode(old_image_data, new_image, message)
	else:
		image.close()
		print("Not enought target space! Aborting...\n")

def encode(pixel_list, new_image, message):
	"""
	Encodes text into image
	Args:
		pixel_list (list): image values converted into list, contains whole image
		new_image (pointer): pointer to image to be altered
		message (string): message to encode
	"""
	width = new_image.size[0]
	pixel_pointer = 0
	x, y = 0, 0 #Location of pixel being altered
	for character in message:
		three_pixels, pixel_pointer = loadThreePixels(pixel_list, pixel_pointer)
		if (len(message) * 3 > pixel_pointer + 1):
			bit_character = list(textToBinary(character) + '0')
		else:
			bit_character = list(textToBinary(character) + '1') #Appends odd number if no more characters are left, end condition
		new_pixel = encodeCore(three_pixels, bit_character) #Core of encoding
		x, y = alterPixels(new_image, x, y, new_pixel, width) #Inserts altered pixels into new image
	postEncode(new_image)

def postEncode(altered_image):
	"""Saves altered image"""
	image_name = input("Name of new image [with extension]: ")
	altered_image.save(image_name, str(image_name.split(".")[1].upper()))
	print("Done encoding...\n")
