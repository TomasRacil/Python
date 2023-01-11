from random import randint

def generuj_nahodnou_matici(radky: int, sloupce: int) -> list:
    """Funkce generujici n8hodnou matici radky x sloupce

    Args:
        radky (int): pocet radku pro generaci
        sloupce (int): pocet sloupcu pro generaci

    Returns:
        list: vygenerovana matice
    """
    return [[randint(0,9) for _ in range(sloupce)] for _ in range(radky)]

def vytiskni_matici(matice:list)->None:
    for radek in matice:
        print(radek)
    print()

def secti_matice(A:list, B:list)->list:
    if len(A)==len(B) and len(A[0])==len(B[0]):
        return [[prvek+B[y][x] for x, prvek in enumerate(radek)] for y,radek in enumerate(A)]
    else:
        return []

def vynasob_matice(A:list, B:list)->list:
    if len(A[0])==len(B):
        # vysledek=[]
        # for y, radek in enumerate(A):
        #     radek_v = []
        #     for x,_ in enumerate(B[y]):
        #         temp=0
        #         for y2, prvek in enumerate(A[y]):
        #             temp+=prvek*B[y2][x]
        #         radek_v.append(temp)
        #     vysledek.append(radek_v)
        
        vysledek = [[sum([prvek*B[y2][x] for y2, prvek in enumerate(A[y])]) for x,_ in enumerate(B[y])]for y, radek in enumerate(A)]
        return vysledek
    else:
        return []

radky = 2
sloupce = 2
A = generuj_nahodnou_matici(2,3)
B = generuj_nahodnou_matici(3,2)

vytiskni_matici(A)
vytiskni_matici(B)

vytiskni_matici(secti_matice(A,B))
vytiskni_matici(vynasob_matice(A,B))
# vytiskni_matici(matice)