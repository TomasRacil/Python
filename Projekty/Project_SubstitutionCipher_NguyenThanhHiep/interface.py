from personal import *
from tkinter import *

root= Tk()
root.title("Substitution Cipher")
root.resizable(height=False, width=False)
root.minsize(height=200,width=500)

password=StringVar()

def Pass():
    if(password.get()==m_Password):
        root.destroy()
    else:
        Label(root,text="Please try again!").place(x=100,y=60)

Label(root,text="Enter password:").place(x=100,y=20)
Entry(root,textvariable=password,width=30).place(x=100,y=40)
Button(root,text="ENTER",command=Pass).place(x=200,y=100)
def MakeCenter(rooot):  #Move tkinter to center of screen
    rooot.update_idletasks()
    width=rooot.winfo_width()
    height=rooot.winfo_height()
    x=(rooot.winfo_screenwidth()//2)-(width//2)
    y=(rooot.winfo_screenheight()//2)-(height//2)
    rooot.geometry(f'{width}x{height}+{x}+{y}')

MakeCenter(root)
root.mainloop()

root= Tk()
root.title("hello user")
root.resizable(height=True, width=True)
root.minsize(height=500,width=500)

text=StringVar()
encoded_text=StringVar()
encoded_Vysledek=StringVar()
decoded_Vysledek= StringVar()

def Sifrovej():
    temp=text.get()
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

def Desifrovej():
    decoded=""
    temp=encoded_text.get()
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

def ClearAll():
    text.set("")
    encoded_text.set("")
    encoded_Vysledek.set("")
    decoded_Vysledek.set("")



Entry(root,textvariable=text,width=30).place(x=100,y=100)
Button(root, text="ENCRYPT",command=Sifrovej).place(x=300,y=100)


Entry(root,textvariable=encoded_text,width=30).place(x=100,y=300)
Button(root, text="DECRYPT",command=Desifrovej).place(x=300,y=300)


Button(root, text="CLEAR ALL",command=ClearAll).place(x=100,y=400)
Button(root, text="QUIT",command=root.quit).place(x=200,y=400)

MakeCenter(root)
root.mainloop()