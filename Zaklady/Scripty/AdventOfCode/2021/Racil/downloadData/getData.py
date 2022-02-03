import json

with open(r"C:\Vyuka\Python\Zaklady\Scripty\AdventOfCode\2021\Racil\downloadData\data.json", "r") as f:
    data = json.load(f)


with open(r"C:\Vyuka\Python\Zaklady\Scripty\AdventOfCode\2021\Racil\downloadData\names.txt", "w") as f:

    for member in data['members']:
        name=data['members'][member]['name']
        if name != None:
            f.write(name+"\n")