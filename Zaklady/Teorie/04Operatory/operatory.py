"""
Jazyk python disponuje celou sadou operátorů velice podobnou operátorům nalezeným v ostatních jazycích.
Aritmetické operátory - využívané především v matematických operacích
Operátory přiřazení - sloužící k přiřazení a upravě hodnot proměnných
Operátory porovnání - poskytující možnosti porovnání proměnných
Logické operátory - sloužící k práci s hodnotami boolean (True/Flase)
Operátory příslušnosti - zjišťující přislušnost k dané množině
Binární operátory - zajišťující operce s binárními čísly
"""


#aritmetické operátory jsou 
#	+ 		Sčítání
print(f'Sčítat můžeme čísla stejného typu {6+6},')
print(f'ale i různých typů {6+6.5}')
print(f'Sčítat můžeme'+'i řetězce')

#	- 		Odčítání
print(f'Stejně jako u sčítaní,\n odčítat můžeme čísla stejného typu {6-6},')
print(f'ale i různých typů {6-6.5}')

#	*		Násobení
print(f'Násobit můžeme čísla stejného typu {6*6},')
print(f'ale i různých typů {6*6.5}')
print(f'Násobit můžeme i řetězce. '*3)

#	/		Dělení
print(f'Stejně jako u dělení,\n dělit můžeme čísla stejného typu {6/6},')
print(f'ale i různých typů {6/6.5}')

#	%		Modulus
print(f'Modulus můžeme použít u stejných typů {7%6},')
print(f'ale i různých typů {7%6.5}')

#	**		Mocnění
print(f'Mocnit můžeme stejné typy {2**2},')
print(f'ale i různé typy {4**0.5}')

#	//		Dělení na nejnižší celé číslo
print(f'Dělení na nejnižší celé číslo je možné použít na stejné typy {7//2},')
print(f'ale i různé typy {9//3.5}')



#operátory přiřazení
#	=		Přiřazení hodnoty funkční pro všechny typy proměnných
x=5
text='text'
print(x,text)

#	+=		Přičtení a přiřazení hodnoty pouze u proměných u kterých je možné použít operátor +								x = x + 3	
x+=5
text+=' text2'
print(x,text)

#	-=		Odečtení a přiřazení hodnoty pouze u proměných u kterých je možné použít operátor -								x = x - 3	
x-=5
print(x)

#	*=		Vynásobení a přiřazení hodnoty pouze u proměných u kterých je možné použít operátor *							x = x * 3
x*=5
text*=2
print(x,text)

#	/=		Vydělení a přiřazení hodnoty pouze u proměných u kterých je možné použít operátor /								x = x / 3
x/=2
print(x)

#	%=		Modulus a přiřazení hodnoty pouze u proměných u kterých je možné použít operátor %								x = x % 3
x%=17
print(x)

#	//=		Dělení na nejnižší celé číslo a přiřazení hodnoty pouze u proměných u kterých je možné použít operátor //		x = x // 3
x//=5
print(x)

#	**=		Umocnění a přiřazení hodnoty pouze u proměných u kterých je možné použít operátor **							x = x ** 3	
x**=3
print(x)



#operátory porovnání jsou 
#	== 		True pokud jsou si prvky rovny
print(f'12 se rovná  12: {12==12}')

#	!= 		True pokud si prvky nejsou rovny
print(f'12 se nerovná 12: {12!=12}')

#	> <		True pokud jsou prvky (větší/menší)
print(f'12 je menší 12: {12<12}')

#	>= <=	True pokud jsou prvky (větší nebo rovny/menší nebo rovny)
print(f'12 se menší nebo rovno 12: {12<=12}')


#logické operátory 
#	and 	True pokud jsou obě tvrzení pravdivá
print(f'pravda a lež je: {True and False}')

#	or  	True pokud je alespoň jedno tvrzení pravdivé
print(f'pravda nebo lež je: {True or False}')

#	not 	negace tvrzení
print(f'opak pravdy je: {not True}')



#operátory typu
text,cislo="text",8

# 	is		True pokud jsou obě proměné stejného typu
print(f'je {text} a {cislo} stejného typu: {text is cislo}')

# 	is not 	True pokud jsou rozdílného typu
print(f'není {text} a {cislo} stejného typu: {text is not cislo}')



#operátory příslušnosti uplatnitelný na všechny datové struktury a řetězce
seznam = ['python','go','kotlin']
prvek = 'python'

#	in 		True pokud je tato hodnota přítomná v objektu
print(f'je {prvek} v {seznam}: {prvek in seznam}')

#	not in 	True pokud je tato hodnota není přítomná v objektu
print(f'není {prvek} v {seznam}: {prvek not in seznam}')



"""
Pro operace s binárními čísly se používají operátory (&,|,^,~,<<,>>)
Vzhledem k povaze pythonu jich nebývá příliš často používáno.
Proto je zde nebudeme nijak více rozebírat
"""