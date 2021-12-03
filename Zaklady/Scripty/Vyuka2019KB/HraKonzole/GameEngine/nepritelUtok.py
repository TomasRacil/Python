from GameEngine import *

def nepritelUtok(zivoty):
    print("Nepřítel ti vrací úder, házíš kostkou kolik dostaneš poškození")
    hod=hodKostkou(1,6)
    print("Hodil jsi: " + str(hod))
    if hod == 1:
        print("Nepřítel ti udělil kritické poškození")
        zivoty = zivoty - 2
    elif hod == 2 or hod == 3:
        print("Nepřítel tě zasáhl a ubral ti jeden život")
        zivoty = zivoty - 1
    elif hod == 4 or hod == 5:
        print("Vyhnul jsi se útoku nepřítele")
    elif hod == 6:
        print("Fuuha, jak se říká, co tě nezabije to tě posílí. Získáváš jeden život navíc.")
        zivoty = zivoty + 1
    print("\n")
    return zivoty