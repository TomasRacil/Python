import argparse

from zdeJeProgramovaLogika import *

def parseArgumets():
	parser = argparse.ArgumentParser(description='Argumenty předáváme pomocí -přikaz')
	parser.add_argument('-z', metavar='zpráva', type=str, default="nic nebylo předáno", help='Zde zadejte zprávu která má být předána programu')
	return parser.parse_args()

if __name__ == '__main__':
    #args = parse_arguments()
    print(parseArgumets().z)
    run()