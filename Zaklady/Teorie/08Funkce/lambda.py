"""
Lambda funkce jsou jednoduché, anonymní, jednořádkové funkce.
Díky tomu že jsou anonymní není možné je opakovaně volat. Na rozdíl od ostatních funkcí jsou tedy zavolány hned při jejich vytvoření.
Snytax
lambda argumenty: provedená funkce
"""
#lambda funkce
lambda x:x
#funkce se stejnou činností jako labda
def vrat(x):
	return x

print((lambda x:x)("Vrácená hodnota lambda"))
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