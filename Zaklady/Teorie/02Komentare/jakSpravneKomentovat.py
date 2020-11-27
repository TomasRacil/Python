"""
Komentáře podobně jako v každém jiném jazyce mají dvě funkce.
	První ta hlavní je lépe popsat fungování kódu to může pomoci jak nám samotným tak ostatním, kteří se třeba naším kódem budou chtít inspirovat.
	Druhý, i když vedlejší, mnohem častěji využíván je pro hledání a řešení chyb
Zaměříme se na tu první, protože ta druhá by měla být řešena jinými způsoby.

Neexistuje jeden standard, který by určoval jakým způsobem má být kód okomentovan. 
Obecně pravidla pro komentování:
	komentáře jsou vždy stručné a vystižné
	komentujeme tam, kde je algoritmus z jistých důvodů nepřehledný, nebo by se tak mohl jevit
	komentujeme všechny klíčové části či myšlenky našeho programu (scriptu)
	komentujeme v případě, kdy definujeme nějaký samostatný blok například funkci, třídu, nebo její metodu

Ovšem tyto příklady uvadějí, kde by komentář měl být, ovšem můžeme okomentovat klidně každý řádek, pokud to shledáme důležitým a neudělá to program nepřehledným.
Budou následovat některé jednoduché ukázky.
"""

def function(parameter='default'):
	"""Demonstrate commentary of function

	Longer description if neccesary.
	
	Args:
		parameter (str): explain parameter and limitation (default 'default')

	Returns:
		str: return parameter
	"""
	return parameter 


#pokud máme správně okomentované prvky můžeme jednoduše přistupovat k informacím o nich pomocí metody __doc__
print(function.__doc__ + '\n')

"""
Komentování funkcí je poměrně standartně zavedené ve formátu jaký jsem předvedl na příkladu.
Obecně je dobré využívat angličtiny jak při psaní kódu tak při jeho komentování, ale není to nutnost.

Na prvním řádku odpovídáme co funkce dělá
Na dalším může být dodatečný popis pokud je nutný.
Následující řádky jsou nutné pouze v případě že funkce přijímá nějáké parametry.
Následuje sekce 'Keyword arguments:' nebo 'Args:' její prvky jsou odsazené tabulátorem.
Na následujících řádcích jsou vysvětleny jednotlivé parametry název parametru (typ): co parametr představuje a omezení(default 'defaultní hodnota pokud nějaká je')
Následuje sekce 'Returns:'  její prvky jsou odsazené tabulátorem.
Na následujícím řádku je vysvětlena návratová hodnota funkce typ: co funkce vrací popřípadě význam návratových hodnot nebo rozsah
"""

"""
Můžeme popisovat i jedotlivé proměné pokud uznáme za vhodné.
Tyto popisy by měli následovat rovnou za její deklarací.
"""

real=4.0	#real part of number
imag=1.0	#imaginary part of number

"""
Komentáře jsou také vhodné k označování kódu, 
	kterému nerozumíme 
	kde je nutné ještě provést nějáké úpravy
	odkaz na související webovou stránku
Tyto části nemusí být anglicky předpokládá se, že v programu budou jen při vývoji.
Dobré je používat slovo TODO pro snazší hledání těchto bodů.
"""

import os 	#https://docs.python.org/3/library/os.html

os.environ 	#TODO: Podívat se na objekt environ

x,y = 2,1
print(x/y)	#TODO: Zabezpečit dělení nulou

"""
Poslední co je důležité zmínit je komentování námi vytvořených modůlů (knihoven) obsahujících funkce třídy a jejich metody.
Tento komentář by měl vždy být uveden v hlavičce našeho modulu.
"""

# -*- coding: utf-8 -*-
"""Name of the module

Followed by basic explenation of the modules purpose and function. Can be
multiple lines

Example:
    There should be same usage examples of the module but this part is optional.

        $ python example_google.py

Attributes:
    varible (int): documentation of potential variables on the module level. They
    	are optional can be documented directly not in head.

Todo:
    * List of things that has to be done in future

website of this module if exists

"""


"""
Jedná se pouze o jednoduché shrnutí postupů, které jsem považoval za vhodné uvést.
Velice dobrý návod jak komentovat je zde https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
"""