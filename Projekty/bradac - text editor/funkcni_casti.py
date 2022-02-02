from tkinter import *
from tkinter import font , filedialog
from tkinter import messagebox as mbox
from tkinter.scrolledtext import *
from markdown2 import Markdown
from tkhtmlview import HTMLLabel


class Body(Frame):
    """
    Tato třída obsahuje formátování aplikace
    """
    # Konstruktor pro hlavní frame
    # master == root
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.myfont = font.Font(family="Times New Roman", size=16)
        self.init_window()
        self.buttonbox()

    # tlačítka pro vkládání nadpisů, seznamů, ...
    def buttonbox(self):

        # tlačítka jsou vložena ve framu, kde se rozmisťují opět grid. systémem
        box = Frame(master=self.master)

        #priprava select boxu
        OPTIONS_NAD = [
            "Moc velky",
            "Velky",
            "Normalka",
            "Maly"
        ]
        nadpis_size = StringVar(box)
        nadpis_size.set(OPTIONS_NAD[0])
        
        but_tuc = Button(box, text="tučné", fg="black", command=lambda:self.buttonclick(1))
        but_tuc.grid(row=0, column=0,ipadx=8, ipady=1)
        but_kurz = Button(box, text="kurzíva", fg="black", command=lambda:self.buttonclick(2))
        but_kurz.grid(row=0, column=1,ipadx=8, ipady=1)
        but_Nad = Button(box, text="Nadpis", fg="black", command=lambda:self.sizecorrection(nadpis_size.get()))
        but_Nad.grid(row=0, column=2,ipadx=8, ipady=1)
        sel_nad = OptionMenu(box, nadpis_size, *OPTIONS_NAD)
        sel_nad.grid(row=0, column=3, ipadx=8, ipady=1)
        but_sez = Button(box, text="Seznam", fg="black", command=lambda: self.buttonclick(7))
        but_sez.grid(row=0, column=4,ipadx=8, ipady=1)
        but_podsez = Button(box, text="Podseznam", fg="black", command=lambda: self.buttonclick(8))
        but_podsez.grid(row=0, column=5,ipadx=8, ipady=1)
        box.grid(row=0, column=0, sticky="w")


    # Funkce, které převádí input uživatele na html
    def onInputChange(self, event):
        self.inputeditor.edit_modified(0)
        md2html = Markdown()
        self.outputbox.set_html(md2html.convert(self.inputeditor.get("1.0", END)))


    # Funkce pro ukládání souboru (msbox, pokud se napodaří)
    def savefile(self):
        filedata = self.inputeditor.get("1.0", END)
        savefilename = filedialog.asksaveasfilename(filetypes=(("Markdown File", "*.md"),
                                                               ("Text File", "*.txt")), title="Save Markdown File")
        if savefilename:
            try:
                f = open(savefilename, "w")
                f.write(filedata)
            except:
                mbox.showerror("Error Saving File", "Oops!, The File : {} can not be saved!".format(savefilename))

    # Funkce pro otevření souboru (msbox, pokud se napodaří)
    def openfile(self):
        openfilename = filedialog.askopenfilename(filetypes=(("Markdown File", "*.md , *.mdown , *.markdown"),
                                                             ("Text File", "*.txt"),
                                                             ("All Files", "*.*")))
        if openfilename:
            try:
                self.inputeditor.delete(1.0, END)
                self.inputeditor.insert(END, open(openfilename).read())
            except:
                mbox.showerror("Error Opening Selected File",
                               "Oops!, The file you selected : {} can not be opened!".format(openfilename))


    # konstruktor okna
    def init_window(self):

        self.master.title("TDOWN")

        box = Frame(master=self.master)

        # txt input + scrollbar
        self.inputeditor = ScrolledText(box, width="1", font=self.myfont)
        self.inputeditor.pack(fill=Y,expand=1)
        self.inputeditor.pack(fill=BOTH, expand=1)
        box.grid(row=1, column=0,pady=0, ipadx=300, ipady=300)

        box2 = Frame(master=self.master)

        # vložení html okna + zobrazení převodu
        self.outputbox = HTMLLabel(box2, width="1", background="white")
        self.outputbox.pack(fill=BOTH)
        self.inputeditor.bind("<<Modified>>", self.onInputChange)
        box2.grid(row=1, column=1,ipadx=300,pady=0,ipady=300)

        # Vytvoření hlavního menu
        self.mainmenu = Menu(self.master)
        # vložení filemenu do hlavního menu
        self.filemenu = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.filemenu.add_command(label="Save as", command=self.savefile)
        self.master.config(menu=self.mainmenu)
