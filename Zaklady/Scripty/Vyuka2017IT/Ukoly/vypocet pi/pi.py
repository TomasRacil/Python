pi = 0
#program pro výpočet pi na libovolný počet míst 
# cyklus for pro výpočet pi vycházím ze vzorce 4/1 - 4/3 + 4/5 -4/7 + 4/9....
# čím větší číslo pro "i" v cyklu tím přesnější = čas výpočtu se zvětšuje
for i in range(1, 10000000, 4):
	pi+=4/i
	pi-=4/(i+2)
pocetz = input("Zadej pocet míst na kolik chcete zaokrouhlit")
pocetz = int(pocetz)
piround= round(pi, pocetz)
print (piround)