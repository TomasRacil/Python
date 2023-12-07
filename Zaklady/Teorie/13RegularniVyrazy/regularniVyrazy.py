"""
Regulární výrazy slouží k hledání textu odpovídajícího nějákemu předem definovanonému vzoru. Abychom v pythonu moholi regulární výrazy plně používat budeme muset importovat knihovnu RegEx.
"""
#import modulu RegEx
import re

#Definujeme text, který bude prohledáván.
text= "Email pana Kolika je kolik@email.com.\nTento email nemá pan Kolík již 5 let."


#Dále musíme definovat regulární výraz(string). Ten slouží jako vzor textu, který heldáme.
#Následují pravidla se používají při definici výrazů

#Hranaté závorky používáme pro seskupování jednotlivých znaků např. [abc] -bude roven všem výskytům a,b, nebo c
#Také v rámci hranatých závorek můžeme uvést rozsah [a-z] - všchny malá symboly
#Metoda search(regulární výraz,text) vrací hodnotu pokud v textu existuje řetězec, který vystihuje regularní výraz
x = re.search("[abc]", text)
print(f"První výskyty a,b, nebo c: {x}\n")

#Tečka vystihuje jakýkoliv symbol kromě nového řádku
x = re.search(".....", text)
print(f"První znak: {x}")

#Hvězdička udává že předchozích symbolu skupiny symbolu je 0 až nekonečno
x = re.search(".*", text)
print(f"Všechny znaky: {x}\n")

#Plus udává že předchozích symbolu skupiny symbolu je 1 až nekonečno
x = re.search("[a-z]+", text)
print(f"První slovo s malými písmeny: {x}\n")

#Složené závorky s číslem uvnitř udávají přesný počet výskytů symbolů předcházející skupiny (také můžeme zadat rozsah)
x = re.search("[ajepn]{4}", text)
print(f"Přesně čtyři výskyty jakékoliv kombinace symbolů a,j,p,e,n: {x}\n")

#Pipe slouží jako or 
x = re.search("jmeno|email", text)
print(f"První jmeno nebo email: {x}\n")

#Pomocí stříšky a nebo dolaru označujeme začátek nebo konec řetězce
x = re.search("[a-z\.]+$", text)
print(f"Poslední znaky: {x}\n")

#Pokud chceme použít speciální symbol využijeme \ symbol
x = re.search("\.[a-z]{2,3}", text)
print(f"Domena: {x}\n")

#Kombinace zpětného lomítka a znaku
#\b - označení začátku slova; 
#\B označení konce slova
#u těchto dvou musíme použít r před řetězcem (definuje raw string)
x = re.search(r"\be[a-z]*", text)
print(f"První slovo zacinajici na e: {x}\n")

#\d - pokud řetězec obsahuje cisla stejné jako [0-9]
#\D - pokud řetězec neobsahuje cisla stejné jako [0-9]
x = re.search("\d", text)
print(f"První výskyt cisla: {x}\n")

#\s - pokud řetězec obsahuje mezeru
#\S - pokud řetězec neobsahuje mezeru
x = re.search("\s", text)
print(f"První výskyt mezery: {x}\n")

#\w - pokud řetězec obsahuje znaky a-Z, O-9, nebo _
#\W - pokud řetězec neobsahuje znaky a-Z, O-9, nebo _
x = re.search("\w+", text)
print(f"První slovo: {x}\n")

#DAlší informace a možnosti je možné najít na této stránce https://docs.python.org/3/library/re.html

#Jednoduchý regulární výraz pro nalezení emailové adresy
emailVzor="([a-z\d]+[a-z\d\.-_]*[a-z0-9]+)@(\w+.\w{2,3})"
#vysvětlení výrazu
#[a-z0-9]+ 	jakýkoliv počet znaků nebo čísel větší jak jedna 
#[\._]? 	nula nebo jeden výskyt . nebo ?
#@
#\w+		jeden a více znaků a-Z, O-9, nebo _
#.
#\w{2,3}	dva až tři znaky a-Z, O-9, nebo _

#metoda findall(regulární výraz, text) vrací list všech podmnožin řetězce, které splňovali regulární výraz
emaily = re.findall(emailVzor, text)
print(f"Nalezené emaily: {emaily}\n")

#metoda split(regulární výraz, text) rozdělí email v místě které splňuje regulární výraz
# slicedEmail = re.split('@',emaily[0])
# print(f"Rozdělený email: {slicedEmail}\n")

#metoda sub(regulární výraz, nová hodnota textu, text) vymění všechny podmnožiny textu splňující regulární výraz za novou hodnotu textu
ladan = re.sub("[kK]ol[ií]k", "ladan", text)
print(f"Záměna kolik za Ladan: {ladan}\n")