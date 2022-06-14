from threading import Thread
from queue import Queue
from time import sleep
from rwCSV import csvWrite

# This module is started in parallel with the sniffer module. It takes a queue filled with captured packed by the sniffer module and writes queue content into a csv file(rwCSV module).

class Recorder(Thread):
    """ Constructor - initialization of recorder which is responsible for offloading packets from queue
	    Args:
		    parameters: self, queue(Queue) - stores packet records, packetGroupLen(int) - default size of packet list(buffer)
    """
    def __init__(self, queue: Queue, packetGroupLen: int = 20):
        super().__init__()
        self.q = queue
        self.packets = []
        self.packetGroupLen = packetGroupLen
        self.stopFlag = False
        self.pauseFlag = False

    def run(self):
        """ Starts this object in new thread
	        Args:
		        parameter: instance of Recorder
        """        
        
        print("Spousteni rekorderu... ")
        self.checkQueue()
        print("Ukonceni rekorderu...")

    def checkQueue(self):
        """ Function - continually checks the status of queue, if the queue is full it writes content of "packets[]" variable into csv file using csvWrite function
	        Args:
		        parameters: recorderInstance: Recorder, snifferInstance: Sniffer
         """
        while not ((emptyQueue := self.q.empty()) & (packetsLen := len(self.packets)) == 0 and self.stopFlag):
            if self.pauseFlag and emptyQueue and packetsLen == 0:
                sleep(0.01)
            else:
                if not emptyQueue:
                    self.packets.append(self.q.get(timeout=0.01))
                if packetsLen == self.packetGroupLen or self.stopFlag or self.pauseFlag:
                    csvWrite(self.packets)
                    self.packets = []

     
