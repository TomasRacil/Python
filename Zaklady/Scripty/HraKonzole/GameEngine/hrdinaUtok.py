from GameEngine import *

def hrdinaUtok(nepritelHP):
    print("Házíš kostkou kolik udělíš poškození")
    hod=hodKostkou(1,6)
    print("Hodil jsi: " + str(hod))
    if hod == 1:
        print("Zakopl jsi a útok úplně minul")
    elif hod == 6:
        print("Použil jsi své umění KungFu a udělil nepříteli dvojnásobné poškození")
        nepritelHP = nepritelHP - 2
    else:
        print("Zasáhl jsi nepřítele a ubral mu jeden život")
        nepritelHP = nepritelHP - 1
    print("\n")
    return nepritelHP