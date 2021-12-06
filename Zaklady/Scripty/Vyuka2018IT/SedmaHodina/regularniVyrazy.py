from urllib.request import urlopen
import re

# with urlopen("https://www.gutenberg.org/cache/epub/2265/pg2265.txt") as url:

#     soubor = open("C:\Výuka\Python\Zaklady\Scripty\Vyuka2018IT\SedmaHodina\hamlet.txt", "w")
#     for line in url:
#         soubor.write(str(line))

with open("C:\Výuka\Python\Zaklady\Scripty\Vyuka2018IT\SedmaHodina\hamlet.txt", "r") as hamlet:
    hamletFormated=re.sub(r"'b'||b'||'b||\\r||\\n",'',hamlet.read())
    print(hamletFormated)
    
