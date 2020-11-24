#Podobně jako u funkceVPodslozce musíme uvést celou cestu z pohledu scriptu který je výchozím  bodem programu.

from slozka.prvniPodslozka.funkceVPodslozce import funkceVPodslozce

def druhaFunkceVPodslozce():
	"""Druha funkce v podslozce"""
	print(funkceVPodslozce.__doc__)