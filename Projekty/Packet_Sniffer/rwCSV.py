import csv
from os.path import dirname, realpath, join, isfile

# This module takes care of writing into and reading from a csv file

folder = dirname(dirname(realpath(__file__)))
file = join(folder, 'data.csv')

def csvRead(filename):
    """ Fucntion - it reads content of csv file. On openning it skips header("next" fucntion) and reads file line by line 
	    Args:
		    parameters: filename(str)
    """
    with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='|')
            next(csv_reader)
            return list(csv_reader)
    

def csvWrite(packets: list):
    """ Fucntion - it write packets list into csv file. If file does not exists then create it otherwise append the list content to the file
	    Args:
		    parameters: packets(list)
    """
    file_exists = isfile(file)
    if file_exists:
        attr = 'a'
    else:
        attr = 'w'
    with open(file, attr) as new_file:
        fieldnames = ["No.","Time","Source","Destination","Protocol","Length","Info","No.","ScrapedData" ]
        csv_writer = csv.writer(new_file, delimiter='|')
        if not file_exists:
            csv_writer.writerow(fieldnames)
        for packet in packets:
            csv_writer.writerow(packet)


   
