
import queue
import time
from tkinter import *
from sniffer import Sniffer
from scapy.all import *
from scapy.layers.dns import *
from threading import Thread
from csv_parser import CSVParser



exitFlag = False
gui = None
sniffer= None

def init():
    workQueue = queue.Queue()
    csvQueue = queue.Queue()
    gui = GUI('GUI ID', workQueue)

    sniffer = Sniffer('Sniffer ID',workQueue,exitFlag)
    return [gui,sniffer]

def startSniffing():
    print('Hello')
    global exitFlag, gui, sniffer
    [gui,sniffer] = init()
    exitFlag = False
    sniffer.flag = exitFlag
    gui.start()
    sniffer.start()

def stopSniffing():
    global exitFlag
    exitFlag = True
    sniffer.flag = exitFlag
    sniffer.join()

    gui.join()
    print("Exiting Main Thread")

# class Snif(Thread):

#     def __init__(self, id, q):
#         super().__init__()
#         self.id = id
#         self.q = q
#         print(f"{id}: Sniffer vytvoren")

#     def run(self):
#         print(f"{self.id} spousteni ... ")
#         self.snif()
#         print(f"{self.id}: ukoncuji se...")
#     def process_packet(self,pkt):  
#             if pkt.haslayer(TCP):
#                self.q.put(str("[")+str(time)+str("]")+"  "+"TCP-IN:{}".format(len(pkt[TCP]))+" Bytes"+"    "+"SRC-MAC:" +str(pkt.src)+"    "+ "DST-MAC:"+str(pkt.dst)+"    "+ "SRC-PORT:"+str(pkt.sport)+"    "+"DST-PORT:"+str(pkt.dport)+"    "+"SRC-IP:"+str(pkt[IP].src  )+"    "+"DST-IP:"+str(pkt[IP].dst ))

#     def snif(self,iface='eth0'):
#         data = AsyncSniffer(prn=self.process_packet, iface=iface, store=False)
#         data.start()
#         while True:
#             # print(data.results)
#             if exitFlag:
#                 data.stop()
#                 break


class GUI(Thread):
    def __init__(self, id, q):
        super().__init__()
        self.id = id
        self.q = q
        print(f"{id}: GUI vytvoren")

    def run(self):
        print(f"{self.id} spousteni ... ")
        self.launchGUI()
        print(f"{self.id}: ukoncuji se...")

    def launchGUI(self):
        while True:
            try:
                item = self.q.get(timeout=0.1)
                print(f"Item {item}")
            except queue.Empty:
                print(f"No item in que")
                pass
            if exitFlag:
                break


if __name__ == "__main__":
    

    # # sniffer.start()t(gui, sniffer):

    # # time.sleep(30)
    # workQueue = queue.Queue()
    # csvQueue = queue.Queue()
    # gui = GUI('GUI ID', workQueue)

    # sniffer = Sniffer('Sniffer ID',workQueue,exitFlag)

    root = Tk()
    startButton = Button(root, text="Start",command= lambda:startScript())
    stopButton = Button(root, text="Stop",command=lambda:stopScript())
    startButton.pack()
    stopButton.pack()
    root.mainloop()


