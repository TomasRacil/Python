import datetime

datum = datetime.datetime.now()
tag = (datum.day)#ukládá dnešní den
monat = (datum.month)#ukládá dnešní měsíc

soubor = open("schranka.txt", "r")
seznam = str(soubor.read())
CoList = seznam.split("\n")#vytvoří ze stringu seznam list 

Counter = 0#počítá počet řádků v souboru
for i in CoList:#počítá počet řádků v souboru
    if i: 
        Counter += 1

x = 0#index který určuje číslo řádku s kterým se pracuje
while x < Counter:
    if (x+1) % 2 == 0:#datum je na každém sudém řádku, řádky se počítají od nuly proto +1
        den = CoList[x].split(".")[1]#najde den
        den = int(den)
        mesic = CoList[x].split(".")[2]#najde měsíc
        mesic = int(mesic)
        if den == tag and mesic == monat:#porovnává dnešní datum s daty v souboru
        	print("Dnes ma narozeniny: ",CoList[x-1],"\n")
        x+=1
    else:
        x+=1#zvýší index pokud je na řádku se jménem
soubor.close()

novy = input("Chcete pridat noveho cloveka? (y/n)")=='y'#přidává další členy do souboru
if novy:
	dalsi = True
	soubor = open("schranka.txt", "a")
	while dalsi > False:
		soubor.write(input("Zadejte jmeno\n")+"\n."+input("Zadejte datum narozeni <dd.mm.rrrr>\n")+"\n")
		dalsi = input("Chcete pridat noveho cloveka? (y/n)")=='y'
	soubor.close()