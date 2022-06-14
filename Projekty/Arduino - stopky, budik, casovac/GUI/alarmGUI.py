from tkinter import *
from .root import root

from Functions import alarm_begin



def alarm():
    """Display alarm clock labels, button,.."""
    global hour,minute,second
    # Label
    Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
    Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()
    
    # Frame (arranging the position of widgets)
    frame = Frame(root)
    frame.pack()
    
    # Create list of Hours
    hour = StringVar(root)
    hours = [str(x) if x > 9 else '0'+str(x) for x in range(25)]
    hour.set(hours[0])
    
    hrs = OptionMenu(frame, hour, *hours)
    hrs.pack(side=LEFT)
    
    # Create list of Minutes
    minute = StringVar(root)
    minutes = [str(x) if x > 9 else '0'+str(x) for x in range(61)]
    minute.set(minutes[0])
    
    mins = OptionMenu(frame, minute, *minutes)
    mins.pack(side=LEFT)

    # Create list of Seconds
    second = StringVar(root)
    seconds = [str(x) if x > 9 else '0'+str(x) for x in range(61)]
    second.set(seconds[0])
    
    secs = OptionMenu(frame, second, *seconds)
    secs.pack(side=LEFT)

    # Button
    begin = Button(root,text="Start Alarm",font=("Helvetica 15"))
    begin.place(x=90,y=330)
    def handler(event,hour=hour,minute=minute,second=second):
            return alarm_begin(event,hour,minute,second)
    begin.bind("<Button-1>",handler)
    #Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)