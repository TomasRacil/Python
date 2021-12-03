text = open('input.txt', 'r').readlines()
lines = [x.strip() for x in text]

voc=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]#, "cid"]
goal, Sum = 0, 0

for line in lines:
    for i in line.split():
        i=i.split(":")
        if i[0] in voc: Sum+=1

    if line == "": 
        if Sum==7: goal+=1
        Sum=0

print(goal)