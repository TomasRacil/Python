# pro komentování se v pythonu používá # = jednořádkový komentář nebo """ pro více řádků

#print() je funkce sloužící k výpisu na konzoli
print("Hello world!")

#Každý print tiskne na samostatný řádek konzoly
print("Ahoj světe!")

#V pythonu se nedefinuje typ proměné při jejich deklaraci.Python sám určí typ podle vkládané hodnoty
text = "Jaké je tvé křestní jméno: "

#input() je funkce, která přijímá argument typu string pro zobrazení v konzoli a vrací string zadaný uživatelem
krestni=input(text)

#jako v jiných jazycích je možné stringy skládat pomocí operátoru +
print("Jmenuješ se" + krestni)

#Následující řádek ukazuje dynamické chování jazyka, kdy při přiřazení čísla do řetězce automaticky přetypuje proměnou
text=2

#Pro přehlednost přiřadíme int uložený v textu do proměné cislo a text naplníme textem
cislo=text
text="lesson"

"""
Následující řádek vypíše chybu. 
Vzhledem k tomu že je python interpretovaný jazyk, tedy vyhodnocuje příkazy řádek po řádku.
Spustí se program zcela v pořádku a poběží až do chvíle kdy se pokusí interpretovat  tuto chybu.
Důvodem vzniku této chyby jak je možné vidět v chybové hlášce je snaha o skládání dvou různých typů.
"""
#print(text+cislo)

#Pro tisk kombinací různých typů existují tři možnosti
#První využívá operátoru %
print("Hi, %s. This is propably your %s. %s." % (krestni, cislo, text))

#Druhá metody format třídy string 
print("Hello there, {1}. This is propably your {2}. {0}.".format(text, krestni, cislo))

#Třetí je takzvaný formátovaný string. Jedná se o nejpoužívanější metodu neboť je nejpřehlednější, nejkratší a nejflexibilnější.
print(f"Hello there again, {krestni}. This is propably your {cislo}. {text}.")

"""
print() je také schponý provést přetypování většiny proměných na string. 
A vzhledem ke způsobu jak je python vyhodnocován je možné přímo v rámci této funkce provádět různén operace.
"""
tisicileti=2
desetileti=2

#Přetypování
print(print)
print(tisicileti)

#Operace
print("Vytvořeno v roce")
print(tisicileti*1000+desetileti*10)
