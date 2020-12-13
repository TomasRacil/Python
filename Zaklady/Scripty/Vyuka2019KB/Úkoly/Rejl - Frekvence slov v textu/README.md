                          Frekvence slov v textu
==============================================================================
Program vypoèítá frekvenci výskytu každého platného slova v souboru data.txt

Vstup:
- program pøijímá vlajku -min - pokud je poèet znakù daného slova vyšší nebo roven hodnotì pøedané vlajce min - program
  slovo pøidá do databáze - slova s menším poètem znakù, než je min jsou ignorována
- syntaxe: "WordFrequency.py -min 3" ignoruje všechna slova, která mají ménì znakù než 3
- program urèuje délku slova až po odstranìní znakù obsažených v listu remove - tzn. slovo "don't" po odstranìní apostrofu
  obsahuje 4 znaky

Popis funkce:
- Program nahraje obsah souboru data.txt do pamìti a rozdìlí text na jednotlivá slova (podle mezer a koncù øádku)
- Z každého slova odebere nežádoucí znaky (list remove) a pøevede vše na malá písmena
- Vytvoøí se databáze unikátních slov a ke každému slovu se pøiøazuje jeho výskyt - program
  prochází všechna upravená slova a porovnává je se svojí databází, pokud slovo najde, pøiète si 1 k jeho výskytu
  pokud slovo v databázi nenajde - pøidá si ho do databáze a nastaví mu výskyt 1
- program pøijímá jako vstup vlajku -min která definuje, kolik musí mít slovo minimálnì znakù, aby bylo
  považováno za platné a pøidalo se do databáze programu - je takto možné odfiltrovat krátká slova
- databáze má charakter dvourozmìrného pole (vnoøené listy do listu) 
  pø. database = [["ahoj", 2], ["pes", 3]] - slovo ahoj má výskyt 2, slovo pes má výskyt 3
  pøístup k prvkùm: database[1][0] vrací pes, database[1][1] vrací 3 