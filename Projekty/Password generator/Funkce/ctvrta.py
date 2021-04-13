import string
import random



def fetch_string_constant(choice_list):
	'''
	Vrátí konstantu řetězce na základě uživatelů choice_list.
    řetězcová konstanta může být buď číslice, písmena, interpunkce nebo
    jejich kombinace.f
	'''
	string_constant = ''

	string_constant += NUMBERS if choice_list[0] else ''
	string_constant += LETTERS if choice_list[1] else ''
	string_constant += PUNCTUATION if choice_list[2] else ''
	
	return string_constant