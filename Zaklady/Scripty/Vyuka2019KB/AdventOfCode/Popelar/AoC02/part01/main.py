lines = open("input.txt", "r").readlines()
goal = 0

for line in lines:
    inter, lett, passw = line.split(" ")
    Min, Max = inter.split("-")
    sumLett = passw.count(lett[0])

    if int(Min) <= sumLett <= int(Max): goal+=1

print(goal)