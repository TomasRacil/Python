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
  
 """Clock"""
def time(): 
    string = strftime('%H:%M:%S %p \n %d.%m.%Y')
    lbl.config(text = string) 
    lbl.after(1000, time) 
"""Start Stopwatch"""
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
		label.after(1000,start)
		label.place(x=140,y=260)
"""Stop stopwatch"""
def stop():
	global stp
	stp = 1

"""Timer countdown"""
#math.floor - vraci x - nejvetsi cislo, ale ne vetsi nez x 
def countdown(count): 
    seconds=math.floor(count%60)
    minutes=math.floor((count/60)%60)
    hours=math.floor((count/3600))
    label['text'] ="Hours: "+ str(hours)+ " Minutes:  " +str(minutes)+ " Seconds: " +str(seconds)

    if count >= 0:
        root.after(1000, countdown,count-1)
    else:
        for x in range(3):
            winsound.Beep(1000,1000)
            label['text']="Time is up!"

"""Start Timer"""
#isdigit - metoda vraci true, pokud jsou všechny znaky číslice
#get - vraci hodnoty polozky
def updateButton():
    hr,mn,sec = hoursE.get(),minuteE.get(),secondE.get()
    if hr.isdigit() and mn.isdigit() and sec.isdigit():
           time=int(hr)*3600+int(mn)*60+int(sec)
           countdown(time)

clock = Label(root, text="Clock",font=('arial',30,'bold'),foreground='red').pack(anchor = 'n')
lbl = Label(root, font = ('arial', 40, 'bold'), background = 'black', foreground = 'white') 
lbl.pack(anchor = 'n') 

stopwatch = Label(root, text="Stopwatch",font=('arial',30,'bold'),foreground='red').pack(anchor = 'center')
button1=Button(root,text="Start",command=start).place(x=130,y=230)
button2=Button(root,text="Stop",command=stop).place(x=210,y=230)

time() 

hoursT=tkinter.Label(root, text="Hours:",font=('arial',12,'bold')).place(x=20,y=320)
hoursE=tkinter.Entry(root).place(x=100,y=320)
minuteT=tkinter.Label(root, text="Minutes:",font=('arial',12,'bold')).place(x=20,y=340)
minuteE=tkinter.Entry(root).place(x=100,y=340)
secondT=tkinter.Label(root, text="Seconds:",font=('arial',12,'bold')).place(x=20,y=360)
secondE=tkinter.Entry(root).place(x=100,y=360)

button=tkinter.Button(root,text="Start Timer",command=updateButton).place(x=20,y=400)


mainloop() 