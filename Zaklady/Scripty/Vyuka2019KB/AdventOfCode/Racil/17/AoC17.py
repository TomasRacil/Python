"""
Tento skript pracuje s výchozím 2D polem které je součástí nekončného 3D prostoru. 
V závislosti na okolních prvcích se prvky tohoto pole buď aktivují nebo deaktivují. 
Aktivní prvky (#) zůstanou aktivní pokud 2 nebo 3 okolní prvky (celkem jich je 26) jsou také aktivní jinak se deaktivují.
Deaktivované prvky (.) se aktivují pokud jsou přesně 3 okolní první aktivní.
Aktivace a deaktivace probíhá v jednotlivých kolech. Po šesti kolech je program ukončen a aktivní prvky jsou spočítány.
"""

#Správná odpověď je 313

def show(space):
	"""Show represantation of space

	Function to print out space passed in argument in form of multiple 2D arrays (with z coordinate) in command line
	
	Args:
		space (list): list of lists of characters (3D array)
	"""

	for index,height in enumerate(space):
		print(index-int((len(space)-1)/2))
		for line in height:
			print("".join(line))
		print()
	print()

def countActive(space,cz,cy,cx):
	"""Count surounding actives
	
	This function counts all active points (#) arround point specified by passed coordinates.
	
	Args:
		space (list): list of lists of characters (3D array)
		cz (int): z coordinate of central point
		cy (int): y coordinate of central point
		cx (int): x coordinate of central point

	Returns:
		integer: return number of active surounding points
	"""

	active=0
	for z in range(cz-1,cz+2):
		for y in range(cy-1,cy+2):
			for x in range(cx-1,cx+2):
				try:
					if space[z][y][x]=="#":active+=1
				except IndexError: pass
	return active

def countAll(space):
	"""Count all active
	
	This function counts all active points (#) in a 3D space.
	
	Args:
		space (list): list of lists of characters (3D array)

	Returns:
		integer: return number of active points in space
	"""

	active=0
	for z in space:
		for y in z:
			for x in y:
				if x=="#": active+=1
	return active

def expand(space):
	"""Expand space
	
	This function expand space in all dimension by one a and fill it with inactive points.
	Also it keeps original space (and value it holds) in center of expanded one.
	
	Args:
		space (list): list of lists of characters (3D array) - original

	Returns:
		list: return expanded space in all dimensions
	"""

	return [[["." for _ in range(len(space[0][0])+2)] for _ in range(len(space[0])+2)]] +[[["."]+(space[z][y-1] if (y>0 and y<=len(space[0])) else ["." for _ in range(len(space[0][0]))]) +["."] for y in range(len(space[0])+2)] for z in range(len(space))]  +[[["." for _ in range(len(space[0][0])+2)]for _ in range(len(space[0])+2)]] 

def change(space):
	"""Change state
	
	This function change states of active (#) and non active (.) points based on the rules and then return changed space.
		Active stay active if 2 or 3 surrounding point is active else deactivate
		Non actvive activate if exactly surounding 3 points are active.
	This function use countActive function for counting active surounding points.
	
	Args:
		space (list): list of lists of characters (3D array)

	Returns:
		list: return changed space
	"""

	spaceCopy=[[y.copy()for y in z] for z in space]
	for z in range(len(space)):
		for y in range(len(space[0])):
			for x in range(len(space[0][0])):
				active=countActive(space,z,y,x)
				if space[z][y][x]=="#" and active not in [3,4]:spaceCopy[z][y][x]="."
				if space[z][y][x]=="." and active==3: spaceCopy[z][y][x]="#"
	return spaceCopy

def run(space,rounds):
	"""Run simulation
	
	This function expand space  and change states of point in turns.
	After all rounds are completed return final space (expanded and modified).
	
	Args:
		space (list): list of lists of characters (3D array)
		rounds (int): number of rounds to be done

	Returns:
		list: modified space
	"""

	while rounds>0:
		space=expand(space)
		space=change(space)
		rounds-=1
		#show(space)
		#input()
	return(space)

def main():
	startSlice=[[[char for char in line.strip()] for line in open("initState.txt","r")]]
	final=run(startSlice,6)
	#show(final)
	print(countAll(final))

if __name__=="__main__":
	main()