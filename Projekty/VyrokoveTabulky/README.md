# Výrokové tabulky

Téma výrokové logiky je vyučováno v matematice už na střední škole. Tabulka pravdivostních hodnost se používá při vyhodnocení složitějších formulí. Pro pokrytí středoškolské matiky a základů vysokoškolské nám postačí tabulka nanejvýš se 3 výroky.

Program slouží k převedení výrokových formulí na tabulku pravdivostních hodnot.
Jak s tabulkou pracovat:
   - na vstupu je zadána formule - na výstupu zjistíme:
       - v jakých ohodnoceních (řádcích) je formule **pravdivá** (rovna 1)
       - jestli se jedná o **tatologii** (v případě, že jsou všechna ohodnocení pravdivá)
   - na vstupu jsou zadány dvě formule, tak že jsou spojeny ekvivalencí <=>, na výstupu zjistíme jestli jsou **ekvivaletní**, pokud bude ve všech řádcích 1
     

parser.py
   - staženo z: https://github.com/clamesc/Propositional-Logic-Parser
   - následně upraveno
   - funkce parse(lex('retezec'))
       - dělí řetězec na jednotlivé operace a výroky a vkládá je do listů 
   - jiné funkce nevyužívám

formule.py
   - obsahuje všechny základní funkce pro operace s výroky, funkci na parsování převzatou z parser.py a samotnou funkci na řešení výrokových formulí

main.py
   - hlavní část programu, do kterého jsou vloženy ostatní moduly 


Užitečný odkaz: https://www.erpelstolz.at/gateway/formular-uk-zentral.html
   - webový kalkulátor na výrokové tabulky


TODO:
1. vylepšení, zefektivnění v parser.py - např.: aby negace vytvářeli samostatný list
2. neomezený počet výroků, různá písmena pro označení výroků
3. DNF, KNF
4. GUI