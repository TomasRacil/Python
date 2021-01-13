import math
import winsound
from tkinter import messagebox

from GUI.root import root

def countdown(count,label): 
    """Timer countdown - 
    #math.floor - returns x - the largest number, but not larger than x.
    
    Args:
        count(int): the total sum of seconds entered values of time units; back conversion to units of time using modulo and divison
    
    Returns: the original values of units of time

    Subtract 1 from the total to 0, when the value is less than 0 a signal sounds and is displayed alert window. 
    """
    print(count)
    seconds=math.floor(count%60)		
    minutes=math.floor((count/60)%60)
    hours=math.floor((count/3600))
    label['text'] = "Hours: "+ str(hours)+ " Minutes:  " +str(minutes)+ " Seconds: " +str(seconds)

    if count >= 0:
        root.after(1000, countdown,count-1,label)

    else:
        for x in range(3):
            winsound.Beep(500,1000)
            messagebox.showinfo("Timer alert", "Time´s up!")

def updateButton(hoursE,minuteE,secondE,label):
    """Start timer:
    1. Load the entered values into the variables using the get method.  
        #isdigit - this method returns true if all characters are digits 
    2. Convert all values to seconds into a variable stp_time and call the countdown function.
    """

    hr,mn,sec = hoursE.get(),minuteE.get(),secondE.get()
    if hr.isdigit() and mn.isdigit() and sec.isdigit():
           stp_time=int(hr)*3600+int(mn)*60+int(sec)
           countdown(stp_time,label)