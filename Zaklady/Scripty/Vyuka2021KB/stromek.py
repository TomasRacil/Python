def stromek_1(vyska:int):
    for cislo in range(1,vyska+1):
        print("*"*cislo)

def stromek_2(vyska:int):
    for cislo in range(1,vyska+1):
        print(" "*(vyska-cislo)+"*"*(2*cislo-1))
        
def stromek_3(vyska:int, polomer_parezu:int = 1, vyska_parezu:int =2):
    stromek_2(vyska)
    for cislo in range(1,vyska_parezu+1):
        print(" "*(vyska-polomer_parezu-1)+"#"*(polomer_parezu*2+1))

# vyska=input("Zadej vysku: ")
# stromek_3(5)
vyska,polomer_parezu,vyska_parezu =5, 1, 2
stromek = "\n".join([
    " "*(vyska-cislo)+"*"*(2*cislo-1) 
    for cislo in range(1,vyska+1)
    ] + [
        " "*(vyska-polomer_parezu-1)+"#"*(polomer_parezu*2+1) 
        for cislo in range(1,vyska_parezu+1)
        ] )
print(stromek)