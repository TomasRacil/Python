import os

def fAmount(folder = "spz"):
    dirListing = os.listdir(folder)
    #Ulozi seznam souboru do listu
    
    return len(dirListing)
	#Vrati pocet polozek v listu (ve slozce)