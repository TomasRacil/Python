from tkinter import *
import random

def Create():
    x=str(fname.get())
    z=str(lname.get())
    y=str(date.get())
    y=y.replace('/','')
    t=str(color.get())
    list=[x.capitalize(),y[0:4],y[-4:],z.capitalize(),t.capitalize()]
    b=c=d=e=0
    while ((b==c)or(b==d)or(b==e)or(c==d)or(c==e)or(d==e)):
        b=random.randint(0,4)  
        c=random.randint(0,4)
        d=random.randint(0,4)
        e=random.randint(0,4)
    a=list[b]+list[c]+list[d]+list[e]
    password.set(a)


root=Tk()
fname=StringVar()
lname=StringVar()
date=StringVar()
color=StringVar()
password=StringVar()
b=c=d=e=float()

root.title("Password Create")
root.minsize(height=200,width=400)
root.resizable(height=True,width=True)

Label(root,text="PASSWORD CREATE",fg="green",font=("tohama",16),justify=CENTER).grid(row=0,columnspan=2)
Label(root,text="First name:").grid(row=1,column=0)
Entry(root,width=30,textvariable=fname).grid(row=1,column=1)
Label(root,text="Last name:").grid(row=2,column=0)
Entry(root,width=30,textvariable=lname).grid(row=2,column=1)
Label(root,text="Date of Birth(dd/mm/yyyy):").grid(row=3,column=0)
Entry(root,width=30,textvariable=date).grid(row=3,column=1)
Label(root,text="Favourite Color:").grid(row=4,column=0)
Entry(root,width=30,textvariable=color).grid(row=4,column=1)

frameButton=Frame()
Button(frameButton,text="Create",command=Create).pack(side=LEFT)
Button(frameButton,text="Done",command=root.quit).pack(side=LEFT)
frameButton.grid(row=5,columnspan=2)

Label(root,text="Password:").grid(row=7,column=0)
Entry(root,width=30,textvariable=password).grid(row=7,column=1)

Label(root,text="Press 'Create' for another password!",fg="red",font=("tohama",12),justify=CENTER).grid(row=8,columnspan=2)

root.mainloop()