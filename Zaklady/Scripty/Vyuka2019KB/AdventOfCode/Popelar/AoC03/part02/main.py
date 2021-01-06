lines=open("input.txt","r").readlines()

indexy=[[1,1],[3,1],[5,1],[7,1],[1,2]]
goal = 1
lineLenght = len(lines[0]) - 1

for index in indexy:
    count, i, line = 0, 0, 0

    while line<len(lines):
        if lines[line][i] == "#": count+=1
        line+=index[1]
        i+=index[0]
        if i >= lineLenght: i -= lineLenght
    goal*=count

print(goal)