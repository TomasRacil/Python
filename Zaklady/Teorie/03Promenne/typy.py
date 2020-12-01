"""
U proměný v pythonu nedefinujeme typ sami, ale je sám identifikován při jejich vytvoření.
Pro kontrolu typu proměné využíváme vestavěné funkce type().
Jak bude možné vidět na výstupu, každá proměná je třídou s vlastními metodami, 
ty budou později podrobněji rozebírány v dalších lekcích, nebo je možné je dohledat v dokumentaci.
"""

#klasický int; velikost není limitovaná ničím kromě paměti zařízení; jediný typ celých čísel, terý python vnitřně používá
integer = 1
print(f"hodnota {integer} typ {type(integer)}")

#zápis binárního čísla
binary = 0b10
print(f"hodnota {binary} typ {type(binary)}")

#zápis čísla osmičkové soustavy
octal = 0o10
print(f"hodnota {octal} typ {type(octal)}")

#zápis čísla šestnásctkové soustavy
hexadecimal = 0x10
print(f"hodnota {hexadecimal} typ {type(hexadecimal)}")

#Jak je vidět na výstupu python přijíma čísla v různých soustavách, ale převádí je na svůj univerzální typ int.

#zápis čísla s plovoucí desetinou čárkou; opět bez omezení velikosti; dva způsoby
floatingPointNumber= 2.58
print(f"hodnota {floatingPointNumber} typ {type(floatingPointNumber)}")

#rozeznává také vědecký zápis
floatingPointNumber = 4.2e-4
print(f"hodnota {floatingPointNumber} typ {type(floatingPointNumber)}")

#komplexní čísla opět bez omezení 
complexNumber = 2+3j
print(f"hodnota {complexNumber} typ {type(complexNumber)}")

#řetězce je možné zapisovat třemi způsoby pomocí dvojitých uvozovek, jednoduchých uvozovek, anebo je uzavřít mezi trojici uvozovek.
text1="Ahoj "
text2='světe!'
print(f"hodnoty: {text1}, {text2} typ {type(text1)}, {type(text2)}")
text3="""
Mezi trojící uvozovek je text ukládán
ve stejném formátu jako byl napsán
včetně řádků 
	a odstavců
"""
print(f"hodnota: {text3} typ {type(text3)}")

#dalším základním datovým typem je binární proměná boolean; python je casesensitive True/False musí začínat velkým písmenem.
boolean = True
print(f"hodnota {boolean} typ {type(boolean)}")




