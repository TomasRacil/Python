#Protože tento i nadřezený modul obsahují soubor __init__.py můžeme použít relativního importu z nadřazené složky
#dvě tečky znamená hledání v nadřazeném modulu následuje názave scriptu a import daného modulu
from ..TretiTrida import TretiTrida

def funkceVPodmodulu():
	"""První funkce v podmodulu"""
	print("První funkce")

def relativniVolani():
	"""Funkce tisknoucí dokumentaci třetí třidy"""
	print(TretiTrida.__doc__)
