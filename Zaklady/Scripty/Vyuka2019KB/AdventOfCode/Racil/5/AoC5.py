
letenky={
int("".join(["0" if char=="F" else "1" for char in letenka.strip()[:-3]]),2)*8
+int("".join(["0" if char=="L" else "1" for char in letenka.strip()[-3:]]),2) 
for letenka in open("letenky.txt", "r")}

print(max(letenky))

print(next(iter((set(range(min(letenky),max(letenky)))-letenky))))