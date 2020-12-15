MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', 'Á':'.-', 'Č':'-.-.',
                    'É':'.', 'Í':'..', 'Ů':'..-', 'Ý':'-.--','Š':'...',
                    'Ř':'.-.', 'Ě':'.','Ž':'--..'}

"""MORSE_CODE_DICT = {line.split()[0]:line.split()[1] for line in open("Morse.txt","r")}

MORSE_CODE_DICT = dict()

for line in open("Morse.txt","r"):
    MORSE_CODE_DICT[line.split()[0]]=line.split()[1]

print(MORSE_CODE_DICT)
input()"""

def encrypt(zprava):
    sifra = ''
    # vyhleda ve slovniku
    for letter in zprava:
        if letter != ' ':
            sifra += MORSE_CODE_DICT[letter] + ' '

        else:
            # 1 mezera znamena pismeno a 2 znamenají mezeru
            sifra += ' '
    return sifra


#Funkce na dešifrování
def decrypt(zprava):
    zprava += ' '
    decipher = ''
    citext = ''
    for letter in zprava:
        if (letter != ' '):
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            citext += letter
        else:
            # Znamená nové písmeno
            i += 1
            if i == 2:
                decipher += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''

    return decipher

def main():
    toMorse=input("Zadej vhodnou zprávu pro přeložení: ")
    result = encrypt(toMorse.upper())
    print(result)

    fromMorse=input("Zadej vhodnou zprávu pro přeložení: ")
    result = decrypt(fromMorse)
    print(result)

if __name__ == '__main__':
    main()