import re
from .parser import *

#vytvorit dynamicky
def Vyroky(s):
    """
    funkce hledá, jaké výroky se vyskytují v řetezci
    argumenty: s (string)
    vrací: vyroky (list)
    """
    vyroky=set(re.findall(r'[a-zA-Z]',s))
    return (sorted(vyroky))

def FillList(amount,step):
    """
    naplní pole 0 a 1
    argumenty: amount (int), step (int)
    výstup: list (list)
    """
    list = []
    k = 0
    for i in range(0,2**amount,step):
        for j in range(step):
            list.append(k%2)
        k+=1
    return list    

def SetMatrices(s):
    """
    Vytvoří matici výroků ve formě dictionary... "označení výroku" : pole naplněné 0 a 1
    argumenty: s (string)
    vrací: matrices (set)
    """
    matrices = {}
    vyroky = Vyroky(s)
    steps = 1
    for vyrok in vyroky:
        matrices.update({vyrok:FillList(len(vyroky),steps)}) 
        steps = steps*2
    return matrices

def Parsing(string):
    string = parse(lex(string))
    return string

def Neg(a):
    c = []
    x = 0
    while x != len(a):
        if a[x] == 0:
            c.append(1)
        else:
            c.append(0)
        x += 1
    return c
def Kon(a, b):
    c = []
    x = 0
    while x != len(a):
        if a[x] == 1 and b[x] == 1:
            c.append(1)
        else:
            c.append(0)
        x += 1
    return c
def Dis(a, b):
    c = []
    x = 0
    while x != len(a):
        if a[x] == 0 and b[x] == 0:
            c.append(0)
        else:
            c.append(1)
        x += 1
    return c
def Imp(a, b):
    c = []
    x = 0
    while x != len(a):
        if a[x] == 1 and b[x] == 0:
            c.append(0)
        else:
            c.append(1)
        x += 1
    return c
def Ekv(a, b):
    c = []
    x = 0
    while x != len(a):
        if a[x] == b[x]:
            c.append(1)
        else:
            c.append(0)
        x += 1
    return c

def Solve(matrices, prvek: list) -> list:
    """
    rekurzivní funkce 
    argumenty: matrices (dictionary), prvek (list)
    vrací: prvni (list)
    """
    konec = False
    repetition = int(len(prvek) / 2) 
    if isinstance(prvek[0], list):
        prvni = Solve(matrices, prvek.pop(0)) #priradi prvni 0.prvek - tedy list v listu - a smaze ho, zavola znovu funkci solve
    else:
        if (prvek[0].endswith('~')):    #pro pripad ze je vice negaci za sebou
            if ((prvek[0].count('~')%2)==1): #negace rusi negaci...sudy pocet negaci = zadna negace
                if isinstance(prvek[1], list):
                    prvek.pop(0)
                    prvni = Neg(Solve(matrices, prvek.pop(0)))
                    konec = True                                        
                else:
                    repetition-=1
                    prvek.pop(0)
                    prvni = Neg(matrices[prvek.pop(0)]) 
            else: #neni negace
                repetition-=1
                prvek.pop(0)
                prvni = matrices[prvek.pop(0)]  
        else: prvni = matrices[prvek.pop(0)]    
    k = False
    for _ in range(repetition):
        if konec: break 
        op = prvek.pop(0) #priradim dalsi prvek operaci a smazu

        if isinstance(prvek[0], list):
            druhy = Solve(matrices, prvek.pop(0))
        else:
            if (prvek[0].endswith('~')):
                k = True
                if ((prvek[0].count('~')%2)==1):   
                    prvek.pop(0)                
                    druhy = Neg(matrices[prvek.pop(0)])
                else:
                    prvek.pop(0)
                    druhy = matrices[prvek.pop(0)]
            else: druhy = matrices[prvek.pop(0)]
        prvni = operations[op](prvni, druhy)
        if k: break
    return prvni

def Vypis(matrices,formule,result):
    """
    Vypíše do konzole naformátovanou tabulku pravdivostních hodnot
    argumenty: matrices (set), formule (string), result (list)
    """
    print()
    #hlavicka
    vyroky = Vyroky(formule)
    o = 0
    for v in vyroky:
        print(v,end ="   ")
        o+=1
    print("|  ",formule)
    #oddelovac
    print(o*"––––",end = "|–––––––––––––––––––––––––––––––––––––––––––––––\n", )
    #tabulka
    for i in range(0,2**len(vyroky),1):
        for j in vyroky:
            print(matrices[j][i], end = "   ")
        print("|  ",result[i])

operations = {"and": Kon, "or": Dis, "iff": Ekv, "implies": Imp, "~": Neg}
# ~ negace, /\ konjunkce, \/ disjunkce, ==> implikace, <=> ekvivalence

