# HANGMAN
- uživatel se může přihlásit a registrovat, modul LogReg.py, uživatele a heslo najdeme v souboru uzivatele.txt
    * program sleduje zda uživatel zadal správně heslo a jméno
    * pokud si zvolíme Singup, tak sleduje, jestli už uživatele nemáme v souboru
- následuje zvolení úrovně
   * najdeme v Score.py 
    1. úroveň = slova od 1 - 5 znaků a bez složitějších znaků
    2. úroveň = slova od 6 - 8 znaků a bez složitějších znaků
    3. úroveň = vygeneruje se slovo od 9 - 10 znaků, nebo slovo, které obsahuje složitější znaky 
- uživatel hádá random generované slovo
    * najdeme v Draw.py
    * pokud uživatel uhodne písmenko, tak se nakreslí a dá se do listu, následně se sleduje, zda uživatel nezadal vícekrát stejné písmenko
    * pokud neuhodne, přikreslí se oběšenec
- počítá se skóre za jedno slovo, které uživatel aktuálně hádá
- následně se celkové skóre sčítá a dělí počtem her --> průměr na jednu hru, modul Score.py
- hráč může pokračovat ve hře, kde se mu vygenuruje nové slovo
- při ukončení se ukáže žebříček jen pro 5 nejlepších hráčů, čím menší skóre na jednu hru, tím lepší pozice
    * vytvoří se txt soubor do kterého dáme srovnaný žeříček, po vypsání se soubor smaže (zebricek.txt)
### Úkoly:
- hash(větší ochrana uživatele) 
- databáze, místo txt souborů
- nápověda / odkrytí písmena, ale bude se muset změnit i skóre 
