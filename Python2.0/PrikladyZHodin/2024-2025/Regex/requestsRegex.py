from requests import get
from os import path
import re

cesta_k_souboru = path.join(path.dirname(path.realpath(__file__)), "othello.txt")

naplnen:bool = False

try:
    with open(cesta_k_souboru, "r") as soubor:
        if soubor.read(1):
            naplnen=True
except FileNotFoundError:
    if not naplnen:
        r = get("https://www.gutenberg.org/ebooks/1531.txt.utf-8")

        with open(cesta_k_souboru, "w",encoding=r.encoding) as soubor:
            soubor.write(r.text)
            
with open(cesta_k_souboru, "r") as soubor:
        # print([slovo for slovo in re.split('\s+',soubor.read())])\
        # jmena = re.findall('[A-Z][a-z]+',soubor.read())
        slova = re.findall('[A-Z]{2,}', soubor.read())
        uninkatni_slova = set(slova)
        pocet_slov = [(slova.count(jmeno),jmeno) for jmeno in uninkatni_slova]
        pocet_slov.sort(key=lambda x:x[0], reverse=True)
        print(pocet_slov[:10])

        # unikatni_jmena = set(jmena)
        # soubor.seek(0)
        # pocet_unikatnich_jmen=[(jmena.count(slovo), slovo) for slovo in unikatni_jmena]
        # print(pocet_unikatnich_jmen)
        


# with open(cesta_k_souboru) as soubor:
#     # print(len(re.split('\s', soubor.read())))
#     # soubor.seek(0)
#     vety = [re.sub("\s+"," ", veta) for veta in re.split("[\.\?\!]\s+", soubor.read()) if len(re.sub("\s+"," ", veta).split(" "))>1]
#     vety.sort(key=lambda x:len(x))
#     print(vety[:100])
#     print(len(vety))
#     # slova = re.findall("\n\n([A-Z]{2,})\.\n",soubor.read())
#     # # print(slova)
#     # vyskyty = [(jmeno,slova.count(jmeno)) for jmeno in set(slova)]
#     # vyskyty.sort(key=lambda x:x[1], reverse=True)
#     # print(vyskyty[-1],vyskyty[0])