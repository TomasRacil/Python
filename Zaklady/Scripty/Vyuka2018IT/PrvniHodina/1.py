
jmeno=input("Zadej křestní jméno: ")
prijmeni=input("Zadej prijmeni: ")

for number in range(1,101):
    if(number%len(jmeno+prijmeni)==0):
        if (number%len(jmeno)==0):
            print("X")
        print(number*2)
    elif (number%len(jmeno)==0):
            pass
    else:
        print(number)