from tkinter import Tk, Entry, LabelFrame, Frame, Button, END
from random import randint


def passGenerator():
    """
    Function for simple string generator from ascii (33,126) with posible input to change lenght.
    Args:
        pwEntry: input label 
        pwLenght: int for lengt of password
        mypass: string to save value of password
        + window functions
    """
    window = Tk()
    window.title("Password Generator")

    def newRand():
        pwEntry.delete(0, END)
        pwLength = int(myEntry.get())

        myPass = ""

        for x in range(pwLength):
         myPass += chr(randint(33, 126))

        pwEntry.insert(0, myPass)

    def clipper():
        window.clipboard_clear()
        window.clipboard_append(pwEntry.get())

    # Label frame.
    lf = LabelFrame(window, text="Pozadovany pocet znaku hesla?")
    lf.pack(pady=20)

    # Create Entry Box for number of characters.
    myEntry = Entry(lf, font=("Helvetica", 12))
    myEntry.pack(pady=20, padx=20)

    # Create entry box for returned password.
    pwEntry = Entry(window, text="", font=(
        "Helvetica", 12), bd=0, bg="systembuttonface")
    pwEntry.pack(pady=20)

    # Frame for buttons.
    myFrame = Frame(window)
    myFrame.pack(pady=20)

    # Create buttons
    myButton = Button(myFrame, text="Generate Passport", command=newRand)
    myButton.grid(row=0, column=0, padx=10)

    # Copy buttons
    clipBtn = Button(myFrame, text="Copy", command=clipper)
    clipBtn.grid(row=0, column=1, padx=10)

    window.mainloop()
