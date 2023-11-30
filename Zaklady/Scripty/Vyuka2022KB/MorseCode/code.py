from os.path import realpath, dirname, join

with open(join(dirname(realpath(__file__)), "code.txt"), "r", encoding="utf_8") as file:
    code = {line[0]:line[2:] for line in file.read().split("\n")}

text:str = input("Zadej text: ")

output=' '.join([code[char.upper()] for char in text])
print(output)

# print(''.join([{line[0]:line[2:] for line in open(join(dirname(realpath(__file__)), "code.txt"), "r", encoding="utf_8").read().split("\n")}[char.upper()] for char in input("Zadej text: ")]))