import hashlib
import sqlite3
from functools import partial
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk

from passgen import passGenerator

# Database Code 
with sqlite3.connect("Database.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
platform TEXT NOT NULL,
account TEXT NOT NULL,
password TEXT NOT NULL);
""")

# Create PopUp


def popUp(text):
    answer = simpledialog.askstring("input string", text)

    return answer

# Initiate Window


window = Tk()
window.update()

window.title("Password Vault")


def hashPassword(input):
    hash1 = hashlib.md5(input)
    hash1 = hash1.hexdigest()

    return hash1

#   Set up master password screen #######################################


def firstTimeScreen():
    window.geometry("250x150")

    lbl = Label(window, text="Create Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window, text="Re-enter Password")
    lbl1.config(anchor=CENTER)
    lbl1.pack()

    txt1 = Entry(window, width=20, show="*")
    txt1.pack()

    def savePassword():
        if txt.get() == txt1.get():
            hashedPassword = hashPassword(txt.get().encode('utf-8'))

            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [hashedPassword])
            db.commit()
            vaultScreen()

        else:
            lbl.config(text="Passwords don't match")

    btn = Button(window, text="Save", command=savePassword)
    btn.pack(pady=5)

#   Login screen #######################################


def loginScreen():
    window.geometry("250x100")

    lbl = Label(window, text="Enter Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window)
    lbl1.pack()

    def getMasterPassword():
        checkhashedpassword = hashPassword(txt.get().encode("utf-8"))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [checkhashedpassword])

        return cursor.fetchall()

    def checkPassword():
        password = getMasterPassword()

        if password:
            vaultScreen()

        else:
            txt.delete(0, 'end')
            lbl1.config(text="Wrong Password")

    btn = Button(window, text="Submit", command=checkPassword)
    btn.pack(pady=5)

#   Vault functionalities #######################################


def vaultScreen():
    for widget in window.winfo_children():
        widget.destroy()

    def addEntry():
        text1 = "Platform"
        text2 = "Account"
        text3 = "Password"

        platform = popUp(text1)
        account = popUp(text2)
        password = popUp(text3)

        insert_fields = """INSERT INTO vault(platform, account, password)
        VALUES(?, ?, ?)"""

        cursor.execute(insert_fields, (platform, account, password))
        db.commit()
        vaultScreen()

    def updateEntry(input):
        update = "Type new password"
        password = popUp(update)

        cursor.execute("UPDATE vault SET password = ? WHERE id = ?", (password, input,))
        db.commit()
        vaultScreen()

    def removeEntry(input):
        cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
        db.commit()
        vaultScreen()

    def copyAcc(input):
        window.clipboard_clear()
        window.clipboard_append(input)

    def copyPass(input):
        window.clipboard_clear()
        window.clipboard_append(input)

#   Window layout #######################################

    window.geometry("650x350")
    main_frame = Frame(window)
    main_frame.pack(fill=BOTH, expand=1)
    
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    lbl = Label(second_frame, text="Password Vault")
    lbl.grid(column=2)

    btn2 = Button(second_frame, text="Generate Password", command=passGenerator)
    btn2.grid(column=2, pady=10)

    btn = Button(second_frame, text="Store New", command=addEntry)
    btn.grid(column=4, pady=10)

    lbl = Label(second_frame, text="Platform")
    lbl.grid(row=2, column=0, padx=40)
    lbl = Label(second_frame, text="Account")
    lbl.grid(row=2, column=1, padx=40)
    lbl = Label(second_frame, text="Password")
    lbl.grid(row=2, column=2, padx=40)

    cursor.execute("SELECT * FROM vault")

#   Buttons Layout #######################################

    if cursor.fetchall() is not None:
        i = 0
        while True:
            cursor.execute("SELECT * FROM vault")
            array = cursor.fetchall()

            lbl1 = Label(second_frame, text=(array[i][1]))
            lbl1.grid(column=0, row=i + 3)
            lbl2 = Label(second_frame, text=(array[i][2]))
            lbl2.grid(column=1, row=i + 3)
            lbl3 = Label(second_frame, text=(array[i][3]))
            lbl3.grid(column=2, row=i + 3)
            btn2 = Button(second_frame, text="Copy Acc", command=partial(copyAcc, array[i][2]))
            btn2.grid(column=3, row=i + 3, pady=10)
            btn3 = Button(second_frame, text="Copy Pass", command=partial(copyPass, array[i][3]))
            btn3.grid(column=4, row=i + 3, pady=10)
            btn1 = Button(second_frame, text="Update", command=partial(updateEntry, array[i][0]))
            btn1.grid(column=5, row=i + 3, pady=10)
            btn = Button(second_frame, text="Delete", command=partial(removeEntry, array[i][0]))
            btn.grid(column=6, row=i + 3, pady=10)

            i = i + 1

            cursor.execute("SELECT * FROM vault")
            if len(cursor.fetchall()) <= i:
                break


cursor.execute("SELECT * FROM masterpassword")
if cursor.fetchall():
    loginScreen()
else:
    firstTimeScreen()
window.mainloop()
