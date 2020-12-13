"""Import knihovny math s funkci π """
import math

"""Funkce round zaokrouhli cislo π na dany pocet desetinnych mist"""
def zaokrouhliPI(zaokrouhleni):
    vysledek = round((math.pi),zaokrouhleni)
    return vysledek

"""Pocet desetinnych mist"""
zaokrouhleni=input("Zadejte pocet desetinnych mist: ")

"""Zavolani funkce zaokrouhliPI"""
try:
    zaokrouhlit=int(zaokrouhleni)
    print (zaokrouhliPI(zaokrouhlit))

except:
    print ("Toto není číslo, zadejte číslo!")