def sorter(numbers, file_name):
	"""Writes sorted list into text file"""
	numbers.sort(reverse=True)
	l_file = open(file_name, "w")
	for number in numbers:
		l_file.write(str(number) + "\n")
	l_file.close()

def findSame(file_1, file_2):
	"""Returns count of numbers contained in both text files and writes them into new file"""
	l_file = open("identical_numbert.txt", "w")
	count = 0
	first = file_1.readline()
	second = file_2.readline()
	try:
		while(True):
			if (int(first) < int(second)):
				second = file_2.readline()
			elif (int(first) > int(second)):
				first = file_1.readline()
			else:
				l_file.write(str(first))
				count += 1
				first = file_1.readline()
				second = file_2.readline()
	except:
		file_1.close()
		file_2.close()
		l_file.close()
		return count
