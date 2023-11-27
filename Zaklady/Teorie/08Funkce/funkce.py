"""
Podobně, jako v ostatních programovacích jazycích, se funkce v pythonu používají pro často se opakujicí bloky kódu, nebo pro zvýšeni přehlednosti.
Funkce musí být prvně nadefinována a to pomicí výrazu def a následně zavolána aby byl daný blok kódu proveden.
Při psaní funkcí je v pythonu důležité zohlednit to že se jedná o interpretovaný jazyk. Funkce tak nemohou být volány v programu dřív než jsou nadefinovány.
"""

#Příklad základní funkce, která nevykonává žádnou činnost.
#def určuje zčátek deklarace funkce; následuje název funkce; do závorek je pak možné vkládat parametry funkce
def funkce()->None:
	#veškerý kód v rámci funkce musí být patřičně odsazený
	pass	#pass je univerzální výraz který interpretovi říká ať pokračuje na dalším řádku

#ukázka volání funkce
funkce()



#následující funkce přijímá dva parametry a pokusí se na ně uplatnit operátor +
def sectiAVypis(a:int,b:int)->None:
	print(f"Soucet {a+b}")

print("Sečti dva prvky")
prvni=input("Vložte  první prvek: ")
druhy=input("Vložte  druhý prvek: ")
#Na následujícím řádku voláme funkci sectiAVypis a jako argumenty jí předáváme data zadaná uživatelem do konzole
sectiAVypis(prvni,druhy)



#Na následujícím případě je demonstrována schopnost vracet hodnoty pomocí funkce. 
#Není nutné typ vracené proměné nijak specifikovat narozdíl od mnoha ostatních programovacích jazyků.
def vrat(a:int):
	if a != 6:
		return a
	else:
		pass

print(f'A je 3: {vrat(3)}')
#Pokud zavoláme funkci s argumentem 6 funkce nemá žádnou návratovou hodnotu, ale i přesto nevyvolá chybu.
#V tomto případě funke vrátí defultní třídu NoneType.
print(f'A je 6: {vrat(6)}')



#Pokud předem nedokážeme určit kolik argumentů bude funkce přebírat. Můžeme použít operátor * před parametrem funkce.
#Následující funkce vezme jakýkoliv počet parametrů a vytvoří z nich seznam. K tomu můžeme pak libovolně přistupovat.
#Většinou se používá jméno *arg (argumenty) pro ukázku je zde však použito pojmenování *jazyky.
def vypisJazyky(*jazyky):
	try:
		print(f"Umím tyto programovací jazyky {jazyky}")
		print(f"Tento jsem napsal první: {jazyky[0]}; a tento poslední: {jazyky[-1]}")
	except Exception as e:
		print(e)

#Jednoduché volání možné vložit libovolý počet prvků
vypisJazyky('C#','C++','Kobol')

#Ukázka s uživatelským vstupem a rozbalením seznamu do skupiny proměných
pokracuj=True
jazyky=[]
while pokracuj:
	inp=input("Zadej programovací jazyk co znáš (nebo zadej q pro ukončení)")
	if inp!='q':
		jazyky.append(inp)
	else:
		pokracuj=False

vypisJazyky(*jazyky) #*před seznamem ho rozbalí a zapíše ve formátu jazyk[0], jazyk[1], ...



#Zatím byly všechny argumety vyhodnocovány na základě jejich pořadí, ale můžeme využít také klíče (názvu parametru) a hodnoty(argumentu).
def deleni(delenec,delitel):
	print(f"podíl je {delenec/delitel}")
#Pokud používáme názvů parametrů můžeme argumety přiřadit v jakémkoliv pořadí
deleni(delitel=2,delenec=8)


#Pokud chceme aby byly parametry volitelné můžeme u nich nastavit defaultní hodnotu.
def helloWorld(text:str="Hello world!"):
	print(text)

helloWorld()



#Pokud chceme do funkce poslat množinu klíčů a hodnot o neznámé velikost využíváme **. 
#Funguje podobně jako *, ale předává dictonary obsahující klíče a hodnoty.
#Zde se většinou používá pojmenování **kwargs (keyword argument) pro ukázku je zde použito **studenti
def vypisStudenty(**studenti):
	for k,v in studenti.items():
		print (f"{k},{v}")

vypisStudenty(student1="Tomas",student2="Jakub",student3="Josef")



#Posledním důležitým bodem pro zmínění je rekurzíva, kterou python samozřejmě umožňuje.
#Ukázka rekurzivního kódu pro výpočet faktoriálu.
def recurFaktorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recurFaktorial(n-1)

print(recurFaktorial(6))