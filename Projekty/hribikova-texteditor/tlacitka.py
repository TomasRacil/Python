from tkinter import SEL_FIRST, SEL_LAST


class Functions:
    """
    Tato třída obsahuje obsluhu tlačítek.
    Obsahuje pravidla formátu vložení textu při stlačení tlacítka.
    Metody - tučné písmo, kurzíva, seznam (odrážka).
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
        """
        Metoda tucne funguje tak, že když označíme text a stiskneme tlačítlo tučné,
        tak se před a za označený text přidá '**', text se při převodu na html přemění na tučné písmo.
        Pokud toto tlačítko stiskneme znovu, '**' se odeberou u označeného textu.
        """
        if self.inputeditor.get("%s-2c" % SEL_FIRST, SEL_FIRST) == "**":
            self.inputeditor.delete("%s-2c" % SEL_FIRST, SEL_FIRST)
            self.inputeditor.delete(SEL_LAST, "%s+2c" % SEL_LAST)
        else:
            self.inputeditor.insert(SEL_FIRST, "**")
            self.inputeditor.insert(SEL_LAST, "**")

    def kurziva(self):
        """
        Metoda kurziva funguje tak, že když označíme text a stiskneme tlačítlo kurzíva,
        tak se před a za označený text přidá '*', text se při převodu na html přemění na písmo s kurzívou.
        Pokud toto tlačítko stiskneme znovu, '*' se odeberou u označeného textu.
        """
        if self.inputeditor.get("%s-1c" % SEL_FIRST) == "*":
            if (
                (self.inputeditor.get("%s-2c" % SEL_FIRST, "%s-1c" % SEL_FIRST))
                == (self.inputeditor.get("%s-3c" % SEL_FIRST, "%s-2c" % SEL_FIRST))
                == "*"
            ):
                self.inputeditor.delete("%s-1c" % SEL_FIRST, SEL_FIRST)
                self.inputeditor.delete(SEL_LAST, "%s+1c" % SEL_LAST)
            elif (
                (self.inputeditor.get("%s-2c" % SEL_FIRST, "%s-1c" % SEL_FIRST)) != "*"
            ) and (
                "*" != (self.inputeditor.get("%s-3c" % SEL_FIRST, "%s-2c" % SEL_FIRST))
            ):  # za tohle se omlouvám
                self.inputeditor.delete("%s-1c" % SEL_FIRST, SEL_FIRST)
                self.inputeditor.delete(SEL_LAST, "%s+1c" % SEL_LAST)
            else:
                self.inputeditor.insert(SEL_FIRST, "*")
                self.inputeditor.insert(SEL_LAST, "*")
        else:
            self.inputeditor.insert(SEL_FIRST, "*")
            self.inputeditor.insert(SEL_LAST, "*")

    def seznam(self):
        """
        Metoda seznam funguje tak, že když označíme text a stiskneme tlačítlo odrážka,
        tak se před označený text přidá '-' a od-entruje se na další řádek,
        text se při převodu na html přemění na odsazenou odrážku na dalším řádku.
        Pokud toto tlačítko stiskneme znovu, '-' se odeberou u označeného textu.
        """
        if self.inputeditor.get("%s-3c" % SEL_FIRST, SEL_FIRST) == "\n- ":
            self.inputeditor.delete("%s-4c" % SEL_FIRST, SEL_FIRST)
            self.inputeditor.delete(SEL_LAST, "%s+1c" % SEL_LAST)
        else:
            if self.inputeditor.get("%s-1c" % SEL_FIRST, SEL_FIRST) != "\n":
                self.inputeditor.insert(SEL_FIRST, "\n")
                if (
                    self.inputeditor.get("%s-2c" % SEL_FIRST, "%s-1c" % SEL_FIRST)
                    != "\n"
                ):
                    self.inputeditor.insert(SEL_FIRST, "\n")
            self.inputeditor.insert(SEL_FIRST, "- ")
            self.inputeditor.insert(SEL_LAST, "\n")
