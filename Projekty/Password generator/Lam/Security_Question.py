from tkinter import *
from Personal_Information import *

Label(root,text="Security questions (Press the questions which you want to answer):",fg="green",font=("tohama",11),justify=CENTER).grid(row=4,columnspan=2)

def Question1():
    Entry(root,width=40,textvariable=answer1).grid(row=11,column=1)

def Question2():
    Entry(root,width=40,textvariable=answer2).grid(row=12,column=1)

def Question3():
    Entry(root,width=40,textvariable=answer3).grid(row=13,column=1)
    
def Question4():
    Entry(root,width=40,textvariable=answer4).grid(row=14,column=1)

def Question5():
    Entry(root,width=40,textvariable=answer5).grid(row=15,column=1)

def Question6():
    Entry(root,width=40,textvariable=answer6).grid(row=16,column=1)

def Question7():
    Entry(root,width=40,textvariable=answer7).grid(row=17,column=1)

'''
7 buttons represent 7 questions. 
If the user wants a question, they will click it.
 "Entry" will help show a space to enter the answer.

'''



Button(root,text="1.What's your favorite color?",command=Question1).grid(row=11,column=0)
Button(root,text="2.What's your first pet's name?",command=Question2).grid(row=12,column=0)
Button(root,text="3.What's your favorite game?",command=Question3).grid(row=13,column=0)
Button(root,text="4.What's your dream job?",command=Question4).grid(row=14,column=0)
Button(root,text="5.Who is your best friend now?",command=Question5).grid(row=15,column=0)
Button(root,text="6.What is your favorite car?",command=Question6).grid(row=16,column=0)
Button(root,text="7.What is your best sport?",command=Question7).grid(row=17,column=0)

answer1=StringVar()
answer2=StringVar()
answer3=StringVar()
answer4=StringVar()
answer5=StringVar()
answer6=StringVar()
answer7=StringVar()
'''
I use 7 variables from answer1 to answer7 to store the answer for later using. 
Of course, if the user doesn't reply then it will be empty.

'''

