from random import randint

# num_str={1:"kamen",2:"nuzky",3:"papir"}
# num_str=["kamne","nuzky","papir"]

def preved_ciselny_vstup_na_retezec(ciselny_vstup):
    """Tato funkce prevadi ciselny vstup 1-3 na kamen, nuzky, papir
	
	Args:
		ciselny_vstup (int): hodnota, ktera ma byt prevedena na retezec; hodnota 1-3

	Returns:
		str: return retezec reprezentující hodnotu
	"""

    cislo_kam_nuz_pap={
        1:"kamen",
        2:"nuzky",
        3:"papir"
        }

    return cislo_kam_nuz_pap.get(ciselny_vstup,"hodnota nenalezena")


def hraj():
    pc_vstup = randint(1,3)

    # if cislo==1: generovano="kamen"
    # elif cislo ==2: generovano="nuzky"
    # else: generovano="papir"
    
    #generovano=num_str[cislo]
    pc_vstup_str=preved_ciselny_vstup_na_retezec(pc_vstup)
    print(pc_vstup,pc_vstup_str)

    vstup=int(input("Zadej pro 1-kamen; zadej 2-nuzky; zadej 3-papir: "))
    
    # if (vstup==1): vstup_str="kamen"
    # elif (vstup==2): vstup_str="nuzky"
    # else: (vstup_str)="papir"
    vstup_str=preved_ciselny_vstup_na_retezec(vstup)

    print(vstup,vstup_str)

    if(vstup==pc_vstup):
        print(f"remiza \nsouper {pc_vstup_str} \nvs \nty {vstup_str}")
    # elif((vstup==1 and cislo==2) or (vstup==2 and cislo ==3)or(vstup==3 and cislo ==1)): #moznost upravit
    #     print(f"vyhra \nsouper {generovano} \nvs \nty {vstup_str}")
    elif(vstup==pc_vstup-1 or vstup==pc_vstup+2): 
        print(f"vyhra \nsouper {pc_vstup_str} \nvs \nty {vstup_str}")
    else:
        print(f"prohra \nsouper {pc_vstup_str} \nvs \nty {vstup_str}")

#if __name__ == "__main__":
hraj()


