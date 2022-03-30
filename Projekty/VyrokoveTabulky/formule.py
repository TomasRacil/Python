from parser import *
def Pocet(s):
    p = 0
    q = 0
    r = 0
    for znak in s:
        if (znak == 'p'): p=1
        elif (znak == 'q'): q=1
        elif (znak == 'r'): r=1
    return (p+q+r)
    
def Parsing(string):
    string = parse(lex(string))
    #co dal? -- prochazet listy v listu ...
    if (type(string) == list):
        pass


    return(string)
def Neg(a):
    #cyklus, prochazi prvky a, prohazuje 1 -> 0 a obracene, vraci je do c
    c = [0,0,0,0,0,0,0,0]
    x = 0
    while (x != len(c)):
        if (a[x]==0): c[x] = 1
        else: c[x] = 0
        x+=1
    return c
def Kon(a, b):
    c = [0,0,0,0,0,0,0,0]
    x = 0
    while (x != len(c)):
        if (a[x]==1 and b[x]==1): c[x] = 1
        else: c[x] = 0       
        x+=1
    return c
def Dis(a, b):
    c = [0,0,0,0,0,0,0,0]
    x = 0
    while (x != len(c)):
        if (a[x]==0 and b[x]==0): c[x] = 0
        else: c[x] = 1        
        x+=1
    return c
def Imp(a, b):
    c = [0,0,0,0,0,0,0,0]
    x = 0
    while (x != len(c)):
        if (a[x]==1 and b[x]==0): c[x] = 0
        else: c[x] = 1        
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
def Vypis():
    pass


p = [0,0,0,0,1,1,1,1]
q = [0,0,1,1,0,0,1,1]
r = [0,1,0,1,0,1,0,1]

# ~ negace, /\ konjunkce, \/ disjunkce, ==> implikace, <=> ekvivalence

parserformule = Parsing("(A /\ B)")
print(parserformule)
parserformule = Parsing("b <=> (a ==> ~a)")
print(parserformule)
print(parserformule[0][2][2])



#formule = Dis(Kon(Neg(p),q),(Ekv(Imp(r,Neg(q)),p)))
#print(formule)
"""
result = Neg(p)
print(result)
result = Kon(p,q)
print(result)
result = Dis(p,q)
print(result)
result = Imp(p,q)
print(result)
result = Ekv(p,q)
print(result)
"""