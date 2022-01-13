from personal import *
from tkinter import *

IsPassed=False

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
    
    def Substitution():
        Selection.destroy()
        root= Tk()
        root.title("hello user!")
        root.resizable(height=True, width=True)
        root.minsize(height=500,width=500)
        plaintext=StringVar()
        ciphertext=StringVar()
        encoded_Vysledek=StringVar()
        decoded_Vysledek= StringVar()
        
        def Desifrovej():
            decoded=""
            temp=ciphertext.get()
            for i in range(len(temp)):
                isFounded=False
                for j in range(len(m_Zobrazeni)):
                    index = m_Zobrazeni[j].find(temp[i])
                    if ( index!= -1):
                        isFounded= True
                        if (index == 0):
                            decoded+=m_Zobrazeni[j][len(m_Zobrazeni[j])-1]
                        else:
                            decoded+=m_Zobrazeni[j][index-1]
                        break
                if(isFounded== False):
                    decoded+=temp[i]
            decoded_Vysledek.set(decoded)
            Entry(root,textvariable=decoded_Vysledek,width=30).place(x=100,y=350)
        def Sifrovej():
            temp=plaintext.get()
            encoded=""
            for i in range(len(temp)):
                isFounded= False
                for j in range(len(m_Zobrazeni)):
                    index = m_Zobrazeni[j].find(temp[i])
                    if ( index!= -1):
                        isFounded= True
                        if (index == len(m_Zobrazeni[j]) - 1):
                            encoded+=m_Zobrazeni[j][0]
                        else:
                            encoded+=m_Zobrazeni[j][index+1]
                        break
                if(isFounded==False):
                    encoded+=temp[i]
            encoded_Vysledek.set(encoded)
            Entry(root,textvariable=encoded_Vysledek,width=30).place(x=100,y=150)
        def ClearAll():
            plaintext.set("")
            ciphertext.set("")
            encoded_Vysledek.set("")
            decoded_Vysledek.set("")
        
        Entry(root,textvariable=plaintext,width=30).place(x=100,y=100)
        Button(root, text="ENCRYPT",command=Sifrovej).place(x=300,y=100)
        Entry(root,textvariable=ciphertext,width=30).place(x=100,y=300)
        Button(root, text="DECRYPT",command=Desifrovej).place(x=300,y=300)
        Button(root, text="CLEAR ALL",command=ClearAll).place(x=100,y=400)
        Button(root, text="QUIT",command=root.quit).place(x=200,y=400)
        MakeCenter(root)
        root.mainloop()

    def Columnar():
        Selection.destroy()
        root= Tk()
        root.title("hello user!")
        root.resizable(height=True, width=True)
        root.minsize(height=500,width=500)
        plaintext=StringVar()
        ciphertext=StringVar()
        encoded_Vysledek=StringVar()
        decoded_Vysledek= StringVar()
        orderedList= sorted(m_Keyword)
        def Desifrovej():
            decoded=""
            temp=ciphertext.get()
            t=len(temp)//len(m_Keyword)
            for m in range(t):
                for j in range(len(orderedList)):
                    for i in range(len(m_Keyword)):
                        if orderedList[j]==m_Keyword[i]:
                            decoded+= temp[i*t+m]
            decoded_Vysledek.set(decoded)
            Entry(root,textvariable=decoded_Vysledek,width=30).place(x=100,y=350)
        def Sifrovej():
            temp=plaintext.get()
            encoded=""
            for i in range(len(m_Keyword)):
                for j in range(len(orderedList)):
                    if orderedList[j]==m_Keyword[i]:
                        k=j
                        while(k+1<=len(temp)+len(m_Keyword)-len(temp)%len(m_Keyword)):
                            if k+1<=len(temp):
                                encoded+= temp[k]
                                k+= len(m_Keyword)
                            else:
                                encoded+= "*" #libovolny znak
                                break
            encoded_Vysledek.set(encoded)
            Entry(root,textvariable=encoded_Vysledek,width=30).place(x=100,y=150)
        def ClearAll():
            plaintext.set("")
            ciphertext.set("")
            encoded_Vysledek.set("")
            decoded_Vysledek.set("")
        
        Entry(root,textvariable=plaintext,width=30).place(x=100,y=100)
        Button(root, text="ENCRYPT",command=Sifrovej).place(x=300,y=100)
        Entry(root,textvariable=ciphertext,width=30).place(x=100,y=300)
        Button(root, text="DECRYPT",command=Desifrovej).place(x=300,y=300)
        Button(root, text="CLEAR ALL",command=ClearAll).place(x=100,y=400)
        Button(root, text="QUIT",command=root.quit).place(x=200,y=400)
        MakeCenter(root)
        root.mainloop()

    def XOR():
        Selection.destroy()
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
            encoded=""
            for i in range(len(temp)):
                cislo=(m_IndexVariable+ ord(temp[i]))^m_KeyNumber
                encoded+= chr(cislo)
            encoded_Vysledek.set(encoded)
            Entry(root,textvariable=encoded_Vysledek,width=30).place(x=100,y=150)
        def Desifrovej():
            decoded=""
            temp=ciphertext.get()
            for i in range(len(temp)):
                cislo=(m_IndexVariable+ord(temp[i]))^m_KeyNumber
                decoded+= chr(cislo)
            decoded_Vysledek.set(decoded)
            Entry(root,textvariable=decoded_Vysledek,width=30).place(x=100,y=350)
        def ClearAll():
            plaintext.set("")
            ciphertext.set("")
            encoded_Vysledek.set("")
            decoded_Vysledek.set("")

        Entry(root,textvariable=plaintext,width=30).place(x=100,y=100)
        Button(root, text="ENCRYPT",command=Sifrovej).place(x=300,y=100)
        Entry(root,textvariable=ciphertext,width=30).place(x=100,y=300)
        Button(root, text="DECRYPT",command=Desifrovej).place(x=300,y=300)
        Button(root, text="CLEAR ALL",command=ClearAll).place(x=100,y=400)
        Button(root, text="QUIT",command=root.quit).place(x=200,y=400)
        MakeCenter(root)
        root.mainloop()

    def Ceasar():
        Selection.destroy()
        root= Tk()
        root.title("hello user!")
        root.resizable(height=True, width=True)
        root.minsize(height=500,width=500)
        plaintext=StringVar()
        ciphertext=StringVar()
        encoded_Vysledek=StringVar()
        decoded_Vysledek= StringVar()
        
        def Desifrovej():
            decoded=""
            temp=ciphertext.get()
            for i in range(len(temp)):
                cislo=((ord(temp[i])-m_KeyShift-32) % 95)+32  #there are 95 letters that can be printed
                decoded += chr(cislo)
            decoded_Vysledek.set(decoded)
            Entry(root,textvariable=decoded_Vysledek,width=30).place(x=100,y=350)
        def Sifrovej():
            temp=plaintext.get()
            encoded=""
            for i in range(len(temp)):
                cislo=((ord(temp[i])+m_KeyShift-32) % 95)+32
                encoded+= chr(cislo)
            encoded_Vysledek.set(encoded)
            Entry(root,textvariable=encoded_Vysledek,width=30).place(x=100,y=150)
        def ClearAll():
            plaintext.set("")
            ciphertext.set("")
            encoded_Vysledek.set("")
            decoded_Vysledek.set("")
        
        Entry(root,textvariable=plaintext,width=30).place(x=100,y=100)
        Button(root, text="ENCRYPT",command=Sifrovej).place(x=300,y=100)
        Entry(root,textvariable=ciphertext,width=30).place(x=100,y=300)
        Button(root, text="DECRYPT",command=Desifrovej).place(x=300,y=300)
        Button(root, text="CLEAR ALL",command=ClearAll).place(x=100,y=400)
        Button(root, text="QUIT",command=root.quit).place(x=200,y=400)
        MakeCenter(root)
        root.mainloop()

    Label(Selection,text="CLASSICAL CIPHERS",fg="green",font=("tohama",16),justify=CENTER).pack()
    Label(Selection,text="SUBSTITUTION CIPHERS").place(x=100,y=50)
    Label(Selection,text="TRANSPOSITION CIPHERS").place(x=100,y=200)
    Button(Selection,text="1. Ceasar/ Shift(posunovací)",command=Ceasar).place(x=300,y=50)
    Button(Selection,text="2. Your substitution cipher",command=Substitution).place(x=300,y=100)
    Button(Selection, text="3. XOR",command= XOR).place(x=300,y=150)
    Button(Selection,text="1. Columnar transposition",command=Columnar).place(x=300,y=200)
    MakeCenter(Selection)
    Selection.mainloop()

