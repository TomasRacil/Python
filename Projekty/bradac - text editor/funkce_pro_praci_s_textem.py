from tkinter import *

class Functions():
    """
    Tato třída obsahuje obsluhu tlačítek a všechny editovací funkce
    """
    # Funkce zjišťující, jaké tlačítko bylo stisknuto
    def buttonclick(self, args):
        if (args) == 1:
            self.tucne()
        if (args) == 2:
            self.kurziva()
        if (args) == 3:
            self.nadpis1()
        if (args) == 4:
            self.nadpis2()
        if (args) == 5:
            self.nadpis3()
        if (args) == 6:
            self.nadpis4()
        if (args) == 7:
            self.seznam()
        if (args) == 8:
            self.podseznam()

    #vyuziti velikosti z vyberu
    def sizecorrection(self, nadpis_size):
        if(nadpis_size == "Moc velky"):
            self.buttonclick(3)
        elif(nadpis_size == "Velky"):
            self.buttonclick(4)
        elif(nadpis_size == "Normalka"):
            self.buttonclick(5)
        elif(nadpis_size == "Maly"):
            self.buttonclick(6)
        else:
            print("Chyba ve vyberu velikosti!")
            print(nadpis_size)
            exit()

    #detekce jiz pouziteho zvetseni a pripadne odstraneni
    def checknadpis(self):
        if(self.inputeditor.get('%s-1c'%SEL_FIRST, SEL_FIRST) == "#"):
            self.inputeditor.delete('%slinestart-1c'%SEL_FIRST, SEL_FIRST)
            if(self.inputeditor.get(SEL_LAST, '%s+1c'%SEL_LAST) == "\n"):
                self.inputeditor.delete(SEL_LAST, '%s+1c'%SEL_LAST)
            return True
        else:
            return False


    # funkce pro vložení formátu text/nadpisů,... do txt pole, při stisknutí tlačítka
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
    def nadpis1(self):
        if self.checknadpis():
            return        
        if(self.inputeditor.get('%s-1c'%SEL_FIRST) != "\n"):
            self.inputeditor.insert(SEL_FIRST, "\n")
        self.inputeditor.insert(SEL_FIRST, "#")
        self.inputeditor.insert(SEL_LAST, "\n")
    def nadpis2(self):
        if self.checknadpis():
            return   
        if(self.inputeditor.get('%s-1c'%SEL_FIRST) != "\n"):
            self.inputeditor.insert(SEL_FIRST, "\n")
        self.inputeditor.insert(SEL_FIRST, "##")
        self.inputeditor.insert(SEL_LAST, "\n")
    def nadpis3(self):
        if self.checknadpis():
            return   
        if(self.inputeditor.get('%s-1c'%SEL_FIRST) != "\n"):
            self.inputeditor.insert(SEL_FIRST, "\n")
        self.inputeditor.insert(SEL_FIRST, "###")
        self.inputeditor.insert(SEL_LAST, "\n")
    def nadpis4(self):
        if self.checknadpis():
            return   
        if(self.inputeditor.get('%s-1c'%SEL_FIRST) != "\n"):
            self.inputeditor.insert(SEL_FIRST, "\n")
        self.inputeditor.insert(SEL_FIRST, "####")
        self.inputeditor.insert(SEL_LAST, "\n")
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
    def podseznam(self):
        if(self.inputeditor.get('%s-7c'%SEL_FIRST, SEL_FIRST) == "     - "):
            self.inputeditor.delete('%s-7c'%SEL_FIRST, SEL_FIRST)
        else:
            if(self.inputeditor.get('%s-1c'%SEL_FIRST, SEL_FIRST) != "\n"):
                self.inputeditor.insert(SEL_FIRST, "\n")
            self.inputeditor.insert(SEL_FIRST, "     - ")
