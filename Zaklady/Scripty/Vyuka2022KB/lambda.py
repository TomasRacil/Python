l:list = [(1,2),(5,1),(3,4),(1,3)]

print(sorted(l,key=lambda x:x[1]+x[0]))
print(list(map(lambda x:(x[0]*2,x[1]), l)))