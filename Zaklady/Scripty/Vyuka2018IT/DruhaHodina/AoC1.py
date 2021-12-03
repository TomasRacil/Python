# soubor = open("2000.txt", "r")

# cisla=[]

# for radek in soubor:
#     cisla.append(int(radek.strip()))
# 	#print(int(radek.strip()))



#print(cisla)

# nalezeno=False

# for cislo1 in cisla:
#     for cislo2 in cisla:
#         if((cislo1+cislo2)==2020):
#             print(cislo1,cislo2,cislo1*cislo2)
#             nalezeno=True
#             break
#         if(nalezeno):break

cisla=[int(line.strip()) for line in open("2000.txt", "r")]
zbytky=[2020-cislo for cislo in cisla]

print(cisla,zbytky)

for cislo in cisla:
	if cislo in zbytky: 
		print(f"prvni: {cislo}; druhe: {2020-cislo}; součin {cislo*(2020-cislo)}")
		break

            
