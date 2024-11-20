print(f'Sčítat můžeme čísla stejného typu {6+6},')
print(f'ale i různých typů {6+6.5}')
print(f'Sčítat můžeme'+'i řetězce')

print(f'Stejně jako u sčítaní,\n odčítat můžeme čísla stejného typu {6-6},')
print(f'ale i různých typů {6-6.5}')

print(f'Násobit můžeme čísla stejného typu {6*6},')
print(f'ale i různých typů {6*6.5}')
print(f'Násobit můžeme i řetězce. '*3)

print(f'Stejně jako u dělení,\n dělit můžeme čísla stejného typu {6/6},')
print(f'ale i různých typů {6/6.5}')

print(f'Modulus můžeme použít u stejných typů {7%6},')
print(f'ale i různých typů {7%6.5}')

print(f'Mocnit můžeme stejné typy {2**2},')
print(f'ale i různé typy {4**0.5}')

print(f'Dělení na nejnižší celé číslo je možné použít na stejné typy {7//2},')
print(f'ale i různé typy {9//3.5}')

x=5
text='text'
print(x,text)

x+=5
text+=' text2'
print(x,text)

x-=5
print(x)

x*=5
text*=2
print(x,text)

x/=2
print(x)

x%=17
print(x)

x//=5
print(x)

x**=3
print(x)

print(f'12 se rovná  12: {12==12}')
print(f'12 se nerovná 12: {12!=12}')
print(f'12 je menší 12: {12<12}')
print(f'12 se menší nebo rovno 12: {12<=12}')

print(f'pravda a lež je: {True and False}')
print(f'pravda nebo lež je: {True or False}')
print(f'opak pravdy je: {not True}')

seznam = ['python','go','kotlin']
prvek = 'python'

print(f'je {prvek} v {seznam}: {prvek in seznam}')
print(f'není {prvek} v {seznam}: {prvek not in seznam}')

text,cislo="text",8

print(f'je {text} a {cislo} stejného typu: {text is cislo}')
print(f'není {text} a {cislo} stejného typu: {text is not cislo}')