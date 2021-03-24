Program pro ukládání dat z JSON struktury do databázového systému PostgreSQL
V projektu jsou dva moduly funkce.py a InsertData.py
Modul funkce.py implementuje knihovnu request a definuje funkci jsonGetInfo() ta po blocích sbírá data přes URL adresu na které se nachází JSON struktura.
Modul InsertData.py implementuje knihovnu psycopg2 pro komunikaci s databází a definuje funkci Uloz(data), která posílá data na databázový systém.
Uloz(data) s parametrem ve funkci main() dostává data, které jsou uloženy do proměnné přes funkci jsonGetInfo()
  V první části funkce Uloz(data) se nachází přihlašovací údaje k databázi (v reálném světě velice neefentivní postup, ale pro mé účely dostačující)
  Dále probíhá vlastní připojení (kontrola try/except), která probíhá po celou dobu přenosu
  Porovná počet prvků v databázi s počtem prvků JSON struktury. Pokud v JSON struktuře byl přidán další prvek, přidá pouze rozdíl těchto prvků
  Komunikace a ukládání dat končí ve chvíli přenosu posledního prvku databáze


  





TODO

1. načíst data
2. dotaz na databázi
3. akceptace/odmítnutí databází
4. hlavní komunikace
5. ukončení relace
