from tkinter import *
from Personal_Information import *
from Security_Question import *

import random

b=c=d=e=float()

def Create():
    x=str(fname.get())
    z=str(lname.get())
    y=str(date.get())
    y=y.replace('/','')
    '''
  'x' will get the first name.
  'z' will get the last name.
  'y' will get the date of birth. but I omitted the / , so it will only contain the number
  '''

    t1=str(answer1.get())
    t2=str(answer2.get())
    t3=str(answer3.get())
    t4=str(answer4.get())
    t5=str(answer5.get())
    t6=str(answer6.get())
    t7=str(answer7.get())
    answer=[t1,t2,t3,t4,t5,t6,t7]
    '''
    t1-t7 will get the answer1-answer7.
    '''

    check=''
    while(check==''):
        check=answer[random.randint(0,6)]
    
    '''
    'check' is used for checking if the answer is empty or not.
    Because there're some questions that users dont want to answer, so the answer will be empty.
    so 'check' will choose just the 'not empty' answer
    '''

    list=[x.capitalize(),y[0:4],z.capitalize(),check[0].capitalize()]
    '''
    I capitalized the first letter of the first and last names, 
    and took the first character of 'check'
    Then I put them in the 'list'.
    '''

    b=c=d=e=0
    while ((b==c)or(b==d)or(b==e)or(c==d)or(c==e)or(d==e)):
        b=random.randint(0,3)  
        c=random.randint(0,3)
        d=random.randint(0,3)
        e=random.randint(0,3)
    a=list[b]+list[c]+list[d]+list[e]
    '''
    This selection function gives me 4 random numbers but no duplicates.
    it represents 4 elements in the 'list'. 
    Then I combine them to make a password.
    '''

    password.set(a)
    Label(root,text="Press 'Create' for another password!",fg="red",font=("tohama",12),justify=CENTER).grid(row=20,columnspan=2)
    '''
    If the user clicks 'Create' again then the whole thing will run again and they will have another hint for the password
    '''
    
frameButton=Frame()
Button(frameButton,text="Create",command=Create).pack(side=LEFT)
Button(frameButton,text="Done",command=root.quit).pack(side=LEFT)
frameButton.grid(row=18,columnspan=2)

'''
'Create' is a button made for creating password
'Done' when the users finish.
'''
password=StringVar()
Label(root,text="Strong password for you:").grid(row=19,column=0)
Entry(root,width=40,textvariable=password).grid(row=19,column=1)
'''
'password' will be got from 'Create', and then displayed on the screen
'''

