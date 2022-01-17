import csv
from datetime import datetime
import os.path

class CSVParser:
    @classmethod
    def read(self,filename):
        with open(filename, 'r') as csv_file:
             csv_reader = csv.reader(csv_file, delimiter='|')
             next(csv_reader)
             return list(csv_reader)
        
   
    @classmethod
    def write(self,filename,record):
        file_exists = os.path.isfile(filename)
        if file_exists:
            attr = 'a'
        else:
            attr = 'w'
        with open(filename, attr) as new_file:
            fieldnames = ["No.","Time","Source","Destination","Protocol","Length","Info","No.","ScrapedData" ]
            csv_writer = csv.writer(new_file, delimiter='|')
            if not file_exists:
                csv_writer.writerow(fieldnames)
            csv_writer.writerow(record)
#