from threading import Thread
from queue import Queue
from time import sleep


class Sniffer(Thread):

    def __init__(self, graphicalQueue: Queue, fileQueue: Queue):
        super().__init__()
        self.gq = graphicalQueue
        self.fq = fileQueue
        self.pauseFlag = False
        self.stopFlag = False

    def run(self):
        print("Spousteni Snifferu... ")
        self.sniff()
        print("Ukonceni Snifferu...")

    def sniff(self):
        i = 0
        while not self.stopFlag:
            if self.pauseFlag:
                sleep(0.5)
            else:
                self.fq.put(i)
                self.gq.put(i)
                sleep(0.2)
                i += 1
