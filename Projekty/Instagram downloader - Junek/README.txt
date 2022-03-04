1. Vytvoření databáze v MySQL
	-Spustit database.py
	-Zadejte požadované údaje(hodnoty v závorkách jsou defaultní):
		host=("localhost")
		user=("root")
		passwd=bylo zvoleno uživatelem
	-Pokud script selže, je třeba nainstalovat mysql connector pro python (nejnovější verze pro 64bit Windows je ve složce)
	-Po vytvoření databáze se vytvoří oznámení o úspěšném vytvoření databází (pokud se nezobrazí program selhal viz. výše) a ukončíme ho stiskem jakéhokoliv tlačítka
	-Tento script se úspěšně dokončí pouze při prvním spuštění, protože potom už je databáze vytvořena. (Pokud databázi smažeme, script bude opět fungovat.) 

2. Stažení instagramového profilu a zapsání do databáze
	-Spustit instadowload
	-Pokud je profil soukromý --> zadat své přihlašovací údaje (musíte daného uživatele sledovat)
		(v souboru login.txt jsou údaje určené k testování)
	-Pokud je profil veřejný --> stisknout ENTER
	-Zadat uživatelské jméno profilu, který chcete stáhnout a zapsat do databáze
	-Po dokončení stahování vám bude nabídnuto zadání dalšího uživatelského jména.

Při častém přihlašování (opakované spouštění scriptu) může dojít k chybě v přihlášení ze strany instagramu --> Je třeba chvíli počkat nebo změnit profil, na který se přihlašujeme.
Podrobnější popis funkce je přímo ve scriptu.

Python 3.10
MySQL 8.0