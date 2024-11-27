MIL_TO_KM:float = 1.60934
GAL_TO_LITRE:float = 3.78541

def prevodMPG_L100(mile_na_galon:float)->float:
    galony_mile:float  = 1 / mile_na_galon
    galony_km:float = galony_mile / MIL_TO_KM
    litry_km:float = galony_km * GAL_TO_LITRE
    litry_100km:float = litry_km * 100
    return litry_100km

def prevodL100_MPG(litry_100km:float)->float:
    galony_100km:float = litry_100km * (1 / GAL_TO_LITRE)
    galony_na_km:float = galony_100km / 100
    galony_na_mili:float = galony_na_km * MIL_TO_KM
    mili_na_galon:float = 1 / galony_na_mili
    return mili_na_galon

if __name__ =="__main__":
    vyber: str = input("Chcete zahajit prevod MPG na L/100km (L) nebo L/100km na MPG (G)?")
    
    match vyber:
        case 'L':
            vstup_prevod: float = float(input("Zadej pocet mili na galon: "))
            print(f"Spotreba v litrech je: {prevodMPG_L100(vstup_prevod)}")
        case 'G':
            vstup_prevod:float = float(input("Zadej pocet l na 100 km: "))
            print(f"Kolik mili na galon: {prevodL100_MPG(vstup_prevod)}")
        case _:
            print("Toto neni platna volba")