from tkinter import *

root=Tk()
root.title("Password Create")
root.minsize(height=420,width=480)
root.resizable(height=True,width=True)
'''
I initialize a window using the Tkinter interface.
I named the variable 'root'
'''

Label(root,text="PASSWORD CREATE",fg="blue",font=("tohama",16),justify=CENTER).grid(row=0,columnspan=2)

Label(root,text="First name:").grid(row=1,column=0)
fname=StringVar()
Entry(root,width=40,textvariable=fname).grid(row=1,column=1)
'''
Users will enter their first name here.
I save its data in variable fname for later using
'''

Label(root,text="Last name:").grid(row=2,column=0)
lname=StringVar()
Entry(root,width=40,textvariable=lname).grid(row=2,column=1)
'''
Users will enter their last name here.
I save its data in variable 'lname' for later using
'''

Label(root,text="Date of Birth(dd/mm/yyyy):").grid(row=3,column=0)
date=StringVar()
Entry(root,width=40,textvariable=date).grid(row=3,column=1)
'''
Users will enter their dates of birth here.
I save its data in variable 'date' for later using
'''







