from Modules import MainWindow

if __name__ == "__main__":
    # root = Tk()
    # root.title("Hello world app")
    # root.geometry("1200x900")
    # frm = Frame(root, padding=10)
    # frm.grid()
    # Label(frm, text="Hello World!").grid(column=0, row=0)
    # Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
    # root.mainloop()
    # path="/home/tomas/GitHub/Python/Zaklady/Scripty/Vyuka2019IT/Tkinter/text.txt"
    # print(open_file(path))
    # write_to_file(path, input("Zadej text: "))
    main = MainWindow()
    main.launch()