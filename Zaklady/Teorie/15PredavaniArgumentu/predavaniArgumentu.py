"""
Ze začátku nám většinou stačí pro zadávání hodnot do skriptu klasický input, 
ale pokročilejší skripty by měly příjímat co nejvíce argumentů z příkazové řádky.
To umožní tyto skripty volat pomoci jiných skriptů, ať už skriptů python, nebo například bash.
"""

#existují dvě metody zastaralá metoda využíva modulu sys rovnou zde vysvětlím modernější s využitím modulu argparse
import argparse

#Vytvoříme instanci nášeho parseru pomocí metody ArgumentParser(), který se stará o zpracování argumentů předaných přes příkazovou řádku
#, můžeme přidat také globální popis, jako například způsob jak mají být argumenty formátovány
parser = argparse.ArgumentParser(description='Program demonstrující předávání argumentů přes vlajky')

#přidáme argumenty pomocí metody add_argument() první definuje vlajku za jakou argument; metavar je celé jméno předávané v nápovědě; typ určuje typ argumentu;
#default určuje hodnotu, která je nastavená v případě že není žádná předána; help je dloubhý popis pro nápovědu
parser.add_argument('-z', metavar='--zprava', type=str, default="nic nebylo předáno", help='Zde zadejte zprávu která má být předána programu')
parser.add_argument('-n',metavar="--nasobnost",type=int, default=1, help="Kolikrát vytisknout řetězec")
#můžeme přidat kolik chceme argumentů

#parse_args vrací specialní datový typ který umožňuje přistupovat k jednotlivým argumentům pomocí jejich vlajky bez -
args = parser.parse_args()

#přístup k argumentu
print(args.z*args.n)

#tento příkaz spusťte prvně pomocí příkazu: 	python predavaniArgumentu.py 						(vrátí defaultní hodnotu)
#po té ho spusťte pomocí příkazu: 				python predavaniArgumentu.py -z "Vaše zpráva"		("vaše zpráva" vymněňte za libovolnou zprávu)