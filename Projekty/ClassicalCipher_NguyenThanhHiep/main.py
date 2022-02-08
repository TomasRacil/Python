from tkinter import *
from functions import *

IsPassed=False
m_Case=0

login= Tk()
login.title("Login")
login.resizable(height=False, width=False)
login.minsize(height=200,width=500)
password=StringVar()
def Pass():
    if(password.get()==m_Password):
        login.destroy()
        global IsPassed
        IsPassed=True
    else:
        Label(login,text="Please try again!").place(x=100,y=60)
Label(login,text="Enter password:").place(x=100,y=20)
Entry(login,textvariable=password,width=30).place(x=100,y=40)
Button(login,text="ENTER",command=Pass).place(x=200,y=100)
MakeCenter(login)
login.mainloop()

if IsPassed==True:
    Selection= Tk()
    Selection.title("Hello user!")
    Selection.resizable(height=False, width=False)
    Selection.minsize(height=300,width=500)

    def Case1():
        Selection.destroy()
        global m_Case
        m_Case=1
    def Case2():
        Selection.destroy()
        global m_Case
        m_Case=2
    def Case3():
        Selection.destroy()
        global m_Case
        m_Case=3
    def Case4():
        Selection.destroy()
        global m_Case
        m_Case=4
    Label(Selection,text="CLASSICAL CIPHERS",fg="green",font=("tohama",16),justify=CENTER).pack()
    Label(Selection,text="SUBSTITUTION CIPHERS").place(x=100,y=50)
    Label(Selection,text="TRANSPOSITION CIPHERS").place(x=100,y=200)
    Button(Selection,text="1. Ceasar/ Shift(posunovací)",command=Case1).place(x=300,y=50)
    Button(Selection,text="2. Your substitution cipher",command=Case2).place(x=300,y=100)
    Button(Selection, text="3. XOR",command= Case3).place(x=300,y=150)
    Button(Selection,text="1. Columnar transposition",command=Case4).place(x=300,y=200)
    MakeCenter(Selection)
    Selection.mainloop()

    root= Tk()
    root.title("hello user!")
    root.resizable(height=True, width=True)
    root.minsize(height=500,width=500)
    plaintext=StringVar()
    ciphertext=StringVar()
    encoded_Vysledek=StringVar()
    decoded_Vysledek= StringVar()
    
    def Sifrovej():
        temp=plaintext.get()
        if (m_Case==1):
            encoded_Vysledek.set(Encrypt1(temp))
        if (m_Case==2):
            encoded_Vysledek.set(Encrypt2(temp))
        if (m_Case==3):
            encoded_Vysledek.set(Encrypt3(temp))
        if (m_Case==4):
            encoded_Vysledek.set(Encrypt4(temp))
        Entry(root,textvariable=encoded_Vysledek,width=30).place(x=100,y=150)
    def Desifrovej():
        temp=ciphertext.get()
        if(m_Case==1):
            decoded_Vysledek.set(Decrypt1(temp))
        if(m_Case==2):
            decoded_Vysledek.set(Decrypt2(temp))
        if(m_Case==3):
            decoded_Vysledek.set(Decrypt3(temp))
        if(m_Case==4):
            decoded_Vysledek.set(Decrypt4(temp))
        Entry(root,textvariable=decoded_Vysledek,width=30).place(x=100,y=350)
        
    def ClearAll():
        plaintext.set("")
        ciphertext.set("")
        encoded_Vysledek.set("")
        decoded_Vysledek.set("")
        
    Label(root,text="CASE {}".format(m_Case),fg="green",font=("tohama",10),justify=CENTER).pack()
    Entry(root,textvariable=plaintext,width=30).place(x=100,y=100)
    Button(root, text="ENCRYPT",command=Sifrovej).place(x=300,y=100)
    Entry(root,textvariable=ciphertext,width=30).place(x=100,y=300)
    Button(root, text="DECRYPT",command=Desifrovej).place(x=300,y=300)
    Button(root, text="CLEAR ALL",command=ClearAll).place(x=100,y=400)
    Button(root, text="QUIT",command=root.quit).place(x=200,y=400)
    MakeCenter(root)
    root.mainloop()

