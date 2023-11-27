def koruna(vyska:int=5)->None:
    """Generator koruny

    Args:
        vyska (int, optional): Vyska vzgenerovane koruny. Defaults to 5.
    """
    for i in range(vyska):
        print(" "*(vyska-i-1),"*"*(2*i+1))


def kmen(vyska_stromu:int=5, vyska_kmene:int =3, sirka:int=3)->None:
    for _ in range(vyska_kmene):
        print(" "*int(vyska_stromu-sirka/2),"#"*sirka)

koruna()
kmen()

print(koruna.__doc__)

cisla=[1,2,3,4,5,6]
cisla2 = []
for cislo in cisla:
    cisla2.append(cislo+1)
vetsi_cisla = [cislo+1 for cislo in cisla]
print(vetsi_cisla)
