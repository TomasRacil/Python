#1 cviceni


#2 cviceni

jmeno:str = "Tomas"
prijmeni = "Racil"
vek:int = 28

veta = f"Jmenuji se {jmeno} {prijmeni} a je mi {vek} let."

print(veta)


#3 cviceni

print(len(veta))

print(veta.lower())

print(veta.replace(" a ", " nebo "))

slova:list = veta.split();

print(slova)

print(slova[2])

vstup = "".join(input("Zadej retezec k testovani: ").split())

vstup_o = vstup[::-1]

# vstup_o = "".join([vstup[i] for i in range(len(vstup_o)-1, -1, -1)])
    
print(vstup_o)
if vstup.lower() == vstup_o.lower():
    print("Je palindrom")
else:
    print("Neni palindrom")