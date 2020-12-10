def PoziceNaNastupu():
	nastup = True
	while nastup:
		print("Vítej na nástupu")
    	if input ("Chcete se účastnit nástupu? (A - ano) (N - ne) \n" ) =='n'or'N':break
    	else:
        	print("Vaše pozice na ranním nástupu \n")
        	print("Podle vašeho jména vám vybereme, zda na nástupu budete ZVR, velící nebo pouhý student ve tvaru")
        	vyber=input("Zadejte své jméno a příjmení: ")
        		try:
        			if  len(vyber)>0 and len(vyber)<12
        				print ("Student ve tvaru")
        			elif len(vyber)>=12 and len(vyber)<18
        				print("Velící")
        			else len(vyber)>=18 and len(vyber)<30
        		    	print ("ZVR")
        		except: 
        				print("Neplatné jmého a příjmení.\n Používejte pouze malá a velká písmena abecedy.\n")

"""Tato funkce spočítá znaky ve jméně a příjmení uživatele a podle toho vybere člověka na nástupu (Petru nebo Romana)"""
def ZVR():
	zvr = True
	while zvr
	





        		 


  
