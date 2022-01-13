from tkinter import RIGHT, Frame, Label, Scrollbar, Tk, Menu, filedialog, Text, Y
from turtle import title 


def openFile():
    print("Open")
    
def saveFile():
    print("Save")

# create main window
window = Tk()
window.title("Simple text editor")
# window.iconbitmap()
window.geometry("1200x800")

main_frame = Frame(window)
main_frame.pack(pady=5, padx=5)

text_scroll = Scrollbar(main_frame)
text_scroll.pack(side=RIGHT, fill=Y)

text_box = Text(main_frame, width=96, height=32, font=("Roboto", 16), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set)
text_box.pack()

text_scroll.config(command=text_box.yview)

menu=Menu(window)
window.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='Open', command=openFile)
file_menu.add_command(label='Save', command=saveFile)


window.mainloop()
