"""
Lambda funkce jsou jednoduché, anonymní, jednořádkové funkce.
Díky tomu že jsou anonymní není možné je opakovaně volat. Na rozdíl od ostatních funkcí jsou tedy zavolány hned při jejich vytvoření.
Sytax
lambda argumenty: provedená funkce
"""

#lambda funkce
#lambda x:x
#funkce se stejnou činností jako labda
def vrat(x):
	return x

print((lambda x:x*2)("Vrácená hodnota lambda"))
print(vrat("Vrácená hodnota normální funkce"))


#lambda funkce může být přiřazena k proměné a pak skrze ni volána
soucet = lambda a,b : a+b
print(type(soucet))
print(soucet(5,6))

#Důvodem zavádění lambda funkcí je především zvýšení přehlednosti kódu.

#Lambda může být také využita jako návratová hodnota funkce.

def nasob(n):
  return lambda a : a * n

sestinasobek = nasob(6)

print(sestinasobek(3))

cisla=[1,2,3,4,5,6,7,8,9,10]

sudaCisla=[cislo for cislo in cisla if cislo%2==0]
print(sudaCisla)
sudaCisla=filter(lambda cislo:cislo%2==0,cisla)
print(list(sudaCisla))
def jeSude(cislo):
  return cislo%2==0
sudaCisla=filter(jeSude,cisla)
print(list(sudaCisla))
