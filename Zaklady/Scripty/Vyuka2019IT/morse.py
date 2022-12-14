from os.path import join, realpath, dirname

soubor = open(join(dirname(realpath(__file__)), "morse.txt"), "r", encoding="utf-8")

morse = {radek.split()[0]: radek.split()[1] for radek in soubor}
# for radek in soubor:
#     morse[radek.split()[0]]=radek.split()[1]
print(morse)

text = input("Zadej text k prekladu: ")

output = "|".join(
    [
        "/".join([morse.get(znak.upper(), znak) for znak in slovo])
        for slovo in text.split()
    ]
)
# temp=""
# for slovo in text.split():
#     for znak in slovo:
#         temp+=morse.get(znak.upper(), znak)+'/'
#     temp=temp[:-1] +'|'

print(output)
