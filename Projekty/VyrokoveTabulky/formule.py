def Parsing(formule):
   pass
def Neg(a):
    #cyklus, prochazi prvky a, prohazuje 1 -> 0 a obracene, vraci je do c
    c = [0,0,0,0,0,0,0,0]
    x = 0
    while (x != len(c)):
        
        x+=1
    return c
def Kon(a, b):
    c = [0,0,0,0,0,0,0,0]
    x = 0
    while (x != len(c)):
        
        x+=1
    return c
def Dis(a, b):
    c = [0,0,0,0,0,0,0,0]
    x = 0
    while (x != len(c)):
        
        x+=1
    return c
def Imp(a, b):
    c = [0,0,0,0,0,0,0,0]
    x = 0
    while (x != len(c)):
        
        x+=1
    return c
def Ekv(a, b):
    c = [0,0,0,0,0,0,0,0]
    x = 0
    while (x != len(a)):
        if (a[x]==b[x]): c[x] = 1
        else: c[x] = 0
        x+=1
    return c

p = [0,0,0,0,1,1,1,1]
q = [0,0,1,1,0,0,1,1]
r = [0,1,0,1,0,1,0,1]

result = Ekv(p,q)
print(result)
