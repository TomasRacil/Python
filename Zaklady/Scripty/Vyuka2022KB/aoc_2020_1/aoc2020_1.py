from os.path import realpath, dirname, join

with open(join(dirname(realpath(__file__)),"input.txt"),
          "r", encoding="utf_8") as file:
    data = [int(radek) for radek in file.read().split('\n')]
    
    
    # for radek in file.read().split('\n'):
    #     data.append(int(radek))
print(data)
for index, cislo1 in enumerate(data):
    for cislo2 in data[index+1:]:
        if cislo1+cislo2 ==2020: print(cislo1, cislo2)

