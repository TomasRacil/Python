from queue import Empty, Queue
from tkinter import END, Text, Tk, Button
from typing import Callable


class GUI(Tk):

    def __init__(self, startSniffing: Callable, stopSniffing: Callable, graphicalQueue: Queue):
        super().__init__()

        w, h = 1280, 720
        ws, hs = self.winfo_screenwidth(), self.winfo_screenheight()
        x, y = (ws/2) - (w/2), (hs/2) - (h/2)
        self.title('Packet sniffer')
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.graphicalQueue = graphicalQueue
        self.startSniffing = startSniffing
        self.stopSniffing = stopSniffing
        self.endUpdating = False

        self.text = Text(self)
        self.text.pack()

        self.startButton = Button(
            self, text='Start', command=self.startButtonPushed)
        self.startButton.pack()
        self.stopButton = Button(
            self, text='Stop', command=self.stopButtonPushed)
        self.stopButton.pack()

    def startButtonPushed(self):
        self.endUpdating = False
        self.updatePackets()
        self.startSniffing()

    def stopButtonPushed(self):
        self.stopSniffing()
        self.endUpdating = True

    def updatePackets(self):
        try:
            item = self.graphicalQueue.get_nowait()
            self.text.insert(END, str(item)+'\n')
        except Empty:
            pass
        if not(self.graphicalQueue.empty() and self.endUpdating):
            self.after(100, self.updatePackets)
