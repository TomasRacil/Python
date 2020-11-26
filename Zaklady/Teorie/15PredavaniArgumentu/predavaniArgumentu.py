"""
Ze začátku nám většinou stačí pro zadávání hodnot do skriptu klasický input, 
ale pokročilejší skripty by měly příjímat co nejvíce argumentů z příkazové řádky.
To umožní tyto skripty volat pomoci jiných skriptů, ať už skriptů python, nebo například bash.
"""

#existují dvě metody zastaralá metoda využíva modulu sys rovnou zde vysvětlím modernější s využitím modulu argparse
import argparse

#Vytvoříme instanci nášeho parseru pomocí metody ArgumentParser(), který se stará o zpracování argumentů předaných přes příkazovou řádku
#, můžeme přidat také globální popis, jako například způsob jak mají být argumenty formátovány
parser = argparse.ArgumentParser(description='Argumenty předáváme pomocí -přikaz')

#přidáme argumenty pomocí metody add_argument() první definuje vlajku za jakou argument; metavar je celé jméno předávané v nápovědě; typ určuje typ argumentu;
#default určuje hodnotu, která je nastavená v případě že není žádná předána; help je dloubhý popis pro nápovědu
parser.add_argument('-z', metavar='zpráva', type=str, default="nic nebylo předáno", help='Zde zadejte zprávu která má být předána programu')
#můžeme přidat kolik chceme argumentů

#parse_args vrací specialní datový typ který umožňuje přistupovat k jednotlivým argumentům pomocí jejich vlajky bez -
args = parser.parse_args()

#přístup k argumentu
print(args.z)

#tento příkaz spusťte prvně pomocí příkazu: 	python predavaniArgumentu.py 						(vrátí defaultní hodnotu)
#po té ho spusťte pomocí příkazu: 				python predavaniArgumentu.py -z "Vaše zpráva"		("vaše zpráva" vymněňte za libovolnou zprávu)