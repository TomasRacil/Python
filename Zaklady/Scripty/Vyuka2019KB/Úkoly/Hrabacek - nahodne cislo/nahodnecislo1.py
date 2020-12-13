import argparse
from random import randint

parser = argparse.ArgumentParser(description='Rozmezí generovaného čísla')
parser.add_argument('-min', metavar='min', type=int, default=0, help='Zde zadejte nejmenší hodnotu')
parser.add_argument('-max', metavar='max', type=int, default=10, help='Zde zadejte největší hodnotu')
args = parser.parse_args()

min=(args.min)
max=(args.max)

hadanecislo=randint(min, max)

podminka=True
while podminka:
	cislo=input("Zadejte čislo:  ")
	if int(cislo)<int(hadanecislo):
		print("Hádané číslo je větší")
	elif int(cislo)>int(hadanecislo):
		print("Hádané číslo je menší")	

	podminka=cislo!=str(hadanecislo)
