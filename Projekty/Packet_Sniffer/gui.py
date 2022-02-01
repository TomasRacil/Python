
from threading import Thread
from queue import Empty, Queue
from typing import Callable

from tkinter import *
from tkinter import ttk, filedialog
from rwCSV import csvRead
from datetime import datetime
import os
import netifaces

ROW_COUNTER_PACKETS =0
ROW_COUNTER_VULN=0


class GUI(Tk):
    def __init__(self, startSniffing: Callable, stopSniffing: Callable, graphicalQueue: Queue,interface):
        super().__init__()
        w, h = 1280, 720
        ws, hs = self.winfo_screenwidth(), self.winfo_screenheight()
        x, y = (ws/2) - (w/2), (hs/2) - (h/2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.title('Packet sniffer')

        self.graphicalQueue = graphicalQueue
        self.startSniffing = startSniffing
        self.stopSniffing = stopSniffing
        self.endUpdating = False

        
        self._loadedPacketsFromCSV = []

        self.interface = interface
        # print(" GUI vytvoren")
        

        self.startButton = None
        self.stopButton = None

        self._snifferRecordsWrapperFrame = None
        self._snifferVulnRecordsWrapperFrame = None
        self.interfaceCombobox = None

       
        self._create_control_menu()
        self._create_packets_window()
        self._create_vulnerabilities_window()



    def startCapturingButtonPush(self):

        if len(self._snifferRecordsWrapperFrame.winfo_children()) > 0:
                self._clear_packets_window()
                self._clear_vulnerabilities_windows()

        self.endUpdating = False
        self.updatePackets()
        self.startSniffing()
        
        self.stopButton['state'] = NORMAL
        self.startButton['state'] = DISABLED



    def stopCapturingButtonPush(self):

        self.stopSniffing()
        self.endUpdating = True

        self.stopButton['state'] = DISABLED
        self.startButton['state'] = NORMAL
        



    def updatePackets(self):
        recordWrapper = self._snifferRecordsWrapperFrame
        vulnRecordWrapper = self._snifferVulnRecordsWrapperFrame

        try:
            packet = self.graphicalQueue.get_nowait()
            self._add_record_to_packet_window(recordWrapper,packet)
            if(packet[7] != ""):
                 self._add_record_to_vuln_window(vulnRecordWrapper, packet[::len(packet)-1])
        except Empty:
            pass
        if not(self.graphicalQueue.empty() and self.endUpdating):
            self.after(250, self.updatePackets) 
 




    def _openDialog(self):
        pass
        fileName = filedialog.askopenfilename(initialdir=str(os.getcwd()),title="Select A Capture(CSV file)",filetypes = [("CSV", "*.csv")])        
        if(len(fileName) != 0):
            pass
            recordWrapper = self._snifferRecordsWrapperFrame
            if len(recordWrapper.winfo_children()) > 0:
                self._clear_packets_window()
                self._clear_vulnerabilities_windows()
            
            self._loadedPacketsFromCSV = csvRead(fileName)
            [self._add_record_to_packet_window(recordWrapper,row) for row in self._loadedPacketsFromCSV]
            vulnList = [row[7:] for row in self._loadedPacketsFromCSV if row[7:][1].strip()]

            if vulnList:
                [self._add_record_to_vuln_window(self._snifferVulnRecordsWrapperFrame,row) for row in vulnList]


    
    def _add_record_to_packet_window(self,parent, record):
        packets = record
        global ROW_COUNTER_PACKETS
        recordFrame = Frame(parent)
        recordFrame.grid(row= ROW_COUNTER_PACKETS,column=0)
        
        recLabelNum = Label(recordFrame, text= packets[0],width=10, anchor="e")
        rec2Frame = Frame(recordFrame)
        rec2 = Label(rec2Frame, text=packets[1],width=14,anchor="w")
        rec3 = Label(recordFrame, text=packets[2],width=14, anchor="w")
        rec4 = Label(recordFrame, text=packets[3],width=14, anchor="w")
        rec5 = Label(recordFrame, text=packets[4],width=12, anchor="w")
        rec6 = Label(recordFrame, text=packets[5],width=12, anchor="w")
        rec7 = Label(recordFrame, text=packets[6],width=500, anchor="w")

        recLabelNum.grid(row=0,column=0)
        rec2Frame.grid(row=0,column=1)
        rec2.grid(row=0,padx=(20,0))
        rec3.grid(row=0,column=2)
        rec4.grid(row=0,column=3)
        rec5.grid(row=0,column=4)
        rec6.grid(row=0,column=5)
        rec7.grid(row=0,column=6)
        ROW_COUNTER_PACKETS +=1

    def _add_record_to_vuln_window(self,parent,record):
        global ROW_COUNTER_VULN
        recordFrame = Frame(parent)
        recordFrame.grid(row= ROW_COUNTER_VULN,column=0)
        
        recVulnNumLabel = Label(recordFrame, text=record[0],width=10, anchor="w")
        rec7 = Label(recordFrame, text=record[1],width=500, anchor="w")

        recVulnNumLabel.grid(row=0,column=0)
        rec7.grid(row=0,column=1,padx=(20,0))
        ROW_COUNTER_VULN +=1


    def _selectedItem(self,event):
            self.interface = self.interfaceCombobox.get()

    def _create_control_menu(self):
        controlsFrame = Frame(self,padx=5, pady= 5)
        controlsFrame.pack(anchor=W)

        self.startButton = Button(controlsFrame, text="Start",command= lambda:self.startCapturingButtonPush())
        self.stopButton = Button(controlsFrame, text="Stop",command= lambda:self.stopCapturingButtonPush())
        self.stopButton["state"] = "disabled"

        laodButton = Button(controlsFrame, text="Load", command=self._openDialog)


        interfaceOptions = netifaces.interfaces()
        self.interfaceCombobox = ttk.Combobox(controlsFrame,value = interfaceOptions)
        self.interfaceCombobox.current(0)
        self.interface = self.interfaceCombobox.get()
        self.interfaceCombobox.bind("<<ComboboxSelected>>",self._selectedItem)
        self.interfaceCombobox.grid(row=0,column=3,padx=20)

        self.startButton.grid(row=0,column=0)
        self.stopButton.grid(row=0,column=1)
        laodButton.grid(row=0,column=2)

    def _create_packets_window(self):
        snifferWrapperFrame = Frame(self)
        snifferWrapperFrame.pack(anchor=W, expand=True, fill=Y)

        snifferHeaderFrame = Frame(snifferWrapperFrame,padx=5,pady=5, bg="white")
        snifferHeaderFrame.pack(anchor=W)

        snifferBodyFrame = ScrollbarFrame(snifferWrapperFrame,padx=5)
        snifferBodyFrame.canvas.configure(height=450)
        snifferBodyFrame.pack(anchor=NW,expand=True, fill=Y)

        self._snifferRecordsWrapperFrame = Frame(snifferBodyFrame.scrolled_frame)

        # for x in range(50):
        #     self._add_record_to_packet_window(self._snifferRecordsWrapperFrame)

        timestampFrame = Frame(snifferHeaderFrame, bg="white")

        packetNumberLabel = Label(snifferHeaderFrame, text="No.",bg="white", width=10, anchor="w")
        timestampLabel = Label(timestampFrame, text="Time",width=14,bg="white", anchor="w")
        sourceLabel = Label(snifferHeaderFrame, text="Source",bg="white",width=14, anchor="w")
        destinationLabel = Label(snifferHeaderFrame, text="Destination",bg="white",width=14, anchor="w")
        protocolLabel = Label(snifferHeaderFrame, text="Protocol",bg="white",width=12, anchor="w")
        packetLengthLabel = Label(snifferHeaderFrame, text="Length",bg="white",width=12, anchor="w")
        packetBodyLabel = Label(snifferHeaderFrame, text="Info",bg="white",width=77, anchor="w")

        self._snifferRecordsWrapperFrame.grid(row=0)

        packetNumberLabel.grid(row=0,column=0)
        timestampLabel.grid(row=0,padx=(20,0))
        sourceLabel.grid(row=0,column=2)
        destinationLabel.grid(row=0,column=3) 
        protocolLabel.grid(row=0,column=4)
        packetLengthLabel.grid(row=0,column=5)
        packetBodyLabel.grid(row=0,column=6)
        timestampFrame.grid(row=0,column=1)


    def _create_vulnerabilities_window(self,):

        snifferVulnWrapperFrame = Frame(self)
        snifferVulnWrapperFrame.pack(anchor=W, expand=True, fill=Y)
        

        snifferVulnerabilitesHeaderFrame = Frame(snifferVulnWrapperFrame,padx=5,pady=5, bg="white")
        snifferVulnerabilitesHeaderFrame.pack(anchor=W)

        snifferVulnerabilitesFrame = ScrollbarFrame(snifferVulnWrapperFrame,padx=5)
        snifferVulnerabilitesFrame.pack(anchor=NW,expand=True, fill=Y)

        

        packetNumberVulnLabel = Label(snifferVulnerabilitesHeaderFrame, text="No.",bg="white", width=10, anchor="w")
        packetBodyVulnLabel = Label(snifferVulnerabilitesHeaderFrame, text="Scraped Data",bg="white",width=148, anchor="w")

        packetNumberVulnLabel.grid(row=0,column=0)
        packetBodyVulnLabel.grid(row=0,column=1,padx=(20,0))


        self._snifferVulnRecordsWrapperFrame = Frame(snifferVulnerabilitesFrame.scrolled_frame)
        # self._snifferVulnRecordsWrapperFrame.pack(anchor=W)
        self._snifferVulnRecordsWrapperFrame.grid(row=0)


        # for x in range(30):
        #     self._add_record_to_vuln_window(self._snifferVulnRecordsWrapperFrame)
        # pass
    def _clear_packets_window(self):
        self._snifferRecordsWrapperFrame.configure(background="#F0F0F0")
        for widget in self._snifferRecordsWrapperFrame.winfo_children():
            widget.destroy()

    def _clear_vulnerabilities_windows(self):
         self._snifferVulnRecordsWrapperFrame.configure(background="#F0F0F0")
         for widget in self._snifferVulnRecordsWrapperFrame.winfo_children():
            widget.destroy()




class ScrollbarFrame(Frame):
    """
    Extends class tk.Frame to support a scrollable Frame 
    This class is independent from the widgets to be scrolled and 
    can be used to replace a standard tk.Frame
    """
    def __init__(self, parent, **kwargs):
        Frame.__init__(self, parent, **kwargs)

        # The Scrollbar, layout to the right
       

        # The Canvas which supports the Scrollbar Interface, layout to the left
        self.canvas = Canvas(self, borderwidth=0, background="#F0F0F0",width=1280)

        vsb = Scrollbar(self)
       
        # Bind the Scrollbar to the self.canvas Scrollbar Interface
        self.canvas.configure(yscrollcommand=vsb.set)
        vsb.configure(command=self.canvas.yview)

        hsb = Scrollbar(self, orient=HORIZONTAL)
        hsb.pack(side=BOTTOM, fill="x")
        # Bind the Scrollbar to the self.canvas Scrollbar Interface
        self.canvas.configure(xscrollcommand=hsb.set)
        hsb.configure(command=self.canvas.xview)
       
        vsb.pack(side=RIGHT, fill="y", expand=True)
        self.canvas.pack(side=LEFT, fill="y")


        # The Frame to be scrolled, layout into the canvas
        # All widgets to be scrolled have to use this Frame as parent
        self.scrolled_frame = Frame(self.canvas, background=self.canvas.cget('bg'))
        self.canvas.create_window((0, 0), window=self.scrolled_frame, anchor="nw")

        # Configures the scrollregion of the Canvas dynamically
        self.scrolled_frame.bind("<Configure>", self.on_configure)

    def on_configure(self, event):
        """Set the scroll region to encompass the scrolled frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
