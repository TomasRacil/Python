#Protože se jedná o script, který není součástí modulu musíme používat relativní import
#musíme tedy vždy vědět, kde se nachází výchozí bod programu a na základě toho zvolit cestu k importovanému modulu
#vzhledem k tomu, že je volaný z scriptu main musíme vstoupit do slozky a následně vybrat script z kterého importujeme samotný prvek
from slozka.CtvrtaTrida import CtvrtaTrida

def funkceVPodslozce():
	"""První funkce v podslozce"""
	print("První funkce")

def absolutniVolani():
	"""Funkce tisknoucí dokumentaci čtvrté třidy"""
	print(CtvrtaTrida.__doc__)
