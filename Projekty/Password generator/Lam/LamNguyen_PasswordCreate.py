from tkinter import *
import random

def Create():
    x=str(fname.get())
    z=str(lname.get())
    y=str(date.get())
    y=y.replace('/','')
    t1=str(question1.get())
    t2=str(question2.get())
    t3=str(question3.get())
    t4=str(question4.get())
    t5=str(question5.get())
    t6=str(question6.get())
    t7=str(question7.get())
    answer=[t1,t2,t3,t4,t5,t6,t7]
    w=''
    while(w==''):
        w=answer[random.randint(0,6)]

    list=[x.capitalize(),y[0:4],z.capitalize(),w[0].capitalize()]
    b=c=d=e=0
    while ((b==c)or(b==d)or(b==e)or(c==d)or(c==e)or(d==e)):
        b=random.randint(0,3)  
        c=random.randint(0,3)
        d=random.randint(0,3)
        e=random.randint(0,3)
    a=list[b]+list[c]+list[d]+list[e]
    password.set(a)
    Label(root,text="Press 'Create' for another password!",fg="red",font=("tohama",12),justify=CENTER).grid(row=20,columnspan=2)



 
def Question1():
    Entry(root,width=40,textvariable=question1).grid(row=11,column=1)

def Question2():
    Entry(root,width=40,textvariable=question2).grid(row=12,column=1)

def Question3():
    Entry(root,width=40,textvariable=question3).grid(row=13,column=1)
    
def Question4():
    Entry(root,width=40,textvariable=question4).grid(row=14,column=1)

def Question5():
    Entry(root,width=40,textvariable=question5).grid(row=15,column=1)

def Question6():
    Entry(root,width=40,textvariable=question6).grid(row=16,column=1)

def Question7():
    Entry(root,width=40,textvariable=question7).grid(row=17,column=1)

root=Tk()
question1=StringVar()
question2=StringVar()
question3=StringVar()
question4=StringVar()
question5=StringVar()
question6=StringVar()
question7=StringVar()
fname=StringVar()
lname=StringVar()
date=StringVar()
password=StringVar()
b=c=d=e=float()

root.title("Password Create")
root.minsize(height=420,width=480)
root.resizable(height=True,width=True)

Label(root,text="PASSWORD CREATE",fg="blue",font=("tohama",16),justify=CENTER).grid(row=0,columnspan=2)
Label(root,text="First name:").grid(row=1,column=0)
Entry(root,width=40,textvariable=fname).grid(row=1,column=1)
Label(root,text="Last name:").grid(row=2,column=0)
Entry(root,width=40,textvariable=lname).grid(row=2,column=1)
Label(root,text="Date of Birth(dd/mm/yyyy):").grid(row=3,column=0)
Entry(root,width=40,textvariable=date).grid(row=3,column=1)
Label(root,text="Security questions (Press the questions which you want to answer):",fg="green",font=("tohama",11),justify=CENTER).grid(row=4,columnspan=2)

Button(root,text="1.What's your favorite color?",command=Question1).grid(row=11,column=0)
Button(root,text="2.What's your first pet's name?",command=Question2).grid(row=12,column=0)
Button(root,text="3.What's your favorite game?",command=Question3).grid(row=13,column=0)
Button(root,text="4.What's your dream job?",command=Question4).grid(row=14,column=0)
Button(root,text="5.Who is your best friend now?",command=Question5).grid(row=15,column=0)
Button(root,text="6.What is your favorite car?",command=Question6).grid(row=16,column=0)
Button(root,text="7.What is your best sport?",command=Question7).grid(row=17,column=0)




frameButton=Frame()
Button(frameButton,text="Create",command=Create).pack(side=LEFT)
Button(frameButton,text="Done",command=root.quit).pack(side=LEFT)
frameButton.grid(row=18,columnspan=2)


Label(root,text="Strong password for you:").grid(row=19,column=0)
Entry(root,width=40,textvariable=password).grid(row=19,column=1)


root.mainloop()