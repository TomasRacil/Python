import argparse

parser = argparse.ArgumentParser(description='Ukázka předávání argumentů.')
parser.add_argument('jmeno', type=str, help='Jméno uživatele.')
parser.add_argument('-v', '--vek', type=int, default=18, help='Věk uživatele.')

args = parser.parse_args()

print(f"Jméno: {args.jmeno}")
print(f"Věk: {args.vek}")