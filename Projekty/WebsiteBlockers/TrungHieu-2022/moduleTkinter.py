from moduleFunkce import *

#Vytvorim tkinter
root = Tk()
root.title("HIEU- Website Blocker")
root.geometry('600x400') # dimension y*x
root.resizable(height=True,width=True)
root.minsize(height=300,width=300)

Label(root, text ='WEBSITE BLOCKER' ,justify=CENTER,fg="red", font ='arial 15 bold').pack() #Hlavni Nazev


Label(root, text ='Enter Website :' , font ='arial 14 bold').place(x=5 ,y=65)
#Zadejte nazev website, abyste blokoval 
Websites = Text(root,font = 'arial 10',height='2', width = '40', wrap = WORD, padx=5, pady=5)
Websites.place(x= 150,y = 60)

Label(root, text ='Unblock Website :' , font ='arial 14 bold').place(x=5 ,y=195)
#Zadejte nazev website, abyste unblokoval
WebsitesUn = Text(root,font = 'arial 10',height='2', width = '40', wrap = WORD, padx=5, pady=5)
WebsitesUn.place(x= 180,y = 190)


def MakeCenter(rooot):  #Move tkinter to center of screen
    """
    Function to move Tkinter display to the center of the screen
    Args:
      rooot: name of Tkinter Display
    """

    rooot.update_idletasks()
    width=rooot.winfo_width()
    height=rooot.winfo_height()
    x=(rooot.winfo_screenwidth()//2)-(width//2)
    y=(rooot.winfo_screenheight()//2)-(height//2)
    rooot.geometry(f'{width}x{height}+{x}+{y}')

def Block():
    # Fuction to command to Block
    Blocker(Websites,root)

def OdBlock():
    #Function to command to Unblock
    UnBlocker(WebsitesUn,root)

#Click to block
Button(root, text = 'Block',font = 'arial 12 bold',pady = 5,command = Block ,width = 6, bg = 'royal blue', activebackground = 'red').place(x = 200, y = 110)

#Click to remove blocked websites
Button(root, text = 'UnBlock',font = 'arial 12 bold',pady = 5,command = OdBlock ,width = 6, bg = 'royal blue', activebackground = 'red').place(x = 200, y = 240)



