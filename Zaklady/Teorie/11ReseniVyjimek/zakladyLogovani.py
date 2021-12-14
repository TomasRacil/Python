"""
Logování nám umožňuje jednoduší způsob sledování chodu našeho programu.
"""

#budeme potřebovat importovat knihovnu logging
import logging


#První co musíme udělat, abychom mohly úspěšně provádět logování je nakonfigurovat náš logging.
#Změna nastavení je provedena pomocí metody bassic config(**args)

#Pro definování úrovně zpráv které budou zaznamenávány slouží klíčové slovo level
#máme pět úrovní DEBUG,INFO,WARNING,ERROR,CRITICAL defaultní je WARNING

#logging.basicConfig(level=logging.INFO)



#Pro logování do souboru místo do konzole slouží klíčová slova 
#filename název souboru;
#filemode způsob zápisu (w-přepíše soubor při každém spuštění aplikace,a-přidává na konec souboru);
#format, který definuje jakým způsobem bude zpráva zformátována;

logging.basicConfig(level=logging.DEBUG, filename='ukazka.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s -%(asctime)s')

#V rámci formátu je možné odkazovat na základní elementy třídy LogRecord, pomocí %(názvu elementu)s
#Užitečné elementy:
#%(asctime)s - čas vytvoření události
#%(message)s - zpráva vytvořená v rámci události
#%(name)s - úroveň události
#%(process)s - ID procesu na kterém k události došlo



#Pro vyvolání zprávy použijeme jednu z pětimetod podle úrovně požadované zprávy
#debug(zpráva) debug používáme při vývoji pro sledování chodu programu, např. pro zjištění metod třídy, obsahu proměnné atd. 
logging.debug(f'Jaké metody má logging {logging}')

#info(zpráva) info slouží pro informování uživatele o chodu aplikace
logging.info('Probíhá připojování k serveru')

#warning(zpráva) upozornění na událost 
logging.warning('Pozor tato akce je nezvratná')

#error(zpráva) upozornění na vzniklou chybu 
logging.error('Připojení k serveru selhalo')

#warning(zpráva) upozornění na takovou chybu, která má za následek ukončení, nebo vážný zásah do fungování aplikace
logging.critical('Klíčové závislosti nenalezeny! Aplikace bude ukončena.')

#Pokud k jednoduchému zachycení chybovou události (try) metodu exception která zachytí událost a přiřadí jí úroveň error 
# a,b = 5,0

# try:
#     c = a / b
# except Exception as e: logging.exception("Exception occurred")