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


def Vypis():
    pass


p = [0, 0, 0, 0, 1, 1, 1, 1]
q = [0, 0, 1, 1, 0, 0, 1, 1]
r = [0, 1, 0, 1, 0, 1, 0, 1]

# ~ negace, /\ konjunkce, \/ disjunkce, ==> implikace, <=> ekvivalence

matrices = {
    "A": [0, 0, 0, 0, 1, 1, 1, 1],
    "B": [0, 0, 1, 1, 0, 0, 1, 1],
    "C": [0, 1, 0, 1, 0, 1, 0, 1],
}

parserformule1 = Parsing("(A /\ (B<=>C) /\ A)")
print(parserformule1)
parserformule2 = Parsing("b <=> (a ==> ~a)")
print(parserformule2)
print(parserformule2[0][2][2])

operations = {"and": Kon, "iff": Ekv, "implies": Imp, "~": Neg}

# formule = Dis(Kon(Neg(p),q),(Ekv(Imp(r,Neg(q)),p)))
# print(formule)
# op = "~"
# print(operations[op](p))


def solve(vyrok: list) -> list:
    """Recursively solve ...

    Args:
        vyrok (list): _description_

    Returns:
        list: _description_
    """

    repetition = int(len(vyrok) / 2)
    if isinstance(vyrok[0], list):
        prvni = solve(vyrok.pop(0))
    else:
        prvni = matrices[vyrok.pop(0)]
    for _ in range(repetition):
        op = vyrok.pop(0)
        druhy = (
            solve(vyrok.pop(0))
            if isinstance(vyrok[0], list)
            else matrices[vyrok.pop(0)]
        )
        prvni = operations[op](prvni, druhy)
    return prvni


print(solve(parserformule1))

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
