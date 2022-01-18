import csv
import os.path
import queue
from threading import Thread

class CSVParser():

    # super().__init__(self)
   
    # def run(self):
    #     print(f" CSV spousteni ... ")


    @classmethod
    def read(self,filename):
        #self.run()
        with open(filename, 'r') as csv_file:
             csv_reader = csv.reader(csv_file, delimiter='|')
             next(csv_reader)
             return list(csv_reader)
        
   
    @classmethod
    def write(self,filename,records):
        #self.run()
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
            while not records.empty():
                csv_writer.writerow(records.get())

# if __name__  == "__main__":
#     data = queue.Queue(3)
#     data.put(["1|0.023|192.168.1.129|192.168.1.1|TELNET|10000000|Standard query response 0x0002 A www.reddit.com CNAME reddit.map.fastly.net A 199.232.17.140|1|Login:den9k12 Password:Bromabora1"])
#     data.put(["1|0.023|192.168.1.129|192.168.1.1|TELNET|10000000|Standard query response 0x0002 A www.reddit.com CNAME reddit.map.fastly.net A 199.232.17.140|1|Login:den9k12 Password:Bromabora1"])
#     data.put(["1|0.023|192.168.1.129|192.168.1.1|TELNET|10000000|Standard query response 0x0002 A www.reddit.com CNAME reddit.map.fastly.net A 199.232.17.140|1|Login:den9k12 Password:Bromabora1"])

#     CSVParser.write('Test.1.csv',data)
   