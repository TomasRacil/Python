#from GUI import *
#
#from tkinter import Label,Button
from tkinter.ttk import Label,Button

from .root import root
from Controls import start,stop

def stopwatchWidgets():
    """Display stopwatch labels and buttons"""
    stopwatch = Label(root, text="Stopwatch",font=('arial',30,'bold'),background="dimgray",foreground='black').pack(anchor = 'center')
    stopwatchLabel = Label(root, text='0:0:0',font=('arial',30,'bold'),foreground='green',background="black",width=6).place(x=110,y=260)
    button1=Button(root,text="Start",command=start).place(x=100,y=230)
    button2=Button(root,text="Stop",command=stop).place(x=180,y=230)