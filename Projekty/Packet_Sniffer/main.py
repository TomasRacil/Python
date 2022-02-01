from mimetypes import init
from queue import Queue
# from sqlite3 import InterfaceError
from time import sleep

from sniffer import Sniffer
from recorder import Recorder
from gui import GUI

sniffer =None

# Program entry point - it initializes and declares start, pause and closing threading functions 

def initSniffer():
    global sniffer
    sniffer = Sniffer(graphicalQueue, fileQueue,interface)

def startSniffing(recorderInstance: Recorder, snifferInstance: Sniffer):
    if recorder.is_alive():
        recorder.pauseFlag = False
        sniffer.pauseFlag = False

        if not sniffer.is_alive():
            initSniffer()
            sniffer.start()


    else:
        print("Starting threads")
        recorder.start()
        sniffer.start()

def pauseSniffing(recorderInstance: Recorder, snifferInstance: Sniffer):

    sniffer.pauseFlag = True
    sleep(0.2)
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
    initSniffer()
    recorder = Recorder(fileQueue, 20)
    app = GUI(
        lambda: startSniffing(recorder, sniffer),
        lambda: pauseSniffing(recorder, sniffer),
        graphicalQueue,
        interface
    )
    app.mainloop()

    closeProgram(recorder, sniffer)


