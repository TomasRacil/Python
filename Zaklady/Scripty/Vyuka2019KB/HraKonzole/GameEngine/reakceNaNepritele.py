from GameEngine import *

#prosim nemazat

def reakceNaNepritele(enemyHP, heroHP):
    nepritelHP = enemyHP
    zivoty = heroHP
    konec = False
    while not konec:
        volba=False
        while not volba:
            volba=input("Vyber co uděláš:\n 1 utéct\n 2 bojovat\n")
            if volba=='1':
                volba=True
                print("Házíš kostkou pro rychlost útěku 1-12")
                hod=hodKostkou(1,12)
                print("Hodil jsi: " + str(hod))
                if hod<=4:
                    print("Nepodařilo se ti utéct, budeš muset bojovat\n")
                    nepritelHP = HrdinaUtok(nepritelHP)
                    zivoty = nepritelUtok(zivoty)
                elif hod>4:
                    print("Dnes je tvůj šťastný den, úspěšně jsi utekl před banditem, stálo tě to 2 energie.\n")
                    konec = True
                    break
                    ##energie=energie-2
            if volba=='2':
                volba=True
                print("Rozhodl jsi se bojovat\n")
                nepritelHP = HrdinaUtok(nepritelHP)
                zivoty = nepritelUtok(zivoty)
            else:
                volba=False

        print("Tvé životy: ",zivoty," | Životy nepřítele: ",nepritelHP,"\n")
        if zivoty <= 0:
            print("Zemřel jsi KONEC HRY\n")
            konec = True
        if nepritelHP <= 0:
            print("Výborně zabil jsi nepřítele, můžeš pokračovat dále\n")
            konec = True