from tkinter import Tk, Menu, DoubleVar, HORIZONTAL, CENTER, IntVar, Scale
from tkinter.ttk import Frame, Label, Button, Entry
from ..Functions import otoc_do_leva, otoc_do_prava
from tkdial import Dial

class MainWindow:
    path = ""
    root = Tk()
    
    def __init__(self) -> None:
        self.root.title("Hello world app")
        self.root.geometry("1200x900")

    def launch(self):
        
        menu = Menu(self.root)
        self.root.config(menu=menu)

        file_menu = Menu(menu)
        # menu.add_cascade(label='File', menu=file_menu)

        # file_menu.add_command(label='Open', command=self.open_file_dialog)
        # file_menu.add_command(label='Save') #, command=saveFile)
        
        frm = Frame(self.root, padding=10)
        frm.grid()

        uhel= IntVar()
        
        # entry_uhel = Entry(frm, textvariable=uhel)
        # entry_uhel.pack(anchor=CENTER)
        # scale = Scale(frm, variable=uhel,from_=-180, to=180, orient=HORIZONTAL, length = 600, digits = 3)
        # scale.pack(anchor=CENTER)
        dial = Dial(self.root)
        dial.grid(padx=10, pady=10)
        # label_uhel = Label(frm, textvariable=uhel)
        # label_uhel.pack(anchor=CENTER)
        # button_otoc = Button(frm, command=lambda :otoc_do_leva(uhel.get()), text="Otoc")
        # button_otoc.pack(anchor=CENTER)
        
        self.root.mainloop()
