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
	"""
	Returns a list with rgb values of three pixels and a new pointer
	Args:
		data (list): list of image values, rgb in tuples representing pixels
		pointer (pointer): points to the beginning of pixels to read next
	Returns:
		three_pixels (list): list of nine rgb values
		pointer (pointer): points behind the read pixels
	"""
	three_pixels = []
	for pixel in range(3):
		for rgb in range(3):
			three_pixels.append(data[pointer+pixel][rgb]) #Creates a list of rgb values, nine in total
	return three_pixels, pointer + 3

def alterPixels(image, x, y, new_pixel, image_width):
	"""
	Inserts three altered pixels into image, returns pointer to unaltered pixel
	Args:
		image (pointer): points to altered image (result of encode)
		x, y (int): position of pixel (pixel is a tuple of rgb values)
		new_pixel (tuple): altered pixel to insert into image
		image_width (int): image width, for keeping track of pixel lines
	Returns:
		x, y (int): position of next pixel to alter
	"""
	for pixel in range(3):
		image.putpixel((x, y), tuple(new_pixel[0:3]))
		del new_pixel[0:3]
		if (x == image_width - 1):
			x = 0
			y += 1
		else:
			x += 1
	return x, y
