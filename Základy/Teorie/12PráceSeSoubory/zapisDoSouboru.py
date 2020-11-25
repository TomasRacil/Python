#Abychom mohli do souboru zapisovat potřebujeme ho prvně otevřít pomocí open()

#vytvoříme zálohu našeho dokumentu
soubor = open("demo.txt", "r")
zaloha=soubor.read()
soubor.close()
try:

	#nejprve začneme argumentem "w" ten nám umožní přepsat kompletně celý dokument 
	soubor = open("demo.txt", "w")

	#metoda write nám umožňuje vložit řetězec, který má nahradit obsah
	soubor.write("A všechno je pryč. ")
	#další metoda write přidá řetězec na konec předchozího
	soubor.write("A nebo ne?\n")

	soubor.close()

	#zobrazení obsahu změněného dokumentu
	print("Obsah textu s použitím 'w': \n" + open("demo.txt", "r").read())


	#nejprve začneme argumentem "a" ten nám umožní přidat řetězce na konec dokumentu
	soubor = open("demo.txt", "a")

	#metoda write nám umožňuje vložit řetězec, který se přidá na konec dokumentu
	soubor.write("Přidaný řetězec 1\n")
	#další metoda write přidá řetězec na konec předchozího
	soubor.write("Přidaný řetězec 2")

	soubor.close()

	#zobrazení obsahu změněného dokumentu
	print("Obsah textu s použitím 'a': \n" +open("demo.txt", "r").read())

except:
	pass
#obnovíme zálohu
open("demo.txt", "w").write(zaloha)
