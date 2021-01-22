import tkinter as tk
from math import *

# Setting parameters of buttons
btnParams = {
'fg': '#000000',
'bg': '#efefef',
'font': ('arial', 18),
'justify':"center"
}

class Calculator:
    def __init__(self, master):
        self.equation = ""           # Equation that will be evaluated
        self.inputEquation= ""       # Equation that will show up in TextBox
        self.text_input = tk.StringVar()
        self.master = master

        # Creating TextBox

        TextBox = tk.Entry(master, font=('arial', 12),fg="#333333",textvariable=self.text_input,justify='right',borderwidth="2px")
        TextBox.place(x=10,y=10,width=200,height=40)

        # Buttons

        self.Button0=tk.Button(master, **btnParams,text="0", command=lambda: self.btnPress(0))
        self.Button0.place(x=60,y=350,width=50,height=50)

        self.Button1=tk.Button(master, **btnParams, text="1", command=lambda: self.btnPress(1))
        self.Button1.place(x=10,y=300,width=50,height=50)

        self.Button2=tk.Button(master, **btnParams, text="2",command=lambda: self.btnPress(2))
        self.Button2.place(x=60,y=300,width=50,height=50)

        self.Button3=tk.Button(master, **btnParams, text="3",command=lambda: self.btnPress(3))
        self.Button3.place(x=110,y=300,width=50,height=50)

        self.Button4=tk.Button(master, **btnParams, text="4",command=lambda: self.btnPress(4))
        self.Button4.place(x=10,y=250,width=50,height=50)
          
        self.Button5=tk.Button(master, **btnParams, text="5",command=lambda: self.btnPress(5))
        self.Button5.place(x=60,y=250,width=50,height=50)

        self.Button6=tk.Button(master, **btnParams, text="6", command=lambda: self.btnPress(6))
        self.Button6.place(x=110,y=250,width=50,height=50)
           
        self.Button7=tk.Button(master,**btnParams, text="7",command=lambda: self.btnPress(7))
        self.Button7.place(x=10,y=200,width=50,height=50)

        self.Button8=tk.Button(master, **btnParams, text="8",command=lambda: self.btnPress(8))
        self.Button8.place(x=60,y=200,width=50,height=50)
           
        self.Button9=tk.Button(master, **btnParams, text="9",command=lambda: self.btnPress(9))
        self.Button9.place(x=110,y=200,width=50,height=50)

        self.ButtonPlus=tk.Button(master, **btnParams, text="+",command=lambda: self.btnPress("+"))
        self.ButtonPlus.place(x=160,y=300,width=50,height=50)
           
        self.ButtonMinus=tk.Button(master, **btnParams, text="-",command=lambda: self.btnPress("-"))
        self.ButtonMinus.place(x=160,y=250,width=50,height=50)

        self.ButtonDiv=tk.Button(master, **btnParams, text="/",command=lambda: self.btnPress("/"))
        self.ButtonDiv.place(x=160,y=200,width=50,height=50)

        self.ButtonMultiple=tk.Button(master, **btnParams, text="*",command=lambda: self.btnPress("*"))
        self.ButtonMultiple.place(x=160,y=150,width=50,height=50)

        self.ButtonMod=tk.Button(master, **btnParams, text="%",command=lambda: self.btnPress("%"))
        self.ButtonMod.place(x=10,y=350,width=50,height=50)

        self.ButtonComma=tk.Button(master, **btnParams, text=".",command=lambda: self.btnPress("."))
        self.ButtonComma.place(x=110,y=350,width=50,height=50)

        self.ButtonLBracket=tk.Button(master, **btnParams, text="(",command=lambda: self.btnPress("("))
        self.ButtonLBracket.place(x=10,y=100,width=50,height=50)
           
        self.ButtonRBracket=tk.Button(master, **btnParams, text=")",command=lambda: self.btnPress(")"))
        self.ButtonRBracket.place(x=60,y=100,width=50,height=50)

        self.ButtonFact=tk.Button(master, **btnParams, text="x!",command=lambda: self.btnPress("!"))
        self.ButtonFact.place(x=110,y=150,width=50,height=50)
           
        self.ButtonSquare=tk.Button(master, **btnParams, text="√x",command=lambda: self.btnPress("√"))
        self.ButtonSquare.place(x=10,y=150,width=50,height=50)

        self.ButtonPow=tk.Button(master, **btnParams, text="xˆ",command=lambda: self.btnPress("ˆ"))
        self.ButtonPow.place(x=60,y=150,width=50,height=50)

        self.ButtonEquals=tk.Button(master, **btnParams, text="=",command=lambda: self.btnEquals())
        self.ButtonEquals.configure(bg='#18672e', fg='#ffffff')
        self.ButtonEquals.place(x=160,y=350,width=50,height=50)

        self.ButtonClear=tk.Button(master, **btnParams, text="C",command=lambda: self.btnClear())
        self.ButtonClear.configure(bg='#cc0000', fg='#ffffff')
        self.ButtonClear.place(x=110,y=100,width=50,height=50)
         
        self.ButtonDEL=tk.Button(master, **btnParams, text="DEL",command=lambda: self.btnDelete())
        self.ButtonDEL.configure(bg='#cc0000', fg='#ffffff')
        self.ButtonDEL.place(x=160,y=100,width=50,height=50)

# Functions

    # Puts button you press into TextBox and equation
    # equation is the core equation that will be evaluated
    # inputEquation shows up in TextBox it is not evaluated

    def btnPress(self, value):
        if len(self.inputEquation) >= 21:
            self.equation = self.equation
            self.text_input.set(self.equation)
        elif value == "√":
            self.equation = self.equation + str("sqrt(")
            self.inputEquation= self.inputEquation + str(value) + str("(")
            self.text_input.set(self.inputEquation)
        elif value == "!":
            self.equation = self.equation + str("factorial(")
            self.inputEquation= self.inputEquation + str(value) + str("(")
            self.text_input.set(self.inputEquation)
        elif value == "ˆ":
            self.equation = self.equation + str("**")
            self.inputEquation = self.inputEquation + str(value)
            self.text_input.set(self.inputEquation)
        else:
            self.equation = self.equation + str(value)
            self.inputEquation= self.inputEquation + str(value)
            self.text_input.set(self.inputEquation)

    # Deletes the last character in TextBox and the last item in string equation
    # There is difference between inputEquation and equation so we have to delete it differently

    def btnDelete(self):
        if len(self.inputEquation) == 0:            # If there is nothing in inputEquation we are not doing anything
            self.text_input.set(self.inputEquation)
        else:
            if self.inputEquation[-1] == "√":
                self.inputEquation = self.inputEquation[:-1]
                self.equation = self.equation[:-4]
            elif self.inputEquation[-1] == "!":
                self.inputEquation  =self.inputEquation[:-1]
                self.equation = self.equation[:-9]
            elif self.inputEquation[-1] == "ˆ":
                self.inputEquation = self.inputEquation[:-1]
                self.equation = self.equation[:-2]
            else:
                self.inputEquation = self.inputEquation[:-1]
                self.equation = self.equation[:-1]

            self.text_input.set(self.inputEquation)
            
        
    # Clears equation inputEquation and TextBox

    def btnClear(self):
        self.equation = ""
        self.inputEquation = ""
        self.text_input.set("")

    # Converts equation into a mathematical equation and evaluates it

    def btnEquals(self):
        try:
            self.total = str(eval(self.equation))
            self.text_input.set(self.total)
            #self.equation = self.total
        except Exception as e:
            self.text_input.set("Chyba!")
