from tkinter import *

import datetime
import time

from Arduino.components import buzzerPlay
#from Arduino.led import ledShineOn,ledShineOff




def alarm_begin(event,hr,mt,sd):
    """Alarm clock:
    1. Load the entered values into the variables (h,m,s) using the get method.  
    2. If the time we enter is either the current time, Arduino will play sound and then quit.
    """

    hour = hr.get()
    minute = mt.get()
    second = sd.get()

    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm_time = f"{hour}:{minute}:{second}"
 
        # Wait for one seconds (overload CPU)
        time.sleep(1)
 
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        # Check set alarmm, if is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            #ledShineOn()
            buzzerPlay()   
            #ledShineOff
            exit()