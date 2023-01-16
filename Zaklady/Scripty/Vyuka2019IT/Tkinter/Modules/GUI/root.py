from tkinter import Tk, Menu
from tkinter.ttk import Frame, Label, Button
from tkinter.filedialog import askopenfilename, asksaveasfilename
from ..Functions import open_file

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
        menu.add_cascade(label='File', menu=file_menu)

        file_menu.add_command(label='Open', command=self.open_file_dialog)
        file_menu.add_command(label='Save') #, command=saveFile)
        self.root.mainloop()
        # frm = Frame(root, padding=10)
        # frm.grid()

    def open_file_dialog(self):
        path=askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        text=open_file(path)
        print(text)