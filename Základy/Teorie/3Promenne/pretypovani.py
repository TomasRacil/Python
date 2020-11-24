"""
Netypovost jazyka python může být často problémem např. pokud uživatel zadává údaje skrze konzoli vždy budou typu string.
Můžeme například očekávat, že vstup bude int a my s ním budeme provádět nějakou matematickou opreci. 
Pro tyto případy existuje v pythonu takzvaný casting kdy pomocí funkce převedem jeden typ na druhý.
"""

#máme tři typy castingu 
#první int(), který převádí hodnoty typu string a float na integer
string='5'
print(f'1. Hodnota {string} typ {type(string)}\n')

cislo= int(string)
print(f'2. Hodnota {cislo} typ {type(cislo)}\n')

desetineCislo=5.5
print(f'3. Hodnota {desetineCislo} typ {type(desetineCislo)}\n')

cislo= int(desetineCislo)
print(f'4. Hodnota {cislo} typ {type(cislo)}\n')

#druhý float(), který převádí hodnoty typu string a int na float

desetineCislo= float(cislo)
print(f'5. Hodnota {desetineCislo} typ {type(desetineCislo)}\n')

desetineCislo= float(string)
print(f'6. Hodnota {desetineCislo} typ {type(desetineCislo)}\n')

#poslení str(), který převádí hodnoty typu float a int na string

string= str(cislo)
print(f'7. Hodnota {string} typ {type(string)}\n')

string= str(string)
print(f'8. Hodnota {string} typ {type(string)}\n')