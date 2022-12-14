"""Program s funkcí pro počítání prvočísel"""

def najdi_prvocisla(zacatek: int, konec: int)->list[int]:
    """Funkce najde vsechny prvocisla v danem rozsahu

    Args:
        zacatek (int): zacatek rozsahu
        konec (int): konec rozsahu

    Returns:
        list[int]: nalezena prvocisla
    """
    prvocisla=[]
    for cislo in range(zacatek,konec+1): # cyklus, ktery prochazi vsechny cisla od zacatku do konce
        # print(cislo%(cislo-1))
        prvocislo=True
        for delitel in range(2,cislo//2):
            #u kazdeho cisla overime zdali je delitelne vsemi cisly nizsim
            if cislo%delitel==0:
                prvocislo=False # neni prvocislo
                break
        if prvocislo:
            prvocisla.append(cislo)


    return prvocisla

print(najdi_prvocisla.__doc__)
print(najdi_prvocisla(2,100000000))
