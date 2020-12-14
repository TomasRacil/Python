def palindrom(str):
	return str == str[::-1]

soubor = open("text.txt", "r")
text = str(soubor.read())
text = text.lower()

remove = ["(", ")", ",", "\n","    ","   ", "  "]
replace = [":", "?", "!", ". "]
palindromy = []
i = 0

for znak in remove: 
	text = text.replace(znak, " ")

for znak in replace: 
	text = text.replace(znak, ".")

vety = text.split(".")

for veta in vety:
	if len(veta) > 1:
		if palindrom(veta): 
			palindromy.append(veta)

text = text.replace(".", "")
slova = text.split(" ")

for slovo in slova:
	if len(slovo) > 1:
		if palindrom(slovo):
			palindromy.append(slovo)

print(f"V textu se nachazi {len(palindromy)} palindromu:")

for palindr in palindromy:
	print(palindr)