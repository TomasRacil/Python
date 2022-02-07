from mimetypes import init
from queue import Queue
# from sqlite3 import InterfaceError
from time import sleep

from sniffer import Sniffer
from recorder import Recorder
from gui import GUI

sniffer =None

  
    """ Programs entry point - it initializes and declares start, pause and closing threading functions 
    """

def initSniffer():
    """ Function - Initializes sniffer object on script start and on every single sniffing session
	  
    """
    global sniffer
    sniffer = Sniffer(graphicalQueue, fileQueue,interface)

def startSniffing(recorderInstance: Recorder, snifferInstance: Sniffer):
    """ Function - Starts sniffer and recorder and initializes pauseFlags 
	    Args:
		    parameters: recorderInstance: Recorder, snifferInstance: Sniffer
    """
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
    """ Function - Pause sniffer and recorder and by setting pauseFlags to False, sleep function is called so that packets remaining in buffer can be stored into csv file 
	    Args:
		    parameters: recorderInstance: Recorder, snifferInstance: Sniffer
    """
    sniffer.pauseFlag = True
    sleep(0.2)
    recorder.pauseFlag = True

def closeProgram(recorderInstance: Recorder, snifferInstance: Sniffer):
    """ Function - Called on program exit. It stops recorder and sniffer by setting flag to True and closes threads 
	    Args:
		    parameters: recorderInstance: Recorder, snifferInstance: Sniffer
    """
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


