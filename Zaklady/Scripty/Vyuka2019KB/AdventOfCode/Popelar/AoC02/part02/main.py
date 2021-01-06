lines = open("input.txt", "r").readlines()
goal = 0

for line in lines:
    inter, lett, passw = line.split(" ")
    pos1, pos2 = inter.split("-")
    
    if (passw[int(pos1)-1] == lett[0]) != (passw[int(pos2)-1] == lett[0]): goal+=1

print(goal)