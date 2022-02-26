from tkinter import *

class Functions():
    """
    Tato třída obsahuje obsluhu tlačítek.
    """
    # funkce, která zjišťuje jaké tlačítko bylo stisknuto:
    def buttonclick(self, args):
        if (args) == 1:
            self.tucne()
        if (args) == 2:
            self.kurziva()
        if (args) == 3:
            self.seznam()

    # funkce pro vložení formátu text do txt pole, při stisknutí tlačítka
    def tucne(self):
        if(self.inputeditor.get('%s-2c'%SEL_FIRST, SEL_FIRST) == "**"):
            self.inputeditor.delete('%s-2c'%SEL_FIRST, SEL_FIRST)
            self.inputeditor.delete(SEL_LAST, '%s+2c'%SEL_LAST)
        else:
            self.inputeditor.insert(SEL_FIRST, "**")
            self.inputeditor.insert(SEL_LAST, "**")
    def kurziva(self):
        if(self.inputeditor.get('%s-1c'%SEL_FIRST) == "*"):  
            if ((self.inputeditor.get('%s-2c'%SEL_FIRST, '%s-1c'%SEL_FIRST)) == (self.inputeditor.get('%s-3c'%SEL_FIRST,'%s-2c'%SEL_FIRST)) == "*"):
                self.inputeditor.delete('%s-1c'%SEL_FIRST, SEL_FIRST)
                self.inputeditor.delete(SEL_LAST,'%s+1c'%SEL_LAST)
            elif (((self.inputeditor.get('%s-2c'%SEL_FIRST, '%s-1c'%SEL_FIRST))!= "*") and ("*" !=(self.inputeditor.get('%s-3c'%SEL_FIRST,'%s-2c'%SEL_FIRST)))): #za tohle se omlouvám
                self.inputeditor.delete('%s-1c'%SEL_FIRST, SEL_FIRST)
                self.inputeditor.delete(SEL_LAST,'%s+1c'%SEL_LAST)
            else:
                self.inputeditor.insert(SEL_FIRST, "*")
                self.inputeditor.insert(SEL_LAST, "*")
        else:
            self.inputeditor.insert(SEL_FIRST, "*")
            self.inputeditor.insert(SEL_LAST, "*")

    def seznam(self):
        if(self.inputeditor.get('%s-3c'%SEL_FIRST, SEL_FIRST) == "\n- "):
            self.inputeditor.delete('%s-4c'%SEL_FIRST, SEL_FIRST)
            self.inputeditor.delete(SEL_LAST, '%s+1c'%SEL_LAST)
        else:
            if(self.inputeditor.get('%s-1c'%SEL_FIRST, SEL_FIRST) != "\n"):
                self.inputeditor.insert(SEL_FIRST, "\n")
                if(self.inputeditor.get('%s-2c'%SEL_FIRST, '%s-1c'%SEL_FIRST) != "\n"):
                    self.inputeditor.insert(SEL_FIRST, "\n")
            self.inputeditor.insert(SEL_FIRST, "- ")
            self.inputeditor.insert(SEL_LAST, "\n")
   
