# File name: TextEditor.py
# Description: Basic text editor
# Author: Tomáš Ráčil
# Date: 20-11-2020



from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *

def askQuit():
	if askyesno('Potvrzeni','Chcete skoncit?'):
		askSave()
		sys.exit()
	else:
		showinfo('zruseno')
def askSave():
	if askyesno('Potvrzeni','Chcete uložit změny'):
		save()
	else:
		pass

def dummy():
	print('Nic nedelam')

def fileOpen():
	file=askopenfile()
	editor.delete('1.0','end-1c')
	editor.insert(END,file.read())

def save():
	text=editor.get('1.0','end-1c')
	filename=asksaveasfile().name
	f=open(filename,'w')
	f.write(text)
	f.close()

def new():
	if editor.get('1.0','end-1c')!='':
		askSave()
	editor.delete('1.0', END)

def main():
	app=Tk()
	app.title('Textovy editor')
	editor=ScrolledText(app, width=150, height=80)

	menu=Menu(app)
	app.config(menu=menu)
	filemenu=Menu()
	menu.add_cascade(label='File', menu=filemenu)
	filemenu.add_command(label='New',command=new)
	filemenu.add_command(label='Open',command=fileOpen)
	filemenu.add_command(label='Save',command=save)
	filemenu.add_separator()
	filemenu.add_command(label='Exit',command=askQuit)

	helpmenu=Menu()
	menu.add_cascade(label='Help', menu=helpmenu)
	helpmenu.add_command(label='About',command=dummy)
	editor.pack()
	app.mainloop()

if __name__ == '__main__':
    main()