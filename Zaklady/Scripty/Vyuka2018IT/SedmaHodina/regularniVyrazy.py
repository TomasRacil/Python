from urllib.request import urlopen
import re

# with urlopen("https://www.gutenberg.org/cache/epub/2265/pg2265.txt") as url:

#     soubor = open("C:\Výuka\Python\Zaklady\Scripty\Vyuka2018IT\SedmaHodina\hamlet.txt", "w", encoding='utf-8')
#     for line in url.read().decode("utf-8").strip().split("\n"):
#         soubor.write(line)
    # soubor.write(url.read().decode("utf-8"))




with open("C:\Výuka\Python\Zaklady\Scripty\Vyuka2018IT\SedmaHodina\hamlet.txt", "r") as hamlet:
    hamletText=hamlet.read()
    zacatekKnihy=re.search(r'(?<=David Reed\n\n)The Tragedie of Hamlet',hamletText).start()
    hlavicka=hamletText[:zacatekKnihy]
    obsah=hamletText[zacatekKnihy:]
    # print(hlavicka)

    vetyVzor = re.compile(r'([A-Z][^\.!?:]*[\.!?:])', re.M)
    vety=[re.sub("\s+"," ",veta) for veta in vetyVzor.findall(obsah)]

    for veta in vety:
        print(veta)
        input()

    
    # hamletFormated=re.sub(r"'b'||b'||'b||\\r||\\n",'',hamlet.read())
    # print(hamletFormated)
    
