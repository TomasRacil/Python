#Pro přístup k souboru použijeme funkci open("soubor","čtení/zápis")
#"soubor" nahradíme buď jen jménem pokud se nachází ve stejném adresáři ze kterého je script spouštěn
#nebo celou celou cestou
#druhý argument může mít hodnoty: 
#"r"- read pro čtení, "w"- pro zápis, "a"- pro přidání textu na konec
soubor = open("demo.txt", "r")
#soubor = open("/home/tomas/Vyuka/Python/Základy/Teorie/12PráceSeSoubory/demo.txt","r")
print(f"Typ třídy kterou vrací open: {type(soubor)} \n")

#Metoda read() defaultně (pokud jí nepředáme žádnou hodnotu) vrací celý text jako string, pokud chceme jen část můžeme specifikovat počet znaků
print("Následuje obsah textu (šest znaků):")
print(soubor.read(6)+'\n')
#Pokud zavoláme metodu read() znovu pokračuje tam kde poslední read() skončila
print("Následuje obsah textu (dalších šest znaků):")
print(soubor.read(6)+'\n')

#Pro přístup k jednotlivým řádkům můžeme použít metodu readline(), která funguje jako read, akorát se zastaví u newline znaku.
print("Zbytek prvního řádku:")
print(soubor.readline()+'\n')
print("Druhý řádek:")
print(soubor.readline()+'\n')

#Můžeme také soubor procházet pomocí for loop
print("Ostatní řádky:")
for radek in soubor:
	print(radek)

#Po skončení práce se souborem je vhodné zavolat metodu close() pro uzavření komunikace.
soubor.close()
