                          Frekvence slov v textu
==============================================================================

Program vypočítá frekvenci výskytu každého platného slova v souboru data.txt

Vstup:
- program přijímá vlajku -min - pokud je počet znaků daného slova vyšší nebo roven hodnotě předané vlajce min - program
  slovo přidá do databáze - slova s menším počtem znaků, než je min jsou ignorována
- syntaxe: "WordFrequency.py -min 3" ignoruje všechna slova, která mají méně znaků než 3
- program určuje délku slova až po odstranění znaků obsažených v listu remove - tzn. slovo "don't" po odstranění apostrofu
  obsahuje 4 znaky

Popis funkce:
- Program nahraje obsah souboru data.txt do paměti a rozdělí text na jednotlivá slova (podle mezer a konců řádku)
- Z každého slova odebere nežádoucí znaky (list remove) a převede vše na malá písmena
- Vytvoří se databáze unikátních slov a ke každému slovu se přiřazuje jeho výskyt - program
  prochází všechna upravená slova a porovnává je se svojí databází, pokud slovo najde, přičte si 1 k jeho výskytu
  pokud slovo v databázi nenajde - přidá si ho do databáze a nastaví mu výskyt 1
- program přijímá jako vstup vlajku -min která definuje, kolik musí mít slovo minimálně znaků, aby bylo
  považováno za platné a přidalo se do databáze programu - je takto možné odfiltrovat krátká slova
- databáze má charakter dvourozměrného pole (vnořené listy do listu) 
  př. database = [["ahoj", 2], ["pes", 3]] - slovo ahoj má výskyt 2, slovo pes má výskyt 3
  přístup k prvkům: database[1][0] vrací pes, database[1][1] vrací 3 

Progress bar verze:
- přidává do UI grafické zobrazení postupu - negativní vliv na výkon a čas zpracování souboru, ale vypadá to dobře
