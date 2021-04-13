import string
import random




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