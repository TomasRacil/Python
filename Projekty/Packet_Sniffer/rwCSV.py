import csv
from os.path import dirname, realpath, join, isfile


folder = dirname(dirname(realpath(__file__)))
file = join(folder, 'data.csv')

def csvRead(filename):

    with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='|')
            next(csv_reader)
            return list(csv_reader)
    

def csvWrite(packets: list):
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


   