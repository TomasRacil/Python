Program, který běží na pozadí a spouští webové stránky, poskytuje možnost registrace, přihlášení a odhlášení

TODO:
- Nejprve je potřeba si stáhnout všechny potřebné moduly, a to hlavně: Flask, Bootstrap, SQLalchemy a balíček sqlite

- Následně je potřeba mít vytvořenou nějakou stránku, kterou bude program spouštět

- Poté se v programu app.py, pomocí kterého se i stránky spouští, nadefinuje jakým způsobem bude probíhat spouštění, vytvoří se formuláře na přihlášení a registraci a zabezpečí se ověření přihlašovacích údajů

- Důležité je propojení s databází, protože ta slouží jak k ukládání nových uživatelů, tak i kvůli kontrole při přihlášování

- Databáze se vytváří přímo v terminálu a je na ní potřeba balíček sqlite a zároveň si přidat adresář, ve kterém se nachází do PATH!!!!

Spouštění a obsluha:
- Spouští se přímo program app.py, který vytvoří lokální server na adrese http://127.0.0.1:5000/

- Do adresního řádku píšeme za lomítko to, co jsme nadefinovali v app.py, např. pokud máme @app.route('/index'), adresa vypadá takto: http://127.0.0.1:5000/index

- Datábaze je nyní už vytvořená, obsahuje tabulku user a jsou v ní už i záznamy

- Pro vytvoření databáze je třeba v příkazovém řádku zadat: sqlite3 jmeno_databaze.db(k vytvoření dojde pouze pokud  databáze s takovým jménem ještě neexistuje), dále je potřeba napsat: from app import db -> db.create_all() to vytvoří tabulku(samotná tabulka s jednotlivými parametry je definovaná třídou User v app.py)

- Když se chceme na jednotlivé záznamy podívat, napíšeme: sqlite3 databaze.db, to nám otevře databázi a poté: select * from user;
- Podobně můžeme i mazat: delete * from user; (toto smaže všechny uživatele, mazat by šli i jednotlivě při lepší znalosti  jazyka SQL) 

Nápady do budoucna:
- Možnost změny hesla
- Vytvoření stránky na administraci, na které bude moci admin přímo mazat jednotlivé uživatele
- Přidání sekce pro diskuzi 
- Zobrazení uživatelského jména přihlášeného uživatele na stránce index.html např. v bloku header

Chyby:
- Samotná stránka index.html se nezobrazuje úplně správně, u různých rozlišení může dojít k posunutí bloku footer, který by měl zůstávat dole, ale to je zálěžitost CSS