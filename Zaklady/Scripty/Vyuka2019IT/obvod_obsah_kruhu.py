import argparse
from math import pi

parser = argparse.ArgumentParser(description='Program pro vypocet obvodu a obsahu kruhu')

parser.add_argument('-r', metavar='--polomer', type=int, help='Zde zadejte polomer kruhu pro vypocet')
parser.add_argument('-v',metavar="--varianta",type=str, default='F', help="Varianta vypoctu O- obvod, S-obsah")

args = parser.parse_args()
try:
    if args.v =='O':
        print(2*pi*args.r)
    elif args.v =='S':
        print(pi*(args.r**2))
    else:
        raise ValueError
except Exception as e:
    print(e.__doc__)