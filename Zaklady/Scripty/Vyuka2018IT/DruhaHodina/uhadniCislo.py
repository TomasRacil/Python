from random import randint

cislo = randint(0,100)

print(cislo)

#trefa=True

score=0

while True:

    while True:
        try:
            tip=int(input("Hadej cislo: "))

            if tip==cislo:
                print("Cislo uhadnuto")
                score+=1
                break
        
            elif (cislo-tip)>=10 or (tip-cislo)>=10:
                print("jsi daleko")
            elif (cislo-tip)<=10 or (tip-cislo)<=10:
                print("prihoriva")
            
            if cislo>tip: print("cislo je vetsi")
            else:print("cislo je mensi")
        
        except ValueError:
            print("Toto neni cislo zadej znovu")
    
    print(f"Score je: {score}")
    pokracovat = input("chcete hrat znovu? (y/n)")
    if pokracovat=='n':  break

    
    