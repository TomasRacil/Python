from PIL import Image #Module for image manipulation
from .shared_functions import *

def decode(image):
	"""
	Decodes text from image
	Args:
		image (pointer): points to opened image
	Returns:
		(string): decoded message
	"""
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
