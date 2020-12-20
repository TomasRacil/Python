from tkinter import * 
from tkinter.ttk import *
from time import strftime 
import tkinter
import winsound
import time
import math

second=0
minute=0
hour=0
stp=0

root = tkinter.Tk() 
root.title('Clock,alarm,stopwatch,timer') 
root.geometry("420x600")
root.resizable(False,False)
root.configure(bg="white")
  
def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 

def start():
	global second,minute,hour
	second = second + 1
	if(second==60):
		minute=minute+1
		second=0
	if(minute==60):
		hour=hour+1
		minute=0
	if(stp==0):
		label=Label(root,text='%i:%i:%i'%(hour,minute,second),font=('arial',30,'bold'),
		foreground='white',background="black",width=6)
		label.after(300,start)
		label.place(x=140,y=210)

def stop():
	global stp
	stp = 1

clock = Label(root, text="Clock",font=('arial',30,'bold')).pack(anchor = 'n')
lbl = Label(root, font = ('arial', 40, 'bold'), background = 'black', foreground = 'white') 
lbl.pack(anchor = 'n') 

stopwatch = Label(root, text="Stopwatch",font=('arial',30,'bold')).pack(anchor = 'center')
button1=Button(root,text="Start",command=start).place(x=130,y=170)
button2=Button(root,text="Stop",command=stop).place(x=210,y=170)

time() 

mainloop() 