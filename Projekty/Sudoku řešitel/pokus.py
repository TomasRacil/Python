"""m = 9
n = 9
matrix = [9]; columns = [9]
# initialize the number of rows
for i in range(0,m):
  matrix += [0]
# initialize the number of columns
for j in range (0,n):
  columns += [0]
# initialize the matrix
for i in range (0,m):
  matrix[i] = columns
for i in range (0,9):
  for j in range (0,9):
    print ('entry in row: ',i+1,' column: ',j+1)
    matrix[i][j] = int(input())
print (matrix)"""
class NeniVRozsahu(Exception):
    pass

while True:
	try:
		x=int(input("Zadej: "))
		if x not in range(0,10): raise NeniVRozsahu
		break
	except NeniVRozsahu:
		print("Neni v rozsahu")
	except ValueError:
		print("Neni cislo")
	except Exception as e:
		print(f"Neocekavana vyjimka: {type(e)}")

 

