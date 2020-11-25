"""
Řetězce jsou spíše datové struktury než proměné. Nejblíže by se daly prřirovnat polím znamým třeba z C++, nebo jincýh programovacích jazyků.
To tedy znamená že jsem schopní jimi iterovat a indexovat jednotlivé prvky.
"""



#První důležitá věc o řetězcích je způsob jejich formátování. Existují tři typy.
pozdrav,poradi = 'Zdravím', '3'

#První využívá operátoru %
formatovanyText1="%s. Toto je  %s. lekce" % (pozdrav, poradi)
print(formatovanyText1)

#Druhá metody format třídy string 
formatovanyText2="{1}. Toto je  {0}. lekce".format(poradi, pozdrav)
print(formatovanyText2)

#Třetí je takzvaný formátovaný string. Jedná se o nejpoužívanější metodu neboť je nejpřehlednější, nejkratší a nejflexibilnější.
formatovanyText3=f"{pozdrav}. Toto je  {poradi}. lekce"
print(formatovanyText3)


#Pokud chceme využít uvozovek v rámci řetězce, musíme využit oba druhy, jeden pro samotný řetězec a druhý pro jeho obsah.
#Do řetězce jsme také schopní přidat symboly například pro nový řádek \n, nebo \t pro tabulátor  a další
print('\n "Naučila jsem se, že cesta pokroku není rychlá ani snadná." \n \t—  Marie Curie-Skłodowská\n')

#Pokud chceme zapsat funkční sybol do řetězce využíváme \
print("Například jednu uvozovku: \", \nnebo znak pro nový rádek je \\n\n")




#Velice důležitá je také schopnost přistupovat k textu skrze indexy, první znak v retězci má index 0
text="Ukázkový text pro potřeby indexace a iterace\n"
print(text)
print(f'Symbol na druhém místě je {text[2]}\n')

#Python také nabízí možnost záporného indexování 
print(f'Symbol na druhém místě od konce je {text[-2]}\n')

#V neposlední řadě můžeme využít takzvaný slicing, který umožňuje vybrat podmnožinu řetězce na základě indexů znaků.
print(f'Symboly od 8 znaku do 8 znaku před koncem  {text[8:-8]}\n')

#Iterovaná řetězcem
for znak in text:
	print(znak)



#Užitečné funkce a metody pro práci s řetězci
#Funkce len(), která vrací délku objektu předaného v rámci argumentu.
print(f'Délka řetězce:  {len(text)}\n')



#Metoda lower() vrací řetězec se znaky převedenými na malé písmena
print(f'Text malými písmeny:  {text.lower()}\n')

#Metoda upper() vrací řetězec se znaky převedenými na kapitálky
print(f'Text kapitálky:  {text.upper()}\n')

#Metoda replace() vrací řetězec se znaky nebo skupinu znaků převedenými na jiné
print(f'Změna prvního slova:  {text.replace("Ukázkový", "Vzorový")}\n')

#Metoda split() vrací seznam řetězců z původního řetězce na základě definovaného seperátoru
#existuje i metoda splitlines() která vrací seznam podle jednotlivých řádků řetězce
print(f'Rozdělení podle mezezer:  {text.split(" ")}\n')


#Metoda strip() odstraní znaky na začátku a konci řetězce defaultně mezery, ale může být zvolen jakýkoliv znak
#existuje i metoda lstrip() a rstrip() pro odstranění znaků z levé strany a pravé strany
zbytecneMocUvozovek = '-------text------'
print(f'Bez uvozovek: {zbytecneMocUvozovek.strip("-")}\n')

#Metoda find() vrací index první nalezená instance znaků či skupiny znaků předaných jako argument.
#existuje i metoda rfind, která vrací index poslední instance
print(f'Index prvního ř:  {text.find("ř")}\n')

#Metoda count() vrací množství výskutů instance znaků či skupiny znaků předaných jako argument.
print(f'Počet znaků a:  {text.count("a")}\n')

#Metoda join() vrací řetězec rozšířený o prvky datové struktury předané skrze argument
programovaciJazyky = ['Python','Kotlin','Go']
print(f'Převedení seznamu do stringu: {", ".join(programovaciJazyky)}')

"""
Samozřejmě užitečných metod je mnohem více, ale ty zde uvedé považuji za nejdůležitější
"""