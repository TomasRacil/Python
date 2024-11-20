integer: int = 1
print(f"hodnota {integer} typ {type(integer)}")

binary: bin = 0b10  # Binární číslo
print(f"hodnota {binary} typ {type(binary)}")

octal = 0o10  # Osmičkové číslo
print(f"hodnota {octal} typ {type(octal)}")

hexadecimal = 0x10  # Šestnáctkové číslo
print(f"hodnota {hexadecimal} typ {type(hexadecimal)}")

floatingPointNumber = 2.58
print(f"hodnota {floatingPointNumber} typ {type(floatingPointNumber)}")

floatingPointNumber = 4.2e-4  # Vědecký zápis
print(f"hodnota {floatingPointNumber} typ {type(floatingPointNumber)}")

complexNumber = 2 + 3j
print(f"hodnota {complexNumber} typ {type(complexNumber)}")

text1: str = "Ahoj "
text2: str = 'světe!'
print(f"hodnoty: {text1}, {text2} typ {type(text1)}, {type(text2)}")

text3: str = """
Mezi trojící uvozovek je text ukládán
ve stejném formátu jako byl napsán
včetně řádků 
  a odstavců
"""
print(f"hodnota: {text3} typ {type(text3)}")

boolean: bool = True
print(f"hodnota {boolean} typ {type(boolean)}")

pozdrav, poradi = 'Zdravím', '3'

formatovanyText1 = "%s. Toto je %s. lekce" % (pozdrav, poradi)
print(formatovanyText1)

formatovanyText2 = "{1}. Toto je {0}. lekce".format(poradi, pozdrav)
print(formatovanyText2)

formatovanyText3 = f"{pozdrav}. Toto je {poradi}. lekce"
print(formatovanyText3)

print('\n "Naučila jsem se, že cesta pokroku není rychlá ani snadná." \n \t— Marie Curie-Skłodowská\n')
print("Například jednu uvozovku: \", \nnebo znak pro nový rádek je \\n\n")

text = "Ukázkový text pro potřeby indexace a iterace\n"
print(text)
print(f'Symbol na druhém místě je {text[2]}\n')  # Indexování začíná od 0
print(f'Symbol na druhém místě od konce je {text[-2]}\n')  # Záporné indexování
print(f'Symboly od 8 znaku do 8 znaku před koncem  {text[8:-8]}\n')  # Slicing

for znak in text:
    print(znak)

print(f'Délka řetězce:  {len(text)}\n')
print(f'Text malými písmeny:  {text.lower()}\n')
print(f'Text kapitálky:  {text.upper()}\n')
print(f'Změna prvního slova:  {text.replace("Ukázkový", "Vzorový")}\n')
print(f'Rozdělení podle mezer:  {text.split(" ")}\n')

zbytecneMocPomlcek = '-------text------'
print(f'Bez pomlcek: {zbytecneMocPomlcek.strip("-")}\n')

print(f'Index prvního ř:  {text.find("ř")}\n')
print(f'Počet znaků a:  {text.count("a")}\n')

programovaciJazyky = ['Python', 'Kotlin', 'Go']
print(f'Převedení seznamu do stringu: {", ".join(programovaciJazyky)}')

string = '5'
print(f'1. Hodnota {string} typ {type(string)}\n')

cislo = int(string)  # Převod string na int
print(f'2. Hodnota {cislo} typ {type(cislo)}\n')

desetineCislo = 5.5
print(f'3. Hodnota {desetineCislo} typ {type(desetineCislo)}\n')

cislo = int(desetineCislo)  # Převod float na int (ztráta desetinné části)
print(f'4. Hodnota {cislo} typ {type(cislo)}\n')

desetineCislo = float(cislo)  # Převod int na float
print(f'5. Hodnota {desetineCislo} typ {type(desetineCislo)}\n')

desetineCislo = float(string)  # Převod string na float
print(f'6. Hodnota {desetineCislo} typ {type(desetineCislo)}\n')

string = str(cislo)  # Převod int na string
print(f'7. Hodnota {string} typ {type(string)}\n')

string = str(string)  # Převod string na string (beze změny)
print(f'8. Hodnota {string} typ {type(string)}\n')