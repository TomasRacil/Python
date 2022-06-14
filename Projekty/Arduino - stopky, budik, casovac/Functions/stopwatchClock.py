from tkinter import *
import datetime


UTC = datetime.timezone.utc
startdate = datetime.datetime.fromtimestamp(0, tz=UTC)
counter = datetime.datetime.timestamp(startdate)



#counter = 0
running = False


def counter_label(label):
    def count():
        if running:
            global counter
   
            # To manage the initial delay.
            if counter==0:            
                display="Starting..."
            else:
                tt = datetime.datetime.fromtimestamp(counter, tz=UTC)
                string = tt.strftime("%H:%M:%S")
                display=string
   
            label['text']=display
   
            # label.after(arg1, arg2) delays by first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000, count) 
            counter += 1
   
    # Triggering the start of the counter.
    count()     
   
# Start function of the stopwatch
def Start(label):
    global running
    running=True
    counter_label(label)

   
# Stop function of the stopwatch
def Stop():
    global running
    running = False
   
# Reset function of the stopwatch
def Reset(label):
    global counter
    counter=66600
   
    # If rest is pressed after pressing stop.
    if running==False:      
        label['text']='00:00:00'
   
    # If reset is pressed while the stopwatch is running.
    else:               
        label['text']='Starting...'