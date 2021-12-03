import functools

soubor=[int(line.strip()) for line in open("adapters.txt", "r")]
soubor.append(max(soubor)+3)
soubor.append(0)
soubor=sorted(soubor)

def difference(i):
	if i==len(soubor)-2:
		return {soubor[i+1]-soubor[i]:1}
	else:
		x=difference(i+1)
		x[soubor[i+1]-soubor[i]]=x[soubor[i+1]-soubor[i]]+1 if soubor[i+1]-soubor[i] in x else 1
		return x

"""@functools.lru_cache(maxsize=100000)
def posible(adapter):
	i=soubor.index(adapter)
	helper={}
	for moznost in [adapter for adapter in soubor[i:] if adapter-soubor[i]<4 and adapter!=soubor[i]]:
		if not moznost==158:
			helper[moznost]=posible(moznost)
		else: return 158
	return {soubor[i]:helper}
print(posible(50))"""

@functools.lru_cache(maxsize=100)
def posible(i):
	helper=0
	for moznost in [adapter for adapter in soubor[i:] if adapter-soubor[i]<4 and adapter!=soubor[i]]:
		if not moznost==158: helper+=posible(soubor.index(moznost))
		else: return 1
	return helper


print(difference(0))
print(posible(0))
