import string
import random


LETTERS = string.ascii_letters
NUMBERS = string.digits  
PUNCTUATION = string.punctuation    


def get_password_length():
	'''
	Vrací délku hesla
	'''
	length = input("Jak dlouhé chceš heslo: ")
	return int(length)


def password_generator(cbl, length=8):
	'''
	Vygeneruje náhodné heslo, které má určitou délku(podle uživatele). Defaultní hodnota je 8 znaků.
	:cbl-> hodnota zadaná uživatelem
        0---> čísla    
             
        1---> písmena   
             
        2 ---> interpunkce
	'''

	printable = fetch_string_constant(cbl)

	# vytvoří seznam a zamíchá
	printable = list(printable)
	random.shuffle(printable)

	# vygeneruje náhodné heslo
	random_password = random.choices(printable, k=length)

	# převede vygenerované heslo na string
	random_password = ''.join(random_password)
	return random_password


def password_combination_choice():
	'''
	Výběr kombinace hesla, heslo může obsahovat čísla, písmena, interpunkci.
	'''

	# načte volbu kombinace hesla
	want_digits = input("Má heslo obsahovat čísla ? (True or False) : ")
	want_letters = input("Má heslo obsahovat písmena ? (True or False): ")
	want_puncts = input("Má heslo obsahovat interpunkci ? (True or False): ")

	# převede volby z řetězce
	try:
		want_digits = eval(want_digits.title())
		want_puncts = eval(want_puncts.title())
		want_letters = eval(want_letters.title())
		return [want_digits, want_letters, want_puncts]

	except NameError as e:
		print("Zadejte True nebo False")
		print("Zkuste zadat hodnoty znovu.")

	return [True, True, True]



def fetch_string_constant(choice_list):
	'''
	Vrátí konstantu řetězce na základě uživatelů choice_list.
    řetězcová konstanta může být buď číslice, písmena, interpunkce nebo
    jejich kombinace.
	'''
	string_constant = ''

	string_constant += NUMBERS if choice_list[0] else ''
	string_constant += LETTERS if choice_list[1] else ''
	string_constant += PUNCTUATION if choice_list[2] else ''
	
	return string_constant



if __name__ == '__main__':
	length = get_password_length()
	choice_list = password_combination_choice()
	password = password_generator(choice_list, length)

	print(password)