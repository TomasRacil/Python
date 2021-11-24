
jmeno=input("Zadej křestní jméno: ")
prijmeni=input("Zadej prijmeni: ")

for number in range(0,101):
    if(number%len(jmeno+prijmeni)==0):
        if (number%len(jmeno)==0):
            print(number) if number==0 else print("X")
        else:
            print(number*2)
    elif (number%len(jmeno)==0):
            pass
    else:
        print(number)