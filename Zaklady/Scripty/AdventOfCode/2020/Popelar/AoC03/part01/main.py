lines=open("input.txt","r").readlines()

index, goal = 0, 0
lineLenght = len(lines[0]) - 1

for line in lines:
    if index >= lineLenght: index -= lineLenght
    if line[index] == "#": 
        goal+=1
    index+=3

print(goal)