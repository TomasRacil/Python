def vytiskniText(text="nic nebylo predano"):
	"""Tato funkce tiskne text
	"""
	print(text)
	return 1

print(vytiskniText.__doc__)

x=vytiskniText(text="ukazka")
print(x)

def vytiskniMnozinu(*args):
	print(args)

vytiskniMnozinu("tomas",2020,{"prijmeni":"racil"})

def vytiskniMnozinu(**kwargs):
	print(kwargs)

vytiskniMnozinu(jmeno="tomas",rok=2020,slovnik={"prijmeni":"racil"})

def vytiskniMnozinu(*args,**kwargs):
	print(args,kwargs)

vytiskniMnozinu({"prijmeni":"racil"},jmeno="tomas",rok=2020)