import string
import random


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