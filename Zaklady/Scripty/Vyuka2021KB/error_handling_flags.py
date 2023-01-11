from argparse import ArgumentParser

parser = ArgumentParser(description='Program pro deleni dvou cisel')

parser.add_argument('-x', type=int, help='Dělené číslo')
parser.add_argument('-y', type=int, help='Dělitel')

args = parser.parse_args()


# x=input("cislo jedna (od 0 do 10):")
# y=input("cislo dva (od 0 do 10):")

x=args.x
y=args.y

try:
    
    # x=int(x)
    # y=int(y)
    if x>10  or x<0 or y>10 or y<0:
        raise ValueError
    print(x/y)
    
except ZeroDivisionError:
    print("Dělení nulou není možné")

except ValueError:
    print("Musite zadat platná čisla")

except TypeError:
    print("Musite zadat hodnoty")