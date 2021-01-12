from GUI import *
from tkinter import * 
from tkinter.ttk import *
import tkinter
from .root import * 

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

button=tkinter.Button(root,text="Start Timer",command=updateButton).place(x=120,y=480)

#Timer testing
label = tkinter.Label(root,background="dimgray")
label.place(x=100,y=510)
