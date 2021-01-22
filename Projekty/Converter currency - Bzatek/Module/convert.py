from .kontrolaVstupu import *
from .exchangeratesapi import DostanKurzy

def UdelatPrevod(dostupneMeny):
    """
    nejprve zazada vstupni informace
    provede vypocet
    zaokrouhli
    vytiskne
    """
    print("Kterou menu chcete prevest?")
    menaVstup=ZadejMenu(dostupneMeny)
    print("Jakou castku chcete prevest?")
    castkaVstup=zadatInt()
    print("Na kterou menu chcete prevest?")
    menaVystup=ZadejMenu(dostupneMeny)

    castkaVystup=ProvedVypocet(menaVstup,menaVystup,castkaVstup)
    castkaVystup=round(castkaVystup*100)/100.0
    print(castkaVstup+" "+menaVstup+" prevedeno na "+str(castkaVystup)+" "+menaVystup)

def ProvedVypocet(menaVstup,menaVystup,castkaVstup):
    kurzy=DostanKurzy(menaVstup)
    kurz=0
    for i in range(len(kurzy)):
        if kurzy[i][0]==menaVystup:
            kurz=kurzy[i][1]
            break
    vystup=float(castkaVstup)*float(kurz)
    
    return vystup


