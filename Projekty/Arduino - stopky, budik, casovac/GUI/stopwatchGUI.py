
from tkinter import *

from .root import root

from Functions.stopwatchClock import Start, Stop, Reset

def stopwatch():
    """Display stopwatch"""
    
    # Label (to display time)
    global label
    Label(root,text="Stopwatch",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
    label = Label(text='00:00:00', font=('Arial', 25))
    label.pack()

    # start, pause, reset, quit buttons
    start = Button(root, text='Start',width=25, command=lambda:Start(label))
    pause = Button(root, text='Stop', width=25, command=Stop)
    reset = Button(root, text='Reset',width=25, command=lambda:Reset(label))
    quit = Button(root, text='Quit',width=25,command=root.quit)
    start.pack()
    pause.pack()
    reset.pack()
    quit.pack()
    #state='disabled'

