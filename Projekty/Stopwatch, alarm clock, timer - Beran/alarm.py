from tkinter import *
import datetime
import time
import winsound
from time import strftime 

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        #Pokud je soucasny cas roven zvolenemu casu zazni zvukovy signal
        if now == set_alarm_timer:
            print("Time to Wake up")
        winsound.Beep(500,1000)
        break

def actual_time():
    set_alarm_timer = f"{hr.get()}:{mn.get()}:{sec.get()}"
    alarm(set_alarm_timer)

def time(): 
    string = strftime('%H:%M:%S %p \n %d.%m.%Y')
    lbl.config(text = string) 
    lbl.after(1000, time) 

window = Tk()
window.title("Alarm Clock")
window.geometry("280x300")
window.resizable(False,False)
window.configure(bg="silver")

# The Variables we require to set the alarm(initialization):
hr = StringVar()
mn = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
enter_alert=Label(window, text= "Enter time in 24 hour format (00:00:00):", font=("Arial",10,"bold"),bg="pink").place(x=20,y=60)
alarm=Label(window,text="Alarm Clock",font=('arial',30,'bold'),bg="silver",foreground=('red')).place(x=20,y=10)
hourT=Label(window,text="Hours:",font=('arial',10,'bold'),bg="silver").place(x=40,y=90)
hourE= Entry(window,textvariable = hr,width = 5).place(x=110,y=90)
minT=Label(window,text="Minutes:",font=('arial',10,'bold'),bg="silver").place(x=40,y=110)
minE= Entry(window,textvariable = mn,width = 5).place(x=110,y=110)
secT=Label(window,text="Seconds:",font=('arial',10,'bold'),bg="silver").place(x=40,y=130)
secE = Entry(window,textvariable = sec,width = 5).place(x=110,y=130)

#Potvrzeni zadani casu
button = Button(window,text = "Set Alarm",width = 33,command = actual_time).place(x =20,y=160)

lbl = Label(window, font = ('arial', 20, 'bold'), background = 'black', foreground = 'red') 
lbl.place(x=45,y=210) 

time() 



window.mainloop()

