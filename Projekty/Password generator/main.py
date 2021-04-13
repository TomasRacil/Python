from Funkce.prvni import *
from Funkce.druha import *
from Funkce.treti import *
from Funkce.ctvrta import *

LETTERS = string.ascii_letters
NUMBERS = string.digits  
PUNCTUATION = string.punctuation

if __name__ == '__main__':
	length = get_password_length()
	choice_list = password_combination_choice()
	password = password_generator(choice_list, length)

	print(password)