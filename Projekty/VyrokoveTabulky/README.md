Výrokové tabulky

Program slouží k převedení výrokových formulí na tabulku pravdivostních hodnot

parser.py
    staženo z: https://github.com/clamesc/Propositional-Logic-Parser
    následně upraveno
    funkce parse(lex('retezec'))
        dělí řetězec na jednotlivé operace a výroky a vkládá je do listů 
    jiné funkce nevyužívám

formule.py
    obsahuje všechny základní funkce pro operace s výroky, funkci na parsování převzatou z parser.py a samotnou funkci na řešení výrokových formulí

main.py


Užitečný odkaz: https://www.erpelstolz.at/gateway/formular-uk-zentral.html
    webový kalkulátor na výrokové tabulky


TODO:
1. vylepšení, zefektivnění v parser.py - např.: aby negace vytvářeli samostatný list
2. neomezený počet výroků, různá písmena pro označení výroků
3. DNF, KNF
4. GUI