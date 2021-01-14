Program pro rozpoznání a přečtení údajů z cestovního pasu
==========================================================
- Program bude pomocí knihovny OpenCV rozpoznávat údaje na cestovním pasu - jsou zde zapsány v pevně stanoveném formátu pro snažší strojové čtení
- existují dva formáty zápisu: dvouřádkový a trojřádkový - program by si ve finální verzi měl poradit s oběma
- pomocí OpenCV bude fotografie pasu převedna na černobílou a postupně bude obrazovými úpravami převedena na zvýrazněný text
- text bude rozpoznán a zobrazen

- pro bezpečné testování jsem získal vzory různých evropských pasů, na kterých je možné testovat program (viz. složka Examples)

- jako rozšíření tohoto programu by mělo být možné použít jako zdroj obrazu živé záběry z kamery počítače


Verze 0.1
===========================================================
- první funkční verze - rozpozná zadanou část pasu a přečte z ní data
- přečtená data vypisuje do konzole
- pro fungování je třeba mít tesseract verze 5 (https://github.com/UB-Mannheim/tesseract/wiki)


Verze 0.2
===========================================================
- rozdělení jednotlivých částí do modulů
- doplnění komentářů

TODO:
===========================================================
- upravit předávání obrázku z openCV do Tesseract tak, aby se obrázek nemusel ukládat na disk
- dále zpracovat detekovaný string - pomocí RegEx z něj separovat jméno, příjmení atd. + odstranit chyby vzniklé ve strojovém rozpoznání textu
