from tkinter.ttk import Label

from .shared import second,minute,hour,stp
from GUI.root import root

def start():
    """Starting stopwatch
    1. Setting of time units.
    2. If the variable stp==0, the stopwatch starts. 
    """
    global second,minute,hour
    second = second + 1
    if(second==60):
        minute=minute+1
        second=0
    if(minute==60):
        hour=hour+1
        minute=0
    if(stp==0):
        label=Label(root,text='%i:%i:%i'%(hour,minute,second),font=('arial',30,'bold'), foreground='green',background="black",width=6)
        label.after(1000,start)
        label.place(x=110,y=260)

def stop():
    """Stopping stopwatch
    Changes the value of the value of the variable stp to 1. This will stop the stopwatch.
    """
    global stp
    stp = 1