import time
from random import randint
def klickovat():
	print(f"Opište zobrazené číslo, které určí váš krok - časový limit - 1 sekunda\n")
	pomocna = 0
	time.sleep(2)

	for pocet in range(0, 10, 1):
		cislo = randint(0, 20)
		print(f"Krok: {cislo}\n")
		startTime = time.time()
		prvni = int(input("Opsane: "))

		if (time.time()-startTime) < 2:
			if cislo != prvni:
				print("SPADL JSI!!!")
				pomocna = pomocna+1

			if pomocna > 2:
				print("Dosly ti pokusy - prohra? - znovu?")
				break
		else:
			print("Vyprsel Ti  HA HA cas ")
			break

klickovat()

def procedure():
	time.sleep(2.5)