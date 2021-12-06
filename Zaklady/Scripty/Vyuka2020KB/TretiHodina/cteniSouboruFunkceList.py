from time import time	
from timeit import timeit

def bruteForce(roky):

    nalezeno=False

    for rok in roky[:101]:
        for rok2 in roky:
            if rok+rok2==2020:
                print(rok,rok2)
                nalezeno=True
                break
        if nalezeno: break


def presZbytek(roky):
    for rok in roky[:101]:
        zbytek=2020-rok
        if zbytek in roky: 
            print(rok,zbytek)
            break


with open("test.txt", "r") as soubor:


    roky=[int(radek.strip()) for radek in soubor]
    #roky.sort()
    # zac=time()
    zac=timeit()
    bruteForce(roky)
    kon=timeit()
    print(kon-zac)
    # print(time()-zac)
    # zac=time()
    roky.sort()
    presZbytek(roky)
    kon=timeit()
    print(kon-zac)
    # print(time()-zac)
