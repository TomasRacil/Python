from tkinter import * 
from tkinter.ttk import *
from time import strftime 
import tkinter
import winsound
import time
import datetime
import math
  
"""Clock - vypise aktualni cas, AM/PM, den,mesic a rok"""
def time(): 
    string = strftime('%H:%M:%S %p \n %d.%m.%Y')
    lbl.config(text = string) 
    lbl.after(1000, time) 

"""Start stopwatch"""
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
        foreground='green',background="black",width=6)
        label.after(1000,start)
        label.place(x=110,y=260)

"""Stop stopwatch"""
def stop():
    global stp
    stp = 1

"""Timer countdown - odecita 1 od celkoveho souctu do 0"""
def countdown(count): 
	#math.floor - vraci x - nejvetsi cislo, ale ne vetsi nez x 
    seconds=math.floor(count%60)		
    minutes=math.floor((count/60)%60)
    hours=math.floor((count/3600))
    label['text'] = "Hours: "+ str(hours)+ " Minutes:  " +str(minutes)+ " Seconds: " +str(seconds)

    if count >= 0:
        root.after(1000, countdown,count-1)

    else:
    	#Alert okno o vyprseni casu
        alert = tkinter.Tk()
        alert.title('Timer alert')
        alert.geometry("240x160")
        alert.resizable(False,False)
        alert.configure(bg="silver")
        labeltimer = Label(alert, text = "Time is up!",font=('arial',15,'bold'),background='silver',foreground='green')
        labeltimer.place(x=65,y=60) 	

        #Zvukovy signal	
        for x in range(3):
         winsound.Beep(500,1000)

        alert.mainloop()

"""Start timer"""
#isdigit - metoda vraci true, pokud jsou všechny znaky číslice
#get - vraci hodnoty polozky
def updateButton():
    hr,mn,sec = hoursE.get(),minuteE.get(),secondE.get()
    if hr.isdigit() and mn.isdigit() and sec.isdigit():
           stp_time=int(hr)*3600+int(mn)*60+int(sec)
           countdown(stp_time)

def stopwatchWidgets():
    stopwatch = Label(root, text="Stopwatch",font=('arial',30,'bold'),background="dimgray",foreground='black').pack(anchor = 'center')
    stopwatchLabel = Label(root, text='0:0:0',font=('arial',30,'bold'),foreground='green',background="black",width=6).place(x=110,y=260)
    button1=Button(root,text="Start",command=start).place(x=100,y=230)
    button2=Button(root,text="Stop",command=stop).place(x=180,y=230)

#Stopwatch - definování proměnných
second=0
minute=0
hour=0
stp=0
entry1=0
entry2=0

#Hlavni dialogove okno
root = tkinter.Tk() 
root.title('Clock,alarm,stopwatch,timer') 
root.geometry("360x560")
root.resizable(False,False)
root.configure(bg="dimgray")

#Clock labels
clock = Label(root, text="Clock",font=('arial',30,'bold'),background='dimgray',foreground='black').pack(anchor = 'n')
lbl = Label(root, font = ('arial', 40, 'bold'), background = 'black', foreground = 'green') 
lbl.pack(anchor = 'n') 

#Zavolame funkci time a funkci s widgety pro stopky
time() 
stopwatchWidgets()

#Timer labels
timer = Label(root, text="Timer",font=('arial',30,'bold'),background='dimgray',foreground='black').place(x=110,y=310)

enter = Label(text="Enter all values:", font=('arial',14,'bold'),background="lightgreen").place(x=10,y=360)
hoursT=tkinter.Label(root, text="Hours:",font=('arial',10,'bold'),background="lightgreen").place(x=100,y=400)
hoursE=tkinter.Entry(root,width=10)
hoursE.place(x=170,y=400)

minuteT=tkinter.Label(root, text="Minutes:",font=('arial',10,'bold'),background="lightgreen").place(x=100,y=425)
minuteE=tkinter.Entry(root,width=10)
minuteE.place(x=170,y=425)

secondT=tkinter.Label(root, text="Seconds:",font=('arial',10,'bold'),background="lightgreen").place(x=100,y=450)
secondE=tkinter.Entry(root,width=10)
secondE.place(x=170,y=450)

button=tkinter.Button(root,text="Start Timer",command=updateButton).place(x=20,y=490)

#label pro otestování zda zbytek funguje
label = tkinter.Label(root,background="dimgray")
label.place(x=100,y=490)

root.mainloop()