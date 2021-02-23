import datetime

datum = datetime.datetime.now()
date = (str(datum.day)+"."+str(datum.month)+".")

soubor = open("schranka.txt", "r")
soubor.close()

novy = input("Chcete pridat noveho cloveka? (y/n)")=='y'
if novy:
	dalsi = True
	while dalsi > False:
		soubor = open("schranka.txt", "a")
		soubor.write(input("Zadejte jmeno\n")+"\n"+input("Zadejte datum narozeni\n")+"\n")
		soubor.close()
		dalsi = input("Chcete pridat noveho cloveka? (y/n)")=='y'

soubor = open("schranka.txt", "r")
print("Následuje obsah schranky :")
print(soubor.read()+'\n')
soubor.close()