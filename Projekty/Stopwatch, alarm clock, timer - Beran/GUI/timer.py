from tkinter.ttk import Label,Entry,Button

from .root import root 
from Controls import updateButton


def timerWidget():
	#Timer labels
	timer = Label(root, text="Timer",font=('arial',30,'bold'),background='dimgray',foreground='black').place(x=110,y=310)

	enter = Label(text="Enter all values:", font=('arial',14,'bold'),background="lightgreen").place(x=10,y=360)
	hoursT=Label(root, text="Hours:",font=('arial',10,'bold'),background="lightgreen").place(x=100,y=400)
	hoursE=Entry(root,width=10)
	hoursE.place(x=170,y=400)

	minuteT=Label(root, text="Minutes:",font=('arial',10,'bold'),background="lightgreen").place(x=100,y=425)
	minuteE=Entry(root,width=10)
	minuteE.place(x=170,y=425)

	secondT=Label(root, text="Seconds:",font=('arial',10,'bold'),background="lightgreen").place(x=100,y=450)
	secondE=Entry(root,width=10)
	secondE.place(x=170,y=450)

	label = Label(root,background="dimgray")
	button=Button(root,text="Start Timer",command=lambda: updateButton(hoursE,minuteE,secondE,label)).place(x=120,y=480)

	#Timer testing
	
	label.place(x=100,y=510)
