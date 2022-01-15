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

if __name__ == "__main__":
    data = [["1","0.023","192.168.1.129","192.168.1.1","TELNET","10000000","Standard query response 0x0002 A www.reddit.com CNAME reddit.map.fastly.net A 199.232.17.140","1","Login:den9k12 Password:Bromabora1"],["1","0.023","192.168.1.129","192.168.1.1","TELNET","10000000","Standard query response 0x0002 A www.reddit.com CNAME reddit.map.fastly.net A 199.232.17.140","1","Login:den9k12 Password:Bromabora1"]]
    # CsvParser.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+".csv",data[0])
    #CSVParser.read('capture_11.1.csv')