from parser import *


def Pocet(s):
    p = 0
    q = 0
    r = 0
    for znak in s:
        if znak == "p":
            p = 1
        elif znak == "q":
            q = 1
        elif znak == "r":
            r = 1
    return p + q + r


def Parsing(string):
    string = parse(lex(string))
    # co dal? -- prochazet listy v listu ...
    if type(string) == list:
        pass

    return string


def Neg(a):
    # cyklus, prochazi prvky a, prohazuje 1 -> 0 a obracene, vraci je do c
    c = [0, 0, 0, 0, 0, 0, 0, 0]
    x = 0
    while x != len(c):
        if a[x] == 0:
            c[x] = 1
        else:
            c[x] = 0
        x += 1
    return c


def Kon(a, b):
    c = [0, 0, 0, 0, 0, 0, 0, 0]
    x = 0
    while x != len(c):
        if a[x] == 1 and b[x] == 1:
            c[x] = 1
        else:
            c[x] = 0
        x += 1
    return c


def Dis(a, b):
    c = [0, 0, 0, 0, 0, 0, 0, 0]
    x = 0
    while x != len(c):
        if a[x] == 0 and b[x] == 0:
            c[x] = 0
        else:
            c[x] = 1
        x += 1
    return c


def Imp(a, b):
    c = [0, 0, 0, 0, 0, 0, 0, 0]
    x = 0
    while x != len(c):
        if a[x] == 1 and b[x] == 0:
            c[x] = 0
        else:
            c[x] = 1
        x += 1
    return c


def Ekv(a, b):
    c = [0, 0, 0, 0, 0, 0, 0, 0]
    x = 0
    while x != len(a):
        if a[x] == b[x]:
            c[x] = 1
        else:
            c[x] = 0
        x += 1
    return c

def solve(prvek: list) -> list:
    """Recursively solve ...

    Args:
        prvek (list): _description_

    Returns:
        list: _description_
    """
    konec = False
    repetition = int(len(prvek) / 2) 
    if isinstance(prvek[0], list):  #instance() = kdyz prvek[0] je list pak:
        prvni = solve(prvek.pop(0)) #priradi prvni 0.prvek - tedy list v listu - a smaze ho, zavola znovu funkci solve
    else:
        if (prvek[0].endswith('~')):    #pro pripad ze je vice negaci za sebou
            if ((prvek[0].count('~')%2)==1): #negace rusi negaci...sudy pocet negaci = zadna negace
                if isinstance(prvek[1], list): #jak vyresit
                    prvek.pop(0)
                    prvni = Neg(solve(prvek.pop(0)))    #!!!CHYBA!!! po vyhodnoceni jede zase dal
                    konec = True                                        
                else:
                    repetition-=1
                    prvek.pop(0)
                    prvni = Neg(matrices[prvek.pop(0)]) 
            else: #neni negace
                prvek.pop(0)
                prvni = matrices[prvek.pop(0)]  
        else: prvni = matrices[prvek.pop(0)]    
    k = False
    for _ in range(repetition):
        if konec: break 
        op = prvek.pop(0) #priradim dalsi prvek operaci a smazu

        if isinstance(prvek[0], list):
            druhy = solve(prvek.pop(0))
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

def Vypis():
    pass

operations = {"and": Kon, "or": Dis, "iff": Ekv, "implies": Imp, "~": Neg}

matrices = {
    "A": [0, 0, 0, 0, 1, 1, 1, 1],
    "B": [0, 0, 1, 1, 0, 0, 1, 1],
    "C": [0, 1, 0, 1, 0, 1, 0, 1],
}

# ~ negace, /\ konjunkce, \/ disjunkce, ==> implikace, <=> ekvivalence

formule1 = Parsing("(~((A /\ B) ==> ~(B <=> ~C)))")
print(formule1)
print(solve(formule1))
