from GUI import *
from tkinter import * 
from tkinter.ttk import *
from .root import * 

"""Clock labels"""
clock = Label(root, text="Clock",font=('arial',30,'bold'),background='dimgray',foreground='black').pack(anchor = 'n')
lbl = Label(root, font = ('arial', 40, 'bold'), background = 'black', foreground = 'green') 
lbl.pack(anchor = 'n') 