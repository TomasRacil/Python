from tkinter import (
    Frame,
    Button,
    Menu,
    font,
    filedialog,
    messagebox as mbox,
    RIGHT,
    LEFT,
    BOTH,
    END,
)
from tkinter.scrolledtext import ScrolledText
from markdown2 import Markdown
from tkhtmlview import HTMLLabel

# from tlacitka import *

# importujeme vše potřebné z knihoven, s kterými budeme pracovat


class Window(Frame):
    """
    Tato třída obsahuje naše vstupní, výstupní pole a formátování aplikace.
    Obsahuje vytvoření a nastavení okna, buttonbox a menu.
    Obsahuje funkce na otevírání a ukládání souboru.
    """

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.myfont = font.Font(family="Helvetica", size=14)
        self.init_window()
        self.buttonbox()

    def init_window(self):
        """
        vytvoření a nastavení okna:
        """

        self.master.title("TDOWN")

        box = Frame(master=self.master)

        self.inputeditor = ScrolledText(box, width="1", font=self.myfont)
        # musíme přidat textové pole, použijeme widget ScrolledText od tkinter o šířce 1
        # říkáme mu aby používal naše vlastní písmo místo výchozího písma
        self.inputeditor.pack(fill=BOTH, expand=1, side=LEFT)
        # poté ScrolledText zabalíme a nastavíme jak se má vyplnit do TDOWN
        box.grid(row=1, column=0, pady=0, ipadx=350, ipady=500)

        box2 = Frame(master=self.master)

        self.outputbox = HTMLLabel(box2, width="1", background="white")
        # definujeme výstup a jeho okno
        self.outputbox.pack(fill=BOTH, expand=1, side=RIGHT)
        # zabalíme jej a určíme jak se bude okno vyplňovat
        self.outputbox.fit_height()
        # díky tomuto se vejdou okna do widgetu
        self.inputeditor.bind("<<Modified>>", self.onInputChange)
        # volá funkci onInputCharge kdykoliv se změní text
        box2.grid(row=1, column=1, ipadx=350, pady=0, ipady=300)

        # vytvoření hlavního menu:
        self.mainmenu = Menu(self.master)
        # vložení filemenu do hlavního menu:
        self.filemenu = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.filemenu.add_command(label="Save as", command=self.savefile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.master.config(menu=self.mainmenu)

    def buttonbox(self):
        """
        tlačítka - tučné písmo, kurzíva, odrážky:
        """

        box = Frame(master=self.master)

        # priprava tlačítek ve výběru:
        but_tuc = Button(
            box, text="tučné", fg="black", command=lambda: self.buttonclick(1)
        )
        but_tuc.grid(row=0, column=0, ipadx=8, ipady=1)
        but_kurz = Button(
            box, text="kurzíva", fg="black", command=lambda: self.buttonclick(2)
        )
        but_kurz.grid(row=0, column=1, ipadx=8, ipady=1)
        but_sez = Button(
            box, text="odrážka", fg="black", command=lambda: self.buttonclick(3)
        )
        but_sez.grid(row=0, column=2, ipadx=8, ipady=1)
        box.grid(row=0, column=0, sticky="ew")
        # .grid() je správce geometrie stejně jako .pack()
        # vytvořením řížky raw=řádek, column=sloupec, ipadx,ipady=vylnění na ose x a y
        # sticky ew=roztahne se vodorovně

    def onInputChange(self, _):
        """
        funkce, které převádí input uživatele na html:
        """
        self.inputeditor.edit_modified(0)
        md2html = Markdown()
        self.outputbox.set_html(md2html.convert(self.inputeditor.get("1.0", END)))

    def openfile(self):
        """
        definujeme funkci pro otevírání souborů:
        """
        openfilename = filedialog.askopenfilename(
            filetypes=(
                ("Markdown File", "*.md , *.mdown , *.markdown"),
                ("Text File", "*.txt"),
                ("All Files", "*.*"),
            )
        )
        if openfilename:
            try:
                self.inputeditor.delete(1.0, END)
                self.inputeditor.insert(END, open(openfilename).read())
            except:
                # print("Cannot Open File!")
                mbox.showerror(
                    "Error Opening Selected File",
                    f"Oops!, The file you selected : {openfilename} can not be opened!",
                )

    def savefile(self):
        """
        definujeme funkci pro uložení našeho markdown vstupu:
        """
        filedata = self.inputeditor.get("1.0", END)
        savefilename = filedialog.asksaveasfilename(
            filetypes=(("Markdown File", "*.md"), ("Text File", "*.txt")),
            title="Save Markdown File",
        )
        if savefilename:
            try:
                f = open(savefilename, "w")
                f.write(filedata)
            except:
                mbox.showerror(
                    "Error Saving File",
                    f"Oops!, The File : {savefilename} can not be saved!",
                )
