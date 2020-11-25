"""
Datové struktury jsou kolekce prvků. 
Prvky mohou být proměnné, datové struktury a nebo dokonce funkce.
V pythonu máme čtyři základní datové struktury.
"""


#List (seznam) je velice podobný datové struktuře pole používané v jiných jazycích.
#deklaraci seznamu provádíme pomocí hranatých závorek, které naplníme hodnotami oddělenými pomocí čárek
ukazkovySeznam = ['první prvek','druhý prvek','...']
print(f'obsah listu: {ukazkovySeznam} a typ {type(ukazkovySeznam)}\n')
#Seznam má dané pořadí je možné ho měnit a umožňuje ukládat stejné hodnoty

#Druhým typem datové struktury je takzvaný Tuple (n-tice)
#deklaraci provádíme pomocí kulatých závorek, které naplníme hodnotami oddělenými pomocí čárek
ukazkovyTuple = ('první prvek', 'druhý prvek','...')
print(f'obsah tuple: {ukazkovyTuple} a typ {type(ukazkovyTuple)}\n')
#Tuple má pořadí, neumožňuje změny a umožňuje ukládat stejné hodnoty

#Třetím typem je Set
#deklarujeme ho pomocí složených závorek, které naplníme hodnotami oddělenými pomocí čárek
ukazkovySet = {'první prvek', 'druhý prvek','...'}
print(f'obsah setu: {ukazkovySet} a typ {type(ukazkovySet)}\n')
#nemá pořadí, neumožňuje změny  a neumožňuje ukládat stejné hodnoty

#Čtvrým a posledním typem je dictionary (slovník)
#deklarujeme ho pomocí složených závorek, uvnitř ktrých mám vždy klíč:hodnota oddělených čárkami
ukazkovyDict= {'Jmeno':'Tomáš','Prijmeni':'Ráčil', 'Dalsi':'...'}
print(f'obsah slovníku: {ukazkovyDict} a typ {type(ukazkovyDict)}\n')
#nemá pořadí, umožňuje změny  a neumožňuje ukládat stejné hodnoty

#Na všechny datové struktury podbně jako u stringu můžeme použít funci len(datová struktura) pro získání její délky
print(f"Délka ukázkového seznamu: {len(ukazkovySeznam)}")