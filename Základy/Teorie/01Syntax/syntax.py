"""
Syntax v jazyce python je velice jednoduchý, což také jednou z jeho hlavních předností, ale jsou zde jistá pravidla která je nutné dodržovat.
Vzhledem k tomu, že se jedná o interpretovaný (scriptový) jazyk není nutné dodržovat standartní formu programu, ovšem jsou jistá doporučení, která jsou probírána v jiné části.
"""

#Narozdíl od mnoha ostatních jazyků není nutné řádky ukončovat nějakým symbolem stačí jednoduše zčít psát na další řádek.
print("první řádek kódu")
print("druhů řádek kódu")

#Pokud by z nějákéhop důvodu bylo nutné zapsat dva příkazy na jeden řádek je to možné za použití symbolu ;
#Ovšem tento způsob se nedoporučuje, protože činní program značně nepřehledný
print("první kód na stejném řádku");print("druhý kód na stejném řádku")

"""
print() je standartní funkce jazyka python. 
Syntax funkcí je téměř identický jiným programovacím jazykům. Jmeno funkce je následováno závorkamy obsahující argumenty.
Funkce budou více rozebírány ve vlastní kapitole.
"""

#Dalším klíčovým prvkem syntaxu tohoto jazyka je odsazení a symbol dovjtečky. 
#Narozdíl od jiných jazyků nepoužívá k uzavření jednotlivých bloků kódu závorky, ale dvojtečku a odsazení v podobě tabulátorů.
#Zde předvedeno na jednoducá if podmínce, ale funguje stejným způsobem při definici funkcí, tříd, cyklů a dalších jim podobným prvkům.
if True:
	print("Odsazenný blok uvnitř if")
print("Neodsazený blok mimo if")

#V případě že má blook kódu jen jeden řádek je možné ho psát přímo za dvojtečku.
if True: print("Blok přímo za : ")
print("Blok mimo podmínku")

#Důležité je taky si v tomto jazyce dávat pozor na velké a malé znaky, neboť pytho mezi nimi rozlišuje.
print("Toto funguje")
#PRINT("Toto nefunguje")