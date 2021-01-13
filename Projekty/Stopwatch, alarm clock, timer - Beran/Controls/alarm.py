from tkinter import messagebox
import winsound
import datetime

#from GUI.alarm import e1,e2

def alarm_begin(event,e1,e2):
    """Alarm clock:
    1. Load the entered values into the variables (h,m) using the get method.  
    2. If the time we enter is either the current time, a beep will sound and a warning will be displayed.
    """

    h=e1.get()
    m=e2.get()

    while True:
        if int(h)==datetime.datetime.now().hour and int(m)==datetime.datetime.now().minute:
            winsound.Beep(2000,1000)
            winsound.Beep(400,1000)
            winsound.Beep(600,800)
            messagebox.showinfo("Alarm alert", "Time´s up!")
            break