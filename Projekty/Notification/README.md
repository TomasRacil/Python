Notifikační program - Script, který se postará o vytvoření upozornění (notify2)

Aktuální verze programu při spuštění vytvoří request na server s daty o počtech ohledně pandemie covid-19 v ČR. Dostane data ze kterých vytáhne počet mrtvích a vytvoří notifikaci která vypíše toto číslo. Poté program počká 10 minut a znovu získá data ze serveru, porovná je s předchzími daty a vytvoří novou notifikaci pokovaď se počet mrtvích změnil.

Náměty k pokračování:
-pomocí flag umožnit zvolení státu jehož počet mrtvích se bude oznamovat
-pomocí flag umožnit zvolení udaje jiného než umrtí
-upravit program aby se dal např příkazem ukončit