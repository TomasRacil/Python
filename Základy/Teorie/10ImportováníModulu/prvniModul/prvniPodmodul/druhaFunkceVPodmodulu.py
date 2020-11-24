#v rámci modulů můžeme importovat i v rámci stejné složky za použití jedné tečky
#pokud bychom použil  from . import * budeme importovat všechny prvky modulu definované v __init__.py
#toto se výrazně nedoporučuje protože to může vytvořit kruhové závislosti

from .funkceVPodmodulu import funkceVPodmodulu

def druhaFunkceVPodmodulu():
	"""Druha funkce v podmodulu"""
	print(funkceVPodmodulu.__doc__)