import argparse
from random import randint

parser = argparse.ArgumentParser(description='Rozmezí generovaného čísla')
parser.add_argument('-min', metavar='min', type=int, default="nic nebylo předáno", help='Zde zadejte nejmenší hodnotu')
parser.add_argument('-max', metavar='max', type=int, default="nic nebylo předáno", help='Zde zadejte největší hodnotu')
args = parser.parse_args()


min=(args.min)
max=(args.max)
hadanecislo=randint(min, max)
print(hadanecislo)
podminka=True
while podminka:
	podminka=input("Zadejte cislo:  ")!=str(hadanecislo)