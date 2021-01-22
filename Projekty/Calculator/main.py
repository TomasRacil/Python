from modules.calculator import *


root = tk.Tk()
c=Calculator(root)  # This creates object Calculator

# Creating GUI
root.title("Calculator")
width=220
height=411
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

root.mainloop()