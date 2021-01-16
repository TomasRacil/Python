from Zdroj.Pracespolem import *
from Zdroj.Grafika import *
from Zdroj.Argument import *
import argparse

def main():
    #print(praceBod.__doc__ + '\n')
    praceBod(bod,2)

    #print(vymazBod.__doc__ + '\n')
    vymazBod(bod, argument())

    #print(drawbod.__doc__ + '\n')
    drawbod(bod)

    #print(konzole.__doc__ + '\n')
    konzole(bod)

if __name__ == '__main__':
    main()