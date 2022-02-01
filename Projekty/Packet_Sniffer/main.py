from queue import Queue
from sqlite3 import InterfaceError
from time import sleep

from sniffer import Sniffer
from recorder import Recorder
from gui import GUI


def startSniffing(recorderInstance: Recorder, snifferInstance: Sniffer):
    if recorder.is_alive():
        recorder.pauseFlag = False
        sniffer.pauseFlag = False

    else:
        print("Starting threads")
        recorder.start()
        sniffer.start()

def pauseSniffing(recorderInstance: Recorder, snifferInstance: Sniffer):

    sniffer.pauseFlag = True
    sleep(0.1)
    recorder.pauseFlag = True


def closeProgram(recorderInstance: Recorder, snifferInstance: Sniffer):
    
    pauseSniffing(recorder, sniffer)
    sniffer.stopFlag = True
    recorder.stopFlag = True
    sniffer.join()
    recorder.join()




if __name__ == '__main__':
    graphicalQueue = Queue()
    fileQueue = Queue()
    interface = ""
    sniffer = Sniffer(graphicalQueue, fileQueue,interface)
    recorder = Recorder(fileQueue, 50)
    app = GUI(
        lambda: startSniffing(recorder, sniffer),
        lambda: pauseSniffing(recorder, sniffer),
        graphicalQueue,
        interface
    )
    app.mainloop()

    closeProgram(recorder, sniffer)


